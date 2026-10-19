
students = {
    "Student 1": 95,
    "Student 2": 87,
    "Student 3": 78,
    "Student 4": 72,
    "Student 5": 65
}

total = 0
passed = 0
failed = 0

print("========================================")
print("       STUDENT SCORE ANALYZER")
print("========================================")

print("\nStudent Scores and Results:")

for student, score in students.items():

    if score >= 90:
        interpretation = "Excellent"
    elif score >= 80:
        interpretation = "Very Good"
    elif score >= 75:
        interpretation = "Good"
    else:
        interpretation = "Failed"

    if score >= 75:
        result = "Passed"
        passed += 1
    else:
        result = "Failed"
        failed += 1

    total += score

    print(f"{student}: {score} - {interpretation} - {result}")

average = total / len(students)

print("\n========================================")
print("              SUMMARY")
print("========================================")
print(f"Total Score: {total}")
print(f"Average Score: {average:.2f}")
print(f"Highest Score: {max(students.values())}")
print(f"Lowest Score: {min(students.values())}")
print(f"Number of Students Passed: {passed}")
print(f"Number of Students Failed: {failed}")
print("========================================")