# "students.txt" dosyasını okuyup "surnames.txt" dosyasina soyadlarini basalim
with open('students.txt', 'r') as infile:
    with open('surnames.txt', 'w') as outfile:
        for line in infile:
            if line.strip():
                parts = line.strip().split()
                name = parts[0]
                surname = ' '.join(parts[1:])
                outfile.write(surname + '\n')

print("Soyadları başarıyla 'surnames.txt' dosyasına yazıldı.")
