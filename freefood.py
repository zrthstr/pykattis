#!/usr/bin/env python3

if __name__ == "__main__":


    a = set()
    for _ in range(int(input())):
        f, t = list(map(int, input().split()))
        for r in range(f, t+1):
            a.add(r)

    print(len(a))
