words = "BME362 Introduction To Python".split()  # Cümleyi bölelim kelimelerde
letter_counts = list(map(lambda word: len(word), words))  # Kelime basina karakter sayisini uzunlugu hesaplayalim

print(letter_counts)