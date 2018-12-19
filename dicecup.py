#!/usr/bin/env python3

from collections import Counter

if __name__ == "__main__":

    a,b = list(map(int, input().split()))

    ra = list(range(1,a+1))
    rb = list(range(1,b+1))

    pos = [f+s for f in ra for s in rb]

    c = Counter(pos)
    max_occ = c.most_common(1)[0][1]

    out = sorted([k for k, v in c.items() if v == max_occ ])

    for o in out:
        print(o)
     
