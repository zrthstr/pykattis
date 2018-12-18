#!/usr/bin/env python3


if __name__ == "__main__":

    should = [1, 1, 2, 2, 2, 8]
    found = list(map(int, input().split()))
    out = [ a-b for a,b in zip(should, found)]

    print(" ".join(map(str, out)))

