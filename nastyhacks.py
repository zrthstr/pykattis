#!/usr/bin/env python3

if __name__ == "__main__":

    for _ in range(int(input())):
        r, e, c = list(map(int, input().split()))
        if r > e - c:
            print("do not advertise")
        elif r < e - c:
            print("advertise")
        else:
            print("does not matter")

