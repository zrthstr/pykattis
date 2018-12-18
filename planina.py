#!/usr/bin/env python3

if __name__ == "__main__":

    i = int(input())

    sides = 2
 
    for _ in range(i):
        sides = sides + sides - 1


    print(sides ** 2)    
