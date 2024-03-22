# Student records [StudentID, GPA]
student_records = [[14578, 2.4], [14587, 3.6], [14554, 3.1], [14591, 2.6], [14584, 2.9]]

# Sort GPA
sorted_records = sorted(student_records, key=lambda x: x[1])

# Print
for record in sorted_records:
    print(f"Student ID: {record[0]}, GPA: {record[1]}")
