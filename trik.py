#!/usr/bin/env python3

## while simpler solutions do exist,
## none of them are faster when evaluated by katis,
## and most of them are less comprehensive



def a(cups):
    return [cups[1], cups[0], cups[2]]

def b(cups):
    return [cups[0], cups[2], cups[1]]

def c(cups):
    return [cups[2], cups[1], cups[0]]



if __name__ == "__main__":

    movements = input().strip()
    cups = [1, 0, 0]

    for m in movements:
        if m == "A":
            cups = a(cups)
        elif m == "B":
            cups = b(cups)
        else:
            cups = c(cups)

    print(cups.index(1)+1) 
