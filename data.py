import random
random.seed(42)

STUDENTS = [
    {"id": 1,  "name": "Marcus Johnson",   "email": "marcus.johnson@university.edu",   "age": 22, "year": 2, "major": "Computer Science",      "gpa": 1.8, "attendance": 31, "assignments_done": 35, "engagement": 28, "failed_courses": 3, "financial_aid": False},
    {"id": 2,  "name": "Fatima Al-Hassan", "email": "fatima.al-hassan@university.edu", "age": 21, "year": 2, "major": "Engineering",            "gpa": 1.9, "attendance": 33, "assignments_done": 37, "engagement": 30, "failed_courses": 3, "financial_aid": False},
    {"id": 3,  "name": "Diego Rivera",     "email": "diego.rivera@university.edu",     "age": 20, "year": 1, "major": "Medicine",               "gpa": 1.7, "attendance": 29, "assignments_done": 32, "engagement": 25, "failed_courses": 4, "financial_aid": False},
    {"id": 4,  "name": "Kevin Osei",       "email": "kevin.osei@university.edu",       "age": 24, "year": 4, "major": "Arts",                   "gpa": 1.8, "attendance": 30, "assignments_done": 34, "engagement": 27, "failed_courses": 3, "financial_aid": False},
    {"id": 5,  "name": "Aisha Patel",      "email": "aisha.patel@university.edu",      "age": 22, "year": 3, "major": "Business Administration", "gpa": 1.9, "attendance": 32, "assignments_done": 36, "engagement": 29, "failed_courses": 3, "financial_aid": False},
    {"id": 6,  "name": "Priya Sharma",     "email": "priya.sharma@university.edu",     "age": 20, "year": 1, "major": "Computer Science",       "gpa": 2.0, "attendance": 34, "assignments_done": 38, "engagement": 31, "failed_courses": 2, "financial_aid": False},
    {"id": 7,  "name": "James Okonkwo",    "email": "james.okonkwo@university.edu",    "age": 23, "year": 3, "major": "Computer Science",       "gpa": 2.2, "attendance": 50, "assignments_done": 44, "engagement": 38, "failed_courses": 2, "financial_aid": False},
    {"id": 8,  "name": "Mei Lin Chen",     "email": "mei.lin.chen@university.edu",     "age": 20, "year": 1, "major": "Business Administration", "gpa": 2.3, "attendance": 52, "assignments_done": 46, "engagement": 40, "failed_courses": 2, "financial_aid": False},
    {"id": 9,  "name": "Brian Okafor",     "email": "brian.okafor@university.edu",     "age": 22, "year": 2, "major": "Business Admin",         "gpa": 2.1, "attendance": 54, "assignments_done": 48, "engagement": 35, "failed_courses": 2, "financial_aid": False},
    {"id": 10, "name": "Carla Mendes",     "email": "carla.mendes@university.edu",     "age": 21, "year": 2, "major": "Nursing",                "gpa": 3.2, "attendance": 80, "assignments_done": 78, "engagement": 72, "failed_courses": 0, "financial_aid": True},
    {"id": 11, "name": "Eva Rossi",        "email": "eva.rossi@university.edu",        "age": 19, "year": 1, "major": "Psychology",             "gpa": 3.5, "attendance": 88, "assignments_done": 90, "engagement": 85, "failed_courses": 0, "financial_aid": True},
    {"id": 12, "name": "Felix Nguyen",     "email": "felix.nguyen@university.edu",     "age": 24, "year": 3, "major": "Mathematics",            "gpa": 2.4, "attendance": 61, "assignments_done": 55, "engagement": 50, "failed_courses": 1, "financial_aid": False},
    {"id": 13, "name": "Grace Patel",      "email": "grace.patel@university.edu",      "age": 20, "year": 2, "major": "Biology",                "gpa": 3.9, "attendance": 95, "assignments_done": 97, "engagement": 93, "failed_courses": 0, "financial_aid": True},
    {"id": 14, "name": "Henry Dubois",     "email": "henry.dubois@university.edu",     "age": 22, "year": 2, "major": "History",                "gpa": 1.5, "attendance": 38, "assignments_done": 30, "engagement": 22, "failed_courses": 4, "financial_aid": False},
    {"id": 15, "name": "Isla Torres",      "email": "isla.torres@university.edu",      "age": 21, "year": 2, "major": "Chemistry",              "gpa": 2.9, "attendance": 70, "assignments_done": 68, "engagement": 60, "failed_courses": 1, "financial_aid": True},
    {"id": 16, "name": "Kira Yamamoto",    "email": "kira.yamamoto@university.edu",    "age": 20, "year": 1, "major": "Art & Design",           "gpa": 3.6, "attendance": 85, "assignments_done": 88, "engagement": 80, "failed_courses": 0, "financial_aid": True},
    {"id": 17, "name": "Liam Bakker",      "email": "liam.bakker@university.edu",      "age": 22, "year": 3, "major": "Economics",              "gpa": 1.9, "attendance": 45, "assignments_done": 40, "engagement": 32, "failed_courses": 3, "financial_aid": False},
    {"id": 18, "name": "Mia Fernandez",    "email": "mia.fernandez@university.edu",    "age": 19, "year": 1, "major": "Sociology",              "gpa": 3.3, "attendance": 82, "assignments_done": 80, "engagement": 75, "failed_courses": 0, "financial_aid": True},
    {"id": 19, "name": "Noah Andersen",    "email": "noah.andersen@university.edu",    "age": 24, "year": 4, "major": "Law",                    "gpa": 2.6, "attendance": 65, "assignments_done": 60, "engagement": 55, "failed_courses": 1, "financial_aid": False},
    {"id": 20, "name": "Olivia Chukwu",    "email": "olivia.chukwu@university.edu",    "age": 21, "year": 2, "major": "Medicine",               "gpa": 3.7, "attendance": 90, "assignments_done": 93, "engagement": 87, "failed_courses": 0, "financial_aid": True},
    {"id": 21, "name": "Paul Svensson",    "email": "paul.svensson@university.edu",    "age": 23, "year": 3, "major": "Architecture",           "gpa": 2.2, "attendance": 56, "assignments_done": 50, "engagement": 42, "failed_courses": 2, "financial_aid": False},
    {"id": 22, "name": "Quinn Moreau",     "email": "quinn.moreau@university.edu",     "age": 20, "year": 1, "major": "Philosophy",             "gpa": 3.0, "attendance": 74, "assignments_done": 72, "engagement": 65, "failed_courses": 0, "financial_aid": True},
    {"id": 23, "name": "Rosa Alves",       "email": "rosa.alves@university.edu",       "age": 22, "year": 2, "major": "Education",              "gpa": 1.6, "attendance": 40, "assignments_done": 33, "engagement": 25, "failed_courses": 3, "financial_aid": False},
    {"id": 24, "name": "Sam Kowalski",     "email": "sam.kowalski@university.edu",     "age": 21, "year": 2, "major": "IT & Networks",          "gpa": 2.8, "attendance": 68, "assignments_done": 65, "engagement": 58, "failed_courses": 1, "financial_aid": True},
    {"id": 25, "name": "Tina Okonkwo",     "email": "tina.okonkwo@university.edu",     "age": 23, "year": 3, "major": "Public Health",          "gpa": 3.4, "attendance": 84, "assignments_done": 86, "engagement": 78, "failed_courses": 0, "financial_aid": True},
    {"id": 26, "name": "Uma Petrov",       "email": "uma.petrov@university.edu",       "age": 20, "year": 1, "major": "Linguistics",            "gpa": 2.3, "attendance": 58, "assignments_done": 52, "engagement": 45, "failed_courses": 2, "financial_aid": False},
    {"id": 27, "name": "Victor Diallo",    "email": "victor.diallo@university.edu",    "age": 24, "year": 4, "major": "Finance",                "gpa": 1.7, "attendance": 43, "assignments_done": 37, "engagement": 30, "failed_courses": 3, "financial_aid": False},
    {"id": 28, "name": "Wendy Larsson",    "email": "wendy.larsson@university.edu",    "age": 19, "year": 1, "major": "Music",                  "gpa": 3.1, "attendance": 76, "assignments_done": 74, "engagement": 68, "failed_courses": 0, "financial_aid": True},
    {"id": 29, "name": "Xander Mwangi",   "email": "xander.mwangi@university.edu",    "age": 22, "year": 2, "major": "Geography",              "gpa": 2.5, "attendance": 63, "assignments_done": 57, "engagement": 48, "failed_courses": 1, "financial_aid": False},
    {"id": 30, "name": "Yara Hassan",      "email": "yara.hassan@university.edu",      "age": 21, "year": 2, "major": "Political Science",      "gpa": 3.6, "attendance": 87, "assignments_done": 89, "engagement": 82, "failed_courses": 0, "financial_aid": True},
    {"id": 31, "name": "Zoe Bergmann",     "email": "zoe.bergmann@university.edu",     "age": 23, "year": 3, "major": "Environmental Sci.",     "gpa": 2.0, "attendance": 48, "assignments_done": 42, "engagement": 35, "failed_courses": 2, "financial_aid": False},
    {"id": 32, "name": "Aaron Nkosi",      "email": "aaron.nkosi@university.edu",      "age": 20, "year": 1, "major": "Statistics",             "gpa": 3.8, "attendance": 91, "assignments_done": 94, "engagement": 89, "failed_courses": 0, "financial_aid": True},
    {"id": 33, "name": "Bella Fontaine",   "email": "bella.fontaine@university.edu",   "age": 22, "year": 2, "major": "Journalism",             "gpa": 1.9, "attendance": 46, "assignments_done": 39, "engagement": 31, "failed_courses": 3, "financial_aid": False},
    {"id": 34, "name": "Carlos Reyes",     "email": "carlos.reyes@university.edu",     "age": 21, "year": 2, "major": "Anthropology",           "gpa": 2.7, "attendance": 66, "assignments_done": 62, "engagement": 54, "failed_courses": 1, "financial_aid": True},
    {"id": 35, "name": "Diana Volkov",     "email": "diana.volkov@university.edu",     "age": 24, "year": 4, "major": "Biochemistry",           "gpa": 3.5, "attendance": 86, "assignments_done": 91, "engagement": 84, "failed_courses": 0, "financial_aid": True},
    {"id": 36, "name": "Ethan Mbeki",      "email": "ethan.mbeki@university.edu",      "age": 20, "year": 1, "major": "Computer Science",       "gpa": 2.1, "attendance": 53, "assignments_done": 47, "engagement": 36, "failed_courses": 2, "financial_aid": False},
    {"id": 37, "name": "Fiona Castillo",   "email": "fiona.castillo@university.edu",   "age": 22, "year": 2, "major": "Nursing",                "gpa": 3.3, "attendance": 81, "assignments_done": 79, "engagement": 73, "failed_courses": 0, "financial_aid": True},
    {"id": 38, "name": "George Tanaka",    "email": "george.tanaka@university.edu",    "age": 23, "year": 3, "major": "Engineering",            "gpa": 1.8, "attendance": 41, "assignments_done": 34, "engagement": 27, "failed_courses": 3, "financial_aid": False},
    {"id": 39, "name": "Hannah Osei",      "email": "hannah.osei@university.edu",      "age": 19, "year": 1, "major": "Psychology",             "gpa": 3.7, "attendance": 89, "assignments_done": 92, "engagement": 86, "failed_courses": 0, "financial_aid": True},
    {"id": 40, "name": "Ivan Petrov",      "email": "ivan.petrov@university.edu",      "age": 24, "year": 4, "major": "Mathematics",            "gpa": 2.4, "attendance": 60, "assignments_done": 54, "engagement": 49, "failed_courses": 1, "financial_aid": False},
]

# Intervention types with icons
INTERVENTION_TYPES = [
    {"id": "academic_counseling",  "label": "Academic Counseling",  "icon": "🎓", "color": "#f59e0b"},
    {"id": "attendance_warning",   "label": "Attendance Warning",   "icon": "⚠️",  "color": "#ef4444"},
    {"id": "financial_aid",        "label": "Financial Aid",        "icon": "💲", "color": "#22c55e"},
    {"id": "mental_health_support","label": "Mental Health Support","icon": "🧠", "color": "#a855f7"},
    {"id": "peer_tutoring",        "label": "Peer Tutoring",        "icon": "👥", "color": "#3b82f6"},
    {"id": "faculty_meeting",      "label": "Faculty Meeting",      "icon": "📖", "color": "#f97316"},
    {"id": "other",                "label": "Other",                "icon": "❓", "color": "#6b7280"},
]

# In-memory interventions store (list of dicts)
# status: active | pending | resolved
INTERVENTIONS_LIST = [
    {"id": 1,  "student_id": 1,  "type": "attendance_warning",    "description": "Student has missed over 69% of classes. Immediate attendance counseling required.", "advisor": "2vxsx-fae", "created": "Apr 15, 2026", "status": "resolved"},
    {"id": 2,  "student_id": 5,  "type": "academic_counseling",   "description": "GPA has dropped below 1.0. Academic improvement plan initiated.",                  "advisor": "2vxsx-fae", "created": "Apr 15, 2026", "status": "active"},
    {"id": 3,  "student_id": 3,  "type": "mental_health_support", "description": "Student referred to campus counseling center due to extended absences.",            "advisor": "2vxsx-fae", "created": "Apr 15, 2026", "status": "pending"},
    {"id": 4,  "student_id": 2,  "type": "financial_aid",         "description": "Financial hardship identified. Referred to financial aid office.",                  "advisor": "2vxsx-fae", "created": "Apr 14, 2026", "status": "active"},
    {"id": 5,  "student_id": 4,  "type": "peer_tutoring",         "description": "Assigned peer tutor for core subjects. Weekly sessions scheduled.",                 "advisor": "2vxsx-fae", "created": "Apr 14, 2026", "status": "pending"},
    {"id": 6,  "student_id": 6,  "type": "faculty_meeting",       "description": "Faculty meeting scheduled to discuss academic performance and support plan.",        "advisor": "2vxsx-fae", "created": "Apr 13, 2026", "status": "resolved"},
    {"id": 7,  "student_id": 7,  "type": "attendance_warning",    "description": "Attendance below 50%. Warning issued and parent notified.",                         "advisor": "2vxsx-fae", "created": "Apr 13, 2026", "status": "active"},
    {"id": 8,  "student_id": 8,  "type": "academic_counseling",   "description": "Multiple failed courses. Academic plan restructured with reduced load.",            "advisor": "2vxsx-fae", "created": "Apr 12, 2026", "status": "pending"},
    {"id": 9,  "student_id": 9,  "type": "mental_health_support", "description": "Engagement dropped significantly. Peer mentoring assigned.",                        "advisor": "2vxsx-fae", "created": "Apr 12, 2026", "status": "active"},
    {"id": 10, "student_id": 14, "type": "financial_aid",         "description": "Student applied for emergency financial assistance.",                                "advisor": "2vxsx-fae", "created": "Apr 11, 2026", "status": "resolved"},
    {"id": 11, "student_id": 17, "type": "peer_tutoring",         "description": "Peer tutoring sessions initiated for Mathematics and Economics.",                   "advisor": "2vxsx-fae", "created": "Apr 10, 2026", "status": "active"},
    {"id": 12, "student_id": 23, "type": "attendance_warning",    "description": "Attendance critically low. Academic probation warning issued.",                     "advisor": "2vxsx-fae", "created": "Apr 10, 2026", "status": "pending"},
]

_next_id = [13]  # mutable counter for new interventions

def add_intervention(student_id, itype, description):
    iv = {
        "id": _next_id[0],
        "student_id": int(student_id),
        "type": itype,
        "description": description,
        "advisor": "2vxsx-fae",
        "created": "Apr 16, 2026",
        "status": "active",
    }
    INTERVENTIONS_LIST.append(iv)
    _next_id[0] += 1
    return iv

def update_intervention_status(iv_id, status):
    for iv in INTERVENTIONS_LIST:
        if iv["id"] == int(iv_id):
            iv["status"] = status
            return iv
    return None

def get_type_info(type_id):
    return next((t for t in INTERVENTION_TYPES if t["id"] == type_id), INTERVENTION_TYPES[-1])

MAJORS = [
    "Computer Science", "Engineering", "Medicine", "Business Administration",
    "Nursing", "Psychology", "Biology", "Mathematics", "Physics", "Chemistry",
    "History", "Law", "Architecture", "Philosophy", "Education", "Economics",
    "Sociology", "Political Science", "Arts", "Music", "Journalism",
    "Public Health", "Biochemistry", "Statistics", "IT & Networks",
    "Anthropology", "Geography", "Finance", "Linguistics", "Environmental Sci.",
]

_next_student_id = [max(s["id"] for s in STUDENTS) + 1]

def add_student(name, email, age, year, major, gpa, attendance,
                assignments_done, engagement, failed_courses, financial_aid):
    student = {
        "id":               _next_student_id[0],
        "name":             name.strip(),
        "email":            email.strip(),
        "age":              int(age),
        "year":             int(year),
        "major":            major.strip(),
        "gpa":              round(float(gpa), 2),
        "attendance":       int(attendance),
        "assignments_done": int(assignments_done),
        "engagement":       int(engagement),
        "failed_courses":   int(failed_courses),
        "financial_aid":    financial_aid == "true",
    }
    STUDENTS.append(student)
    _next_student_id[0] += 1
    return student
