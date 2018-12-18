#!/usr/bin/env python3

if __name__ == "__main__":

    _ = input()
    a = list(filter( lambda x: x > -1, list(map(int, input().split()))))

    print(sum(a) / len(a))
