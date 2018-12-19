#!/usr/bin/env python3


if __name__ == "__main__":
    n = input()
    print(len(list(filter(lambda x: x < 0, map(int, input().split())))))

