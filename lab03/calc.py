a, op, b = map(str.strip, input('Введите числа >>>').split(' '))
a, b = map(int, (a, b))

if op == '+':
    print(a + b)
if op == '-':
    print(a - b)
if op == '*':
    print(a * b)
if op == '/':
    print(a / b)