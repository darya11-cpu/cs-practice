import sys
from stats import average_by_city, read_valid, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    valid_records = read_valid(lines)

    non_empty_lines = [line for line in lines if line]
    errors_count = len(non_empty_lines) - len(valid_records)

    best_city = warmest_city(valid_records)

    if best_city:
        averages = average_by_city(valid_records)
        best_average = averages[best_city]

    else:
        best_average = 0.0 

    print(len(valid_records))
    print(errors_count)
    print(f'(best_average:.1f)')

if __name__ == '__main__':
    main()