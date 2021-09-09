#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    argl = len(argv)
    sum = 0

    if argl > 1:
        for i in range(argl):
            if i > 0:
                sum = sum + int(argv[i])
    print("{:d}".format(sum))
