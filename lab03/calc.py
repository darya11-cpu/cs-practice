a, op, b = map(str.strip, input('Введите числа >>> ').split())
a, b = map(int, (a, b))

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b == 0:
        print('Нельзя делить на 0')
    else:
        print(a / b)
else:
    print('Неизвестный оператор')

