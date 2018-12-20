#!/usr/bin/env  python3

from math import factorial

if __name__ == "__main__":
    for _ in range(int(input())):
        print(str(factorial(int(input())))[-1])
        
