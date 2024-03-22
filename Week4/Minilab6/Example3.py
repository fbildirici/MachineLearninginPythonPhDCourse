# two list names and nums
names = ["Ali Mert", "Can Demir", "Mehmet Birlik", "Fatma Dikmen", "Ali Demir"]
student_ids = [1214, 1425, 4718, 6547, 1475]

# loops for names ids
for name, student_id in zip(names, student_ids):
    # Check name starts with 'Ali'
    if name.split()[0] == "Ali":
        # Print 
        print(f"Name: {name}, Student ID: {student_id}")
