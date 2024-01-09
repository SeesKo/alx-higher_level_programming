#!/usr/bin/python3
"""
Defines a script that reads stdin line
by line and computes metrics.
"""

import sys
from collections import defaultdict


def compute_metrics():
    """Computes and prints metrics based on input lines."""
    total_size = 0
    status_counts = defaultdict(int)

    try:
        for i, line in enumerate(sys.stdin, start=1):
            parts = line.split()

            if len(parts) >= 9:
                status_code = parts[-2]
                file_size = int(parts[-1])
                total_size += file_size
                status_counts[status_code] += 1

            if i % 10 == 0:
                print(f"File size: {total_size}")

                for code in sorted(status_counts, key=int):
                    print(f"{code}: {status_counts[code]}")

    except KeyboardInterrupt:
        pass

    print(f"File size: {total_size}")
    for code in sorted(status_counts, key=int):
        print(f"{code}: {status_counts[code]}")


if __name__ == "__main__":
    compute_metrics()
