# EduRisk Monitor

AI-powered student dropout risk prediction and intervention tracking system built with Python, Flask, and scikit-learn.

---

## What it does

EduRisk Monitor analyzes student data — GPA, attendance, assignment completion, engagement, and failed courses — to predict dropout risk using a machine learning model. Advisors can monitor all students from a dashboard, view individual risk profiles, and log/track interventions.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12, Flask 3.x |
| ML Model | scikit-learn (RandomForestClassifier) |
| Data | NumPy, in-memory Python dicts |
| Frontend | Jinja2 templates, Chart.js (CDN), vanilla CSS |
| Charts | Chart.js 4.4 (donut + line graphs) |

---

## Project Structure

```
edurisk-monitor/
├── app.py                  # Flask routes and app logic
├── model.py                # ML model (RandomForest, training, prediction)
├── data.py                 # Student data, intervention types, in-memory store
├── requirements.txt        # Python dependencies
├── templates/
│   ├── base.html           # Sidebar layout, topbar, Chart.js import
│   ├── index.html          # Landing / login page (standalone)
│   ├── dashboard.html      # Dashboard with charts and top-8 table
│   ├── students.html       # Student risk list with filters
│   ├── student_detail.html # Individual student AI analysis page
│   └── interventions.html  # Interventions list + New Intervention modal
└── static/
    └── style.css           # Full dark theme stylesheet
```

---

## Setup & Run

**1. Install dependencies**
```bash
pip install flask scikit-learn numpy
```

**2. Run the app**
```bash
cd edurisk-monitor
python app.py
```

**3. Open in browser**
```
http://127.0.0.1:5000
```

Click **Sign in with Internet Identity** to enter the dashboard.

---

## Pages

| Route | Page |
|---|---|
| `/` | Landing / login |
| `/dashboard` | Main dashboard with charts |
| `/students` | Student risk list |
| `/students/<id>` | Individual student detail |
| `/interventions` | Interventions tracker |

---

## How the ML Model Works

The model is a `RandomForestClassifier` trained on 2000 synthetic students at startup (`model.py`). It uses 5 features:

| Feature | Weight (approx) |
|---|---|
| GPA | 35% |
| Attendance | 30% |
| Assignments Done | 20% |
| Engagement | 10% |
| Failed Courses | 5% |

It outputs one of 4 risk levels:

| Level | Description |
|---|---|
| 🟢 Low | Student on track |
| 🟡 Medium | Monitor closely |
| 🟠 High | Advisor meeting needed |
| 🔴 Critical | Immediate intervention required |

The risk score (0–100%) is a weighted probability across all classes, not just the confidence of the predicted class.

---

## How to Add a New Student

Open `data.py` and append a new entry to the `STUDENTS` list:

```python
{"id": 41,
 "name": "Jane Doe",
 "email": "jane.doe@university.edu",
 "age": 21,
 "year": 2,
 "major": "Computer Science",
 "gpa": 2.5,
 "attendance": 60,
 "assignments_done": 55,
 "engagement": 50,
 "failed_courses": 1,
 "financial_aid": True},
```

Save the file — Flask auto-reloads and the student appears everywhere instantly with a live ML risk prediction.

---

## How Charts Work

The dashboard uses **Chart.js** loaded from CDN. Data flows from Python → JSON → JavaScript:

```python
# app.py
donut = [stats["critical"], stats["high"], stats["medium"], stats["low"]]
line_data = {"critical": [5,6,6,7,6, stats["critical"]], ...}
return render_template("dashboard.html", donut=donut, line_data=json.dumps(line_data))
```

```javascript
// dashboard.html
const donut = {{ donut|safe }};
new Chart(document.getElementById('donutChart'), { type: 'doughnut', data: { datasets: [{ data: donut }] } });
```

The last data point in each line series is always the real live count from the ML model.

---

## Intervention Types

| Type | Icon |
|---|---|
| Academic Counseling | 🎓 |
| Attendance Warning | ⚠️ |
| Financial Aid | 💲 |
| Mental Health Support | 🧠 |
| Peer Tutoring | 👥 |
| Faculty Meeting | 📖 |
| Other | ❓ |

Interventions have three statuses: **Active**, **Pending**, **Resolved**. Advisors can change status directly from the interventions page.

---

## Notes

- All data is in-memory. Restarting the server resets any interventions created through the UI (pre-seeded ones in `data.py` persist).
- To persist data across restarts, replace the `STUDENTS` list and `INTERVENTIONS_LIST` in `data.py` with a SQLite database using Flask-SQLAlchemy.
- The ML model retrains from scratch on every server start (takes ~1 second).
