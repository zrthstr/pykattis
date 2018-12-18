#!/usr/bin/env python3

if __name__ == "__main__":


    for _ in range(int(input())):
        citys = set()
        for _ in range(int(input())):
            citys.add(input())
        print(len(citys))

