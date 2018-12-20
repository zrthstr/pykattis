#!/usr/bin/env python3


if __name__ == "__main__":
    for _ in range(int(input())):
        v = list(map(int, input().split()))[:-1]

        imi = 0
        first = v[0]

        for t in v[1:]:
            d = t - first*2
            if d > 0:
                imi += d
            first = t

        print(imi)
