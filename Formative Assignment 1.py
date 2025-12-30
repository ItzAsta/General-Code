students = ["Alice", "Jorge", "Sam", "Emilio", "Carmen", "Marco", "Juliet"]


grades = [
    [85, 78, 92],   # Alice
    [72, 70, 68],   # Jorge
    [67, 64, 61],   # Sam
    [90, 88, 94],   # Emilio
    [58, 52, 55],   # Carmen
    [33, 39, 28],   # Marco
    [74, 79, 71]    # Juliet
]



def get_letter_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    elif mark >= 40:
        return "E"
    else:
        return "F"



all_marks = [m for sublist in grades for m in sublist]



highest_mark = max(all_marks)
lowest_mark = min(all_marks)
mark_range = highest_mark - lowest_mark


highest_student = students[
    [i for i, sub in enumerate(grades) if highest_mark in sub][0]
]

lowest_student = students[
    [i for i, sub in enumerate(grades) if lowest_mark in sub][0]
]



grade_counts = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0}

for mark in all_marks:
    grade_counts[get_letter_grade(mark)] += 1



averages = []
for s_grades in grades:
    averages.append(sum(s_grades) / len(s_grades))



print("------ FULL CLASS STATISTICS ------\n")


print("1. ALL STUDENT MARKS:\n")
for i in range(len(students)):
    print(f"{students[i]}: {grades[i]}  | Average: {averages[i]:.2f}%")

print("\n----------------------------------")


print("2. HIGHEST MARK:")
print(f"Student: {highest_student}")
print(f"Raw Mark: {highest_mark}")
print(f"Percentage: {highest_mark}%\n")


print("3. LOWEST MARK:")
print(f"Student: {lowest_student}")
print(f"Raw Mark: {lowest_mark}")
print(f"Percentage: {lowest_mark}%\n")


print("4. RANGE OF MARKS:")
print(f"Range (raw): {mark_range}")
print(f"Range (%): {mark_range}%\n")


print("5. GRADE DISTRIBUTION:")
for grade in ["A", "B", "C", "D", "E", "F"]:
    print(f"{grade}: {grade_counts[grade]}")