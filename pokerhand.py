#!/usr/bin/env python3

from collections import Counter

    

def foo(x):
    return x[0]

if __name__ == "__main__":

    hand = ''.join(list(map(foo, input().split(" "))))
    c = Counter(hand).most_common(1)[0][1]
    print(c)

    
