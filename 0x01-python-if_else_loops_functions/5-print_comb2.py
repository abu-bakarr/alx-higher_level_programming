#!/usr/bin/python3
for a in range(0, 100):
    if a == 99:
        print("{:d}".format(a))
    else:
        print("{:0>2d}".format(a), end=", ")
