#!/usr/bin/env python3


if __name__ == "__main__":

    while True:
        i = int(input())
        if i == -1:
            break
        d = 0
        tot = 0

        for ii in range(i):
            s, t = list(map(int, input().split()))
            t = t-d
            d+=t
            tot += t * s

        print("{} miles".format(tot))
