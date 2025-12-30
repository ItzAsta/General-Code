# Attendance Tracker

# Function to load student names from a CSV file
def load_students(filename):
    students = []
    with open(filename, "r") as file:
        for line in file:
            students.append(line.strip())
    return students

# Function to mark attendance
def mark_attendance(students):
    attendance = {}
    for student in students:
        present = input(f"Is {student} present? (y/n): ").lower()
        if present == "y":
            attendance[student] = "Present"
        else:
            attendance[student] = "Absent"
    return attendance

# Function to save attendance to TXT file
def save_attendance(attendance, filename):
    with open(filename, "w") as file:
        for student, status in attendance.items():
            file.write(f"{student}: {status}\n")

# Main program
def main():
    students = load_students("students.csv")
    attendance = mark_attendance(students)
    save_attendance(attendance, "attendance.txt")
    print("\nAttendance saved!")

if __name__ == "__main__":
    main()
