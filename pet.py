#!/usr/bin/env  python3


if __name__ == "__main__":
    winner = 0
    best = 0

    for r in range(1,5+1):
        this = sum(list(map(int, input().split())))
        if this > best:
            best = this
            winner = r

    print("{} {}".format(winner, best)) 
