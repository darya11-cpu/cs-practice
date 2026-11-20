import json

def csv_to_records(text):
    lines = text.strip().split('\n')
    names = lines[0].split(',')
    records = []

    for line in lines[1:]:
        values = line.split(',')
        record = {}

        for i in range(len(names)):
            record[names[i]] = values[i]

        records.append(record)

    return records

def parse_settings(lines):
    settings = {}
    key = ''
    values = []

    for line in lines:
        line = line.split('#')[0].strip()

        if line == '':
            continue

        if line.startswith('- '):
            values.append(line[2:])
            settings[key] = values
        else:
            parts = line.split(':', 1)
            key = parts[0].strip()
            value = parts[1].strip()

            if value == '':
                values = []
                settings[key] = values
            else:
                if value == 'true' or value == 'yes':
                    value = True
                elif value == 'false' or value == 'no':
                    value = False
                elif '.' in value:
                    value = float(value)
                elif value.isdigit():
                    value = int(value)

                settings[key] = value

    return settings

def merge_by_key(rows, extra, key='id'):
    result = []

    for row in rows:
        new_row = row.copy()
        value = row[key]

        if value in extra:
            for name in extra[value]:
                if name not in new_row:
                    new_row[name] = extra[value][name]

        result.append(new_row)

    return result

def records_to_json(records):
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)