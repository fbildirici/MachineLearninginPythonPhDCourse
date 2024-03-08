# Dosyayi olusturalim elle
file_path = 'matrix.txt'  # Kodun çalıştığı dizine aldik

# Dosyayı okuyup diagonal elemanlari basalim
with open(file_path, 'r') as file:
    matrix = [list(map(int, row.split())) for row in file]

# islemi yapalim
diagonal_elements = [matrix[i][i] for i in range(len(matrix))]

# Sonuc
print(diagonal_elements)
