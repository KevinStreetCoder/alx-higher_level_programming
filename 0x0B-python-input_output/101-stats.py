#!/usr/bin/python3
"""
    101-stats: Stats from stdin
"""

import sys

def print_metrics(file_size, status_codes):
    """
        Print the computed metrics
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def parse_input(line):
    """
        Parse each line of input
    """
    parts = line.split()
    if len(parts) >= 2:
        status_code = parts[-2]
        file_size = parts[-1]
        if status_code.isdigit() and file_size.isdigit():
            return int(file_size), status_code
    return 0, None

def main():
    """
        Main function
    """
    count = 0
    file_size = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            count += 1
            file_size_increment, status_code = parse_input(line)
            file_size += file_size_increment
            if status_code:
                status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if count % 10 == 0:
                print_metrics(file_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(file_size, status_codes)
        raise

    print_metrics(file_size, status_codes)


if __name__ == "__main__":
    main()
