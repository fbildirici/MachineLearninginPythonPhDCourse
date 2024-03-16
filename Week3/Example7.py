numaralar = ['12290383', '11290263', '13290193', '14290211', '15290055', '10290403', '13290356']

# Lambda fonksiyonu ve filtre kullanarak 2013 kabüllüleri listeleyelim
admitted_2013 = list(filter(lambda num: num.startswith('13'), numaralar))

print(admitted_2013)