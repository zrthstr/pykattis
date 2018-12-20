#!/usr/bin/env python3


if __name__ == "__main__":
    set_c = 0
    while True:
        set_c +=1
        n = int(input())
        if n == 0:
            exit()
        
        s = []
        print("SET {}".format(set_c))
        for _ in range(n):
            s.append(input())
        a = []
        b = []
        i = 0
        for ss in s:
            if i == 0:
                a.append(ss)
                i = 1
            else:
                b.append(ss)
                i = 0

        for ss in a + b[::-1]:
            print(ss)
