#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_args = len(sys.argv)

    if num_args < 2:
        print("{} arguments.".format(num_args - 1))

    elif num_args == 2:
        print("{} argument:".format(num_args - 1))
        print("1: {}".format(sys.argv[1]))

    elif num_args > 2:
        print("{} arguments:".format(num_args - 1))
        for num in range(1, num_args):
            print("{}: {}".format(num, sys.argv[num]))
