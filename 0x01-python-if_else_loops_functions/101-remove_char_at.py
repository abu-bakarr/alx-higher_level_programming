#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return str
    s = ""
    for i in range(0, len(str)):
        if i == n:
            continue
        s += str[i]
    return s
