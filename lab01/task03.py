price = float(input('Введите цену тетради >>> '))
cnt = int(input('Введите количество тетрадей >>> '))

price = abs(price)
cnt = abs(cnt)

res = (price*cnt)

print(f'Общая стоимость: {res:.2f}')