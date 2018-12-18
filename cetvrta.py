#!/usr/bin/env python3

from collections import Counter

if __name__ == "__main__":

    x = []
    y = []
    for _ in range(3):
        xx, yy = list(map(int, input().split()))
        x.append(xx)
        y.append(yy)

    xc = Counter(x).most_common(2)[1][0]
    yc = Counter(y).most_common(2)[1][0]


    print(xc, yc)
