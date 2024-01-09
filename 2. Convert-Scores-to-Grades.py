# Convert Scores to Grades
student_scores = {
    "abcdef" : 98,
    "ijk": 89,
    "lemon": 75,
    "123": 94,
    "abc": 20,
    "xyz": 40,
    "phone": 83,
}
student_grades = {}
for st_scores in student_scores:
    scores = student_scores[st_scores]

    if scores > 90 and scores <= 100:
        student_grades[st_scores] = "Outstanding"
    elif scores > 80:
        student_grades[st_scores] = "exceeds expectation"
    elif scores > 70:
        student_grades[st_scores] = "acceptable"
    elif scores < 70:
        student_grades[st_scores] = "Fail"

print(student_grades)




# Output:
{'abcdef': 'Outstanding', 'ijk': 'exceeds expectation', 'lemon': 'acceptable', '123': 'Outstanding', 'abc': 'Fail', 'xyz': 'Fail', 'phone': 'exceeds expectation'}
