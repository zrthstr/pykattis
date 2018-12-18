#!/usr/bin/env python3

import math

    


if __name__ == "__main__":

    N, X, Y = list(map(int, input().split(" ")))
    mat = [ int(input()) for _ in range(N) ]

    d = math.sqrt( X**2 + Y**2 )


    for m in mat:
        if m > d:
            print("NE")
        else:
            print("DA")


    
