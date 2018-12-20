#!/usr/bin/env python3

import math

if __name__ == "__main__":
    b, B = list(map(int, input().split()))
    print(math.ceil(b/math.sin(math.radians(B))))
