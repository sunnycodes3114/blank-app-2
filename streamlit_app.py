import streamlit as st

# Function to convert grade to grade points
def grade_to_point(grade):
    """Converts grade to grade points based on a standard scale."""
    grade_points = {
        "O": 10,
        "A+": 9,
        "A": 8,
        "B+": 7,
        "B": 6,
        "P": 5,
        "RA": 0
    }
    return grade_points.get(grade.upper(), 0)

# Data for each tab
data = {
    "AI&DS": [
        {"code": "EN1001", "name": "Communicative English", "credits": 3},
        {"code": "MA1001", "name": "Linear Algebra", "credits": 4},
        {"code": "PH1001T", "name": "Engineering Physics", "credits": 3},
        {"code": "BS1001", "name": "Environmental Science and Engineering", "credits": 2},
        {"code": "CS1001", "name": "Programming in C", "credits": 3},
        {"code": "CS1703", "name": "Digital Design + Lab", "credits": 4},
        {"code": "CS1801", "name": "Programming in C Lab", "credits": 2},
        {"code": "PH1801T", "name": "Physics Lab", "credits": 2},
    ],
    "Cyber": [
        {"code": "EN1001", "name": "Communicative English", "credits": 3},
        {"code": "MA1001", "name": "Linear Algebra", "credits": 4},
        {"code": "CS1001", "name": "Programming in C", "credits": 3},
        {"code": "PH1001T", "name": "Engineering Physics", "credits": 3},
        {"code": "CS1009", "name": "Cyber Security Essentials", "credits": 4},
        {"code": "CS1801", "name": "Programming in C Lab", "credits": 2},
        {"code": "PH1801T", "name": "Physics Lab", "credits": 2},
        {"code": "CS1703", "name": "Digital Design + Lab", "credits": 4},
    ],
    "IoT": [
        {"code": "EN1001", "name": "Communicative English", "credits": 3},
        {"code": "MA1001", "name": "Linear Algebra", "credits": 4},
        {"code": "CS1001", "name": "Programming in C", "credits": 3},
        {"code": "BS1001", "name": "Environmental Science and Engineering", "credits": 2},
        {"code": "CS1005", "name": "Digital Design and Microprocessor", "credits": 3},
        {"code": "CS1007", "name": "Basics of Electrical and Electronics Engineering", "credits": 3},
        {"code": "CS1801", "name": "Programming in C Lab", "credits": 2},
        {"code": "CS1803", "name": "Digital Design and Microprocessor Lab", "credits": 2},
    ],
}

# Page header
st.title("CGPA Calculator")
st.subheader("CGPA Cant be Calculated if RA is a grade")

# Create tabs
tabs = st.tabs(["AI&DS", "Cyber", "IoT"])

for i, (tab_name, courses) in enumerate(data.items()):
    with tabs[i]:
        st.subheader(f"{tab_name} Courses")
        
        # Display courses table without Grade
        st.table([{key: value for key, value in course.items() if key != "grade"} for course in courses])
        
        st.write("### Enter Grades for Each Course")
        for course in courses:
            course["grade"] = st.selectbox(
                f"Grade for {course['code']} - {course['name']}",
                options=["O", "A+", "A", "B+", "B", "P", "RA"],
                key=f"{tab_name}_{course['code']}"
            )

        # Calculate CGPA
        weighted_sum = 0
        credit_sum = 0
        for course in courses:
            grade_point = grade_to_point(course["grade"])
            weighted_sum += grade_point * course["credits"]
            credit_sum += course["credits"]

        cgpa = weighted_sum / credit_sum if credit_sum > 0 else 0

        # Display CGPA for the tab
        st.write("### CGPA Results")
        st.write(f"Your CGPA for {tab_name} is: **{cgpa:.2f}**")
