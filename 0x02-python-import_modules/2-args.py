#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    argl = len(argv)
    j = 1

    if argl == 1:
        print("{:d} {:s}.".format(0, "arguments"))
    else:
        print("{:d} {:s}:"
              .format(argl - 1, "arguments" if argl > 2 else "argument"))
        for i in range(argl):
            if i > 0:
                print("{:d}: {:s}".format(i, argv[i]))
