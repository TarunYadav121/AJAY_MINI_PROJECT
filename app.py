import json
import random
from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from data import (STUDENTS, INTERVENTIONS_LIST, INTERVENTION_TYPES, MAJORS,
                  add_intervention, update_intervention_status, get_type_info,
                  add_student)
from model import predict

app = Flask(__name__)
app.secret_key = "edurisk-secret-2026"

# ── helpers ──────────────────────────────────────────────
def get_student(sid):
    return next((s for s in STUDENTS if s["id"] == sid), None)

def make_trend(student, risk_index):
    rng = random.Random(student["id"] * 7)
    base = risk_index / 3.0 * 100
    trend = []
    for i in range(6):
        noise = rng.uniform(-10, 10)
        val = max(5, min(98, base + noise + (i - 3) * rng.uniform(-2, 2)))
        trend.append(round(val))
    return trend

def enrich(student):
    s = dict(student)
    result = predict(s)
    s.update(result)
    s["trend"] = make_trend(student, result["risk_index"])
    s["initials"] = "".join(w[0] for w in s["name"].split()[:2]).upper()
    return s

def all_enriched():
    return [enrich(s) for s in STUDENTS]

def get_stats(enriched_list):
    return {
        "total":    len(enriched_list),
        "critical": sum(1 for s in enriched_list if s["risk_level"] == "Critical"),
        "high":     sum(1 for s in enriched_list if s["risk_level"] == "High"),
        "medium":   sum(1 for s in enriched_list if s["risk_level"] == "Medium"),
        "low":      sum(1 for s in enriched_list if s["risk_level"] == "Low"),
    }

def iv_with_student(iv):
    """Attach student info and type info to an intervention dict."""
    d = dict(iv)
    d["student"] = get_student(iv["student_id"])
    d["type_info"] = get_type_info(iv["type"])
    # attach risk level of student
    if d["student"]:
        pred = predict(d["student"])
        d["student_risk"] = pred["risk_level"]
        d["student_risk_color"] = pred["risk_color"]
    else:
        d["student_risk"] = "Unknown"
        d["student_risk_color"] = "low"
    return d

# ── auth ─────────────────────────────────────────────────
@app.route("/")
def index():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    session["user"] = "Advisor"
    return redirect(url_for("dashboard"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

# ── dashboard ────────────────────────────────────────────
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("index"))
    all_s = all_enriched()
    stats = get_stats(all_s)

    # top 8 by risk score descending
    top8 = sorted(all_s, key=lambda x: x["risk_score"], reverse=True)[:8]

    # donut chart data
    donut = [stats["critical"], stats["high"], stats["medium"], stats["low"]]

    # line chart: 6-month trend data (Nov–Apr) per risk level
    months = ["Nov", "Dec", "Jan", "Feb", "Mar", "Apr"]
    line_data = {
        "critical": [5, 6, 6, 7, 6, stats["critical"]],
        "high":     [13, 12, 11, 10, 10, stats["high"]],
        "medium":   [9, 10, 11, 12, 13, stats["medium"]],
        "low":      [8, 8, 9, 9, 9, stats["low"]],
    }

    # active interventions count
    active_iv = sum(1 for iv in INTERVENTIONS_LIST if iv["status"] == "active")
    resolved_iv = sum(1 for iv in INTERVENTIONS_LIST if iv["status"] == "resolved")

    return render_template("dashboard.html",
        stats=stats, top8=top8, donut=donut,
        months=json.dumps(months), line_data=json.dumps(line_data),
        active_iv=active_iv, resolved_iv=resolved_iv,
        total_iv=len(INTERVENTIONS_LIST))

# ── students ─────────────────────────────────────────────
@app.route("/students")
def students():
    if "user" not in session:
        return redirect(url_for("index"))
    all_s = all_enriched()
    stats = get_stats(all_s)

    risk_filter = request.args.get("risk", "all")
    search = request.args.get("q", "").strip().lower()
    sort = request.args.get("sort", "risk_score")

    filtered = all_s
    if risk_filter != "all":
        filtered = [s for s in filtered if s["risk_level"].lower() == risk_filter]
    if search:
        filtered = [s for s in filtered if
                    search in s["name"].lower() or
                    search in s["major"].lower() or
                    search in s["email"].lower()]

    filtered.sort(key=lambda x: x.get(sort, 0), reverse=True)

    return render_template("students.html", students=filtered, stats=stats,
                           risk_filter=risk_filter, search=request.args.get("q", ""),
                           sort=sort, majors=MAJORS)

@app.route("/students/add", methods=["POST"])
def add_student_route():
    if "user" not in session:
        return redirect(url_for("index"))
    add_student(
        name             = request.form.get("name", ""),
        email            = request.form.get("email", ""),
        age              = request.form.get("age", 18),
        year             = request.form.get("year", 1),
        major            = request.form.get("major", ""),
        gpa              = request.form.get("gpa", 2.0),
        attendance       = request.form.get("attendance", 70),
        assignments_done = request.form.get("assignments_done", 70),
        engagement       = request.form.get("engagement", 70),
        failed_courses   = request.form.get("failed_courses", 0),
        financial_aid    = request.form.get("financial_aid", "false"),
    )
    return redirect(url_for("students"))

@app.route("/students/<int:sid>")
def student_detail(sid):
    if "user" not in session:
        return redirect(url_for("index"))
    student = get_student(sid)
    if not student:
        return "Student not found", 404
    s = enrich(student)
    all_ids = [x["id"] for x in STUDENTS]
    idx = all_ids.index(sid)
    prev_id = all_ids[idx - 1] if idx > 0 else None
    next_id = all_ids[idx + 1] if idx < len(all_ids) - 1 else None
    # student's own interventions
    s_ivs = [iv_with_student(iv) for iv in INTERVENTIONS_LIST if iv["student_id"] == sid]
    return render_template("student_detail.html", s=s, prev_id=prev_id, next_id=next_id, s_ivs=s_ivs)

# ── interventions ─────────────────────────────────────────
@app.route("/interventions")
def interventions():
    if "user" not in session:
        return redirect(url_for("index"))
    status_filter = request.args.get("status", "all")
    ivs = [iv_with_student(iv) for iv in INTERVENTIONS_LIST]
    if status_filter != "all":
        ivs = [iv for iv in ivs if iv["status"] == status_filter]
    counts = {
        "total":    len(INTERVENTIONS_LIST),
        "active":   sum(1 for iv in INTERVENTIONS_LIST if iv["status"] == "active"),
        "pending":  sum(1 for iv in INTERVENTIONS_LIST if iv["status"] == "pending"),
        "resolved": sum(1 for iv in INTERVENTIONS_LIST if iv["status"] == "resolved"),
    }
    return render_template("interventions.html",
        ivs=ivs, counts=counts, status_filter=status_filter,
        students=STUDENTS, intervention_types=INTERVENTION_TYPES)

@app.route("/interventions/create", methods=["POST"])
def create_intervention():
    if "user" not in session:
        return redirect(url_for("index"))
    student_id  = request.form.get("student_id")
    itype       = request.form.get("type")
    description = request.form.get("description", "").strip()
    if student_id and itype and description:
        add_intervention(student_id, itype, description)
    return redirect(url_for("interventions"))

@app.route("/interventions/<int:iv_id>/status", methods=["POST"])
def update_iv_status(iv_id):
    if "user" not in session:
        return redirect(url_for("index"))
    status = request.form.get("status")
    update_intervention_status(iv_id, status)
    return redirect(url_for("interventions"))

if __name__ == "__main__":
    app.run(debug=True)
