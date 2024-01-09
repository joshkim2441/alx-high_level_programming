#!/usr/bin/python3
"""Define script that reads stdin line by line and computes metrics"""
if __name__ == "__main__":
    import sys

    total_size = 0
    status_codes = {200: 0, 301: 0, 401: 0, 400: 0, \
            403: 0, 404: 0, 405: 0, 500: 0}
    lines_processed = 0

    try:
        for line in sys.stdin:
            try:
                ip, _, date, _, status_code, file_size = line.split()
                status_code = int(status_code)
                file_size = int(file_size)

                total_size += file_size
                status_codes[status_code] += 1

                lines_processed += 1
                if lines_processed % 10 == 0:
                    print_statistics(total_size, status_codes)
            except ValueError:
                pass  # Ignore invalid lines
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)

    def print_statistics(total_size, status_codes):
        print("File size:", total_size)
        print("Status codes:")
        for code in sorted(status_codes):
            if status_codes[code] > 0:
                print(f"  {code}: {status_codes[code]}")
