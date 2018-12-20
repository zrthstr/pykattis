#!/usr/bin/env python3


if __name__ == "__main__":
    a = 0
    for _ in range(int(input())):
        x = input()
        a+= int(x[:-1]) ** int(x[-1])
    print(a)
