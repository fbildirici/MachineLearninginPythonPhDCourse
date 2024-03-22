# student names list
names = ["Ali Mert", "Can Demir", "Mehmet Birlik", "Fatma Dikmen", "Ali Demir"]

# index
for index, name in enumerate(names, start=1):
    # names starts with ali
    if name.split()[0] == "Ali":
        # Print
        print(f"Name: {name}, Order Number: {index}")
