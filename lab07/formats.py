import json


def csv_to_records(text):
    if text.strip() == '':
        return []

    lines = text.strip().split('\n')
    names = lines[0].split(',')
    records = []

    for i in range(len(names)):
        names[i] = names[i].strip()

    for line in lines[1:]:
        values = line.split(',')
        record = {}

        for i in range(len(names)):
            record[names[i]] = values[i].strip()

        records.append(record)

    return records


def parse_settings(lines):
    settings = {}
    key = ''

    for line in lines:
        line = line.split('#')[0].strip()

        if line == '':
            continue

        if line.startswith('- '):
            value = line[2:].strip()

            if value.isdigit():
                value = int(value)
            elif value.lower() == 'true' or value.lower() == 'yes':
                value = True
            elif value.lower() == 'false' or value.lower() == 'no':
                value = False
            else:
                try:
                    value = float(value.replace(',', '.'))
                except ValueError:
                    pass

            settings[key].append(value)

        else:
            parts = line.split(':', 1)
            key = parts[0].strip()
            value = parts[1].strip()

            if value == '':
                settings[key] = []
            else:
                if value.isdigit():
                    value = int(value)
                elif value.lower() == 'true' or value.lower() == 'yes':
                    value = True
                elif value.lower() == 'false' or value.lower() == 'no':
                    value = False
                else:
                    try:
                        value = float(value.replace(',', '.'))
                    except ValueError:
                        pass

                settings[key] = value

    return settings


def merge_by_key(rows, extra, key='id'):
    result = []

    for row in rows:
        new_row = row.copy()

        if key in row:
            value = row[key]

            if value in extra:
                for name in extra[value]:
                    if name not in new_row:
                        new_row[name] = extra[value][name]

        result.append(new_row)

    return result


def records_to_json(records):
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)