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
    }

def read_valid(lines):
    valid_records = []
    for line in lines:
        if not line:
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue
    return valid_records

def average_by_city(records):
    totals = {}
    counts = {}
    for r in records:
        city = r['city']
        totals[city] = totals.get(city, 0.0) + r['temp']
        counts['city'] = counts.get(city, 0) + 1
    averages = {}
    for city in totals:
        averages[city] = rount(totals[city] / counts[city], 1)
    return averages