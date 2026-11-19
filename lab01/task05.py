time = int(input('Введите продолжительность в секундах >>> '))
if time >= 0:
    hour = time // 3600
    minute = (time % 3600) // 60
    sec = time % 60
    
    
    print(f'{hour}')
    print(f'{minute}')
    print(f'{sec}')