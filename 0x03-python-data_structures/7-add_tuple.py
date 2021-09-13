#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list1 = list(tuple_a) + [0] * 2
    list2 = list(tuple_b) + [0] * 2
    res = [a + b for a, b in zip(list1, list2)]
    return tuple(res[:2])
