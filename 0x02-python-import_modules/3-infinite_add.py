#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0

    for num in range(1, len(sys.argv)):
        number = int(sys.argv[num])
        sum += number

    print(f"{sum}")
