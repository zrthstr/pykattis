#!/usr/bin/env python3


def dsum(i):
    """ digit sum"""
    return sum([int(ii) for ii in str(i)])
        

def mmds(start, stop):
    """ min or max digits sum"""
    if start > stop:
        step = -1
    else:
        step = 1

    for nn in range(start, stop+1, step):
        if dsum(nn) == x:
            return nn


if __name__ == "__main__":
    l, d, x = [int(input()) for _ in range(3)]

    n = mmds(l, d)
    m = mmds(d, l)
    
    print(n,m, sep="\n")
