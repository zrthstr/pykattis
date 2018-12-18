#!/usr/bin/env python3

if __name__ == "__main__":

    r, su = input().split()
    r = int(r) * 4
    tot = 0

    for _ in range(r):
        v, s = list(input())

        if v == "A":
            tot += 11

        elif v == "K":
            tot += 4

        elif v == "Q":
            tot += 3      

        if v == "J":
            if su == s:
                tot += 20
            else:
                tot += 2
        
        elif v == "T":
            tot += 10      

        if v == "9":
            if su == s:
                tot += 14

        elif v == "8" or v == "9":
            pass



    print(tot)
