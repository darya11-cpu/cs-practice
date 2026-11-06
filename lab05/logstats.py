def parse_event(line):
    line = line.strip().split(' ', 2)

    if len(line) == 3:
        time, level, message = line

        if level == 'DEBUG' or level == 'INFO' or level == 'WARNING' or level == 'ERROR':
            return {'time': time, 'level': level, 'message': message}

    raise ValueError


def count_levels(lines):
    counts = {
        'BROKEN': 0,
        'DEBUG': 0,
        'INFO': 0,
        'WARNING': 0,
        'ERROR': 0
    }

    for line in lines:
        if line.strip() != '':
            try:
                event = parse_event(line)
                level = event['level']
                counts[level] += 1

            except ValueError:
                counts['BROKEN'] += 1

    return counts


def top_errors(lines, n):
    errors = {}

    for line in lines:
        if line.strip() != '':
            try:
                event = parse_event(line)

                if event['level'] == 'ERROR':
                    message = event['message']

                    if message in errors:
                        errors[message] += 1
                    else:
                        errors[message] = 1

            except ValueError:
                continue

    result = []

    for message in errors:
        result.append([message, errors[message]])

    result.sort(key=lambda x: (-x[1], x[0]))

    return result[:n]


def format_report(counts, errors):
    report = 'Отчёт по журналу\n\n'

    for level in sorted(counts):
        report += level + ': ' + str(counts[level]) + '\n'

    report += '\nЧастые ошибки:\n'

    for error in errors:
        report += '- ' + error[0] + ' — ' + str(error[1]) + '\n'

    return report