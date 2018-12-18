#!/usr/bin/env python3

from operator import eq

if __name__ == "__main__":

    n = int(input())
    for _ in range(n):
        a = input()
        b = input()
        res = []
        for aa, bb in zip(a, b):
            if aa == bb:
                res.append(".")
            else:
                res.append("*")
        
        print(a)
        print(b)
        print("".join(res))
        print()
