def parse_record(line):
    line = line.strip(';')
    
    if len(line) != 3:
        raise ValueError('Полей не ровно 3')
    else:
        city, temp_str, date = line
    if not city.strip() or not date.strip():
        raise ValueError('Данные для города или даты отсутствуют')
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError('Температура не является числом')
    
    return {
        "city": city,
        "temp": temp,
        "date": date
    }=]