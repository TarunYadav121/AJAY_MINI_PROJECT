import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Risk levels
RISK_LEVELS = {0: "Low", 1: "Medium", 2: "High", 3: "Critical"}
RISK_COLORS = {0: "low", 1: "medium", 2: "high", 3: "critical"}

def _build_model():
    rng = np.random.RandomState(42)
    n = 2000
    # features: gpa, attendance, assignments_done, engagement, failed_courses
    gpa            = rng.uniform(1.0, 4.0, n)
    attendance     = rng.uniform(20, 100, n)
    assignments    = rng.uniform(20, 100, n)
    engagement     = rng.uniform(10, 100, n)
    failed_courses = rng.randint(0, 6, n)

    # dropout risk score: 0.0 (safe) → 1.0 (certain dropout)
    raw = (
        (4.0 - gpa) / 3.0          * 0.35 +   # low GPA = high risk
        (100 - attendance) / 80.0  * 0.30 +   # low attendance = high risk
        (100 - assignments) / 80.0 * 0.20 +   # low assignments = high risk
        (100 - engagement) / 90.0  * 0.10 +   # low engagement = high risk
        failed_courses / 5.0       * 0.05      # more failures = high risk
    )
    score = np.clip(raw, 0, 1)

    # 4 balanced classes: Low < 0.25, Medium 0.25-0.50, High 0.50-0.75, Critical >= 0.75
    labels = np.digitize(score, bins=[0.25, 0.50, 0.75])

    X = np.column_stack([gpa, attendance, assignments, engagement, failed_courses])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    clf = RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced")
    clf.fit(X_scaled, labels)
    return clf, scaler

_clf, _scaler = _build_model()

def predict(student: dict) -> dict:
    gpa   = student["gpa"]
    att   = student["attendance"]
    asgn  = student["assignments_done"]
    eng   = student["engagement"]
    fails = student["failed_courses"]

    X = np.array([[gpa, att, asgn, eng, fails]])
    X_scaled = _scaler.transform(X)

    risk_idx = int(_clf.predict(X_scaled)[0])
    proba    = _clf.predict_proba(X_scaled)[0]

    # risk_score = weighted sum of class probabilities (0=low,1=med,2=high,3=crit)
    # gives a 0-100 dropout risk percentage, not just confidence of predicted class
    classes = _clf.classes_
    risk_score = int(round(sum(classes[i] * proba[i] for i in range(len(classes))) / 3.0 * 100))

    importances = _clf.feature_importances_
    factors = [
        {"name": "GPA",              "value": gpa,   "weight": round(importances[0]*100, 1)},
        {"name": "Attendance",       "value": att,   "weight": round(importances[1]*100, 1)},
        {"name": "Assignments Done", "value": asgn,  "weight": round(importances[2]*100, 1)},
        {"name": "Engagement",       "value": eng,   "weight": round(importances[3]*100, 1)},
        {"name": "Failed Courses",   "value": fails, "weight": round(importances[4]*100, 1)},
    ]

    return {
        "risk_level": RISK_LEVELS[risk_idx],
        "risk_color": RISK_COLORS[risk_idx],
        "risk_score": risk_score,
        "risk_index": risk_idx,
        "factors": factors,
        "probabilities": {RISK_LEVELS[i]: round(float(p)*100, 1) for i, p in enumerate(proba)},
    }
