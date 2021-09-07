#!/usr/bin/python3
i = 122
x = 0
while i >= 97:
    a = i
    if x == 1:
        x = 0
        a -= 32
    else:
        x = 1
    print("{:c}".format(a), end="")
    i -= 1
