#!/usr/bin/env python3

if __name__ == "__main__":

    avail = int(input())
    month = int(input())

    vals = [int(input()) for _ in range(month)]
    res = (month +1) * avail - sum(vals)

    print(res)
