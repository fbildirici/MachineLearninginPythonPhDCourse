# Numara ve enstitu durumundan listeler tanimlayalim
students = set([14520, 11347, 12699, 12337, 11450, 15147, 12547, 13341])
Ascholar = set([11450, 15147, 12547])
Bscholar = set([12337, 11450, 12547, 13341])

# Bursu olmayanlari cikaralim
no_scholarship = students - (Ascholar.union(Bscholar))

# Sonucu yazdiralim
print(no_scholarship)
