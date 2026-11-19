a = float(input('Введите высоту >>> '))
b = float(input('Введите ширину >>> '))

a = abs(a)
b = abs(b)

s = round((a*b), 1)
p = round(((a+b)*2), 1)

print(f'Площадь: {s}')
print(f'Периметр: {p}')