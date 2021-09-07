#!/usr/bin/python3
def uppercase(str):
    s = ""
    for i in str:
        x = ord(i)
        if ord('a') <= x <= ord('z'):
            s += chr(x - 32)
        else:
            s += i
    print("{:s}".format(s))
