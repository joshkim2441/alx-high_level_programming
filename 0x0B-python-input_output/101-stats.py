#!/usr/bin/python3

import signal
import sys


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


status_codes = {"200": 0, "301": 0, "400": 0,
                "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        data = line.split(" ")
        if len(data) > 2:
            status_code = data[-2]
            file_size = int(data[-1])
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += file_size
            line_count += 1
            if line_count % 10 == 0:
                print_stats()
except KeyboardInterrupt:
    pass
finally:
    print_stats()
