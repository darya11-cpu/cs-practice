def parse_record(line: str) -> dict:
    clean_line = line.strip()
    
    if not clean_line:
        return {}
    
    parts = clean_line.split(",")
    
    return {
        "city": int(parts[0].strip()),       # Приведение к числу, если нужно
        "name": parts[1].strip(),
        "role": parts[2].strip()
    }