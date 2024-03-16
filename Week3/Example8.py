sentence = "BME362 Introduction To Python"
# Cümleyi ayir ve kelime kelime ters çevir
reversed_words = ' '.join([word[::-1] for word in sentence.split()])

print(reversed_words)
