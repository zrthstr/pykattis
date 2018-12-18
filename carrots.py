#!/usr/bin/env python3

import sys

spell = "{} Abracadabra"

if __name__ == "__main__":

    for i in sys.stdin:
        b = int(i.split()[1])
        print(b)
        sys.exit()
