#!/usr/bin/env  python3


if __name__ == "__main__":

    sc = int(input())
    print("{}:".format(sc))

    for f in range(2,sc//2+2):

        if not sc % (2*f-1):
            print("{},{}".format(f,f-1))

        elif sc % (2*f-1) == f:
            print("{},{}".format(f,f-1))

        if not sc % (f):
            print("{},{}".format(f,f))

