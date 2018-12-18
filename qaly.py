#!/usr/bin/env  python3

res = 0
for r in range(int(input())):
    a, b  = map(float, input().split())
    res += a * b
print(res)

