#!/usr/bin/env python3


if __name__ == "__main__":

    i = input()
    p = "PER" * (len(i) // 3)
    days = 0
    for a, b in zip(i, p):
        if not a == b:
            days += 1


    print(days)
