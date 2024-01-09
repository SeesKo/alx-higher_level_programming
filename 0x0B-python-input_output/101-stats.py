#!/usr/bin/python3
"""
Defines a script that reads stdin line
by line and computes metrics.
"""

import signal
import sys


def compute_metrics():
    """Computes and prints metrics based on input lines."""
    total_size = 0
    status_codes = {}

    try:
        for line_number, line in enumerate(sys.stdin, start=1):
            parts = line.split()
            if len(parts) >= 9:
                status_code = parts[-2]
                file_size = int(parts[-1])
                total_size += file_size

                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

            if line_number % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        sys.exit(0)

def print_metrics(total_size, status_codes):
    """Prints the computed metrics."""
    print("File size: {}".format(total_size))

    for code in sorted(status_codes, key=lambda x: int(x)):
        print("{}: {}".format(code, status_codes[code]))

if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda signal, frame: sys.exit(0))

    compute_metrics()
