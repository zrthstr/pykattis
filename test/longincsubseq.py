#!/usr/bin/env python3

import sys

def const(i):
    return [int(i),set()]


def solve(line):
    a = list(map(const, line.split()))[::-1]

    for i in range(len(a)): # make sure this dosent include itself
        a[i][1] = set([len(a)-i-1])
        try:
            print(f"looking for mini for {a[i]} in :",a[:i] )
            mini = min(aa for aa in a[:i] if aa[0] > a[i][0])
        except:
            mini = [-1000,set()]

        print("mini", mini)
        print(mini[1] | a[i][1])
        a[i][1] = mini[1] | a[i][1]


    print(a[::-1])
    #a = [sorted(m) for n,m in a ][::-1]
    #aa = max(a, key=len)
    #result = len(aa), aa
    result = a[::-1]
    return len(a), result


source = map(str.rstrip, sys.stdin)
#for line in map(str.rstrip, sys.stdin):
for c in source:
    line = source.__next__()
    print()
    print("line:", line)
    c, solution = solve(line)
    print(f"{c}\n{solution}")
