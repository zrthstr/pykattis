#!/usr/bin/env python3

import sys

if __name__ == "__main__":

    for i in sys.stdin:
        if int(i) % 2:
            print('Alice')
        else:
            print('Bob')

