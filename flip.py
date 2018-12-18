#!/usr/bin/env python3


def int_reverse(i):
    return int(i[::-1])

if __name__ == "__main__":

    a, b = map(int_reverse, input().split())

    if a > b:
        print(a)
    else:
        print(b)


