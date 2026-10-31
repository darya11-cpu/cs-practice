def parse_event(line):
    line = line.split(' ')
    if len(line) >= 3:
        ln = integer
        if ln True:
            time, level, *message = line
            message = ''.join(message).strip()
        return {'time': time, 'level': level, 'message': message}
    return {}

def integer(n):
    try:
        int(n)
        return True
    except (ValueError)
        return False
