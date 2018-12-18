#!/usr/bin/env python3

if __name__ == "__main__":

    name = input()
    nn = ["-"]
    for n in name:
        if not nn[-1] == n:
            nn.append(n)

    print("".join(nn[1:]))
