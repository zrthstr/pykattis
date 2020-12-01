#!/usr/bin/env python3

import sys

def const(i):
    return [int(i),1]

def solve(line):
    a = list(map(const, line.split()))
    a = a[::-1]

    if len(a) == 1: ## #let see if we can get rid of this later
        return 1, 1

    for i, (value, score) in enumerate(a):
        if i == 0: # last allways has a value of 1 #lets see if we can get rid of this later
            continue

        for pi, (pvalue, pscore) in enumerate(a[:i]):
            if value >= pvalue:
                continue
            if score <= pscore:
                a[i][1] = pscore +1


    a = a[::-1]

    print(a)

    #result = [e[1] for e in a][::-1]
    #result = [e[1] for e in a]

    return len(a),a


source = map(str.rstrip, sys.stdin)
#for line in map(str.rstrip, sys.stdin):
for c in source:
    line = source.__next__()
    print()
    #print("line:", line)
    c, solution = solve(line)
    #print(c, solution)
