#!/usr/bin/env python3

import sys

def const(i):
    return [int(i),set()]


def solve(line):
    a = list(map(const, line.split()))[::-1]
    for i in range(len(a)):
        a[i][1] = set([len(a)-i-1])
        try:
            mini = sorted([aa for aa in a[:i] if aa[0] > a[i][0]], key=lambda x:len(x[1]))[-1][1]
        except:
            mini = set()

        a[i][1] = mini | a[i][1]

    a = [sorted(m) for n,m in a ][::-1]
    aa = max(a, key=len)
    return len(aa), aa


source = map(str.rstrip, sys.stdin)

for c in source:
    line = source.__next__()
    print("line:", line)
    c, solution = solve(line)
    print(f"{c}\n{solution}")
