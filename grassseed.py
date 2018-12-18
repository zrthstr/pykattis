#!/usr/bin/env python3

if __name__ == "__main__":


    cps = float(input())
    abs_l = 0
    for _ in range(int(input())):
        x, y = list(map(float, input().split()))
        abs_l += x * y

    print("{}".format(abs_l * cps))
