#!/usr/bin/env python3


if __name__ == "__main__":


    h, m = input().split(" ")

    if h == "00":
        h = 0
    else:
        h = int(h)

    if m == "00":
        m = 0
    else:
        m = int(m)



    mm = h * 60 + m - 45

    if mm < 0:
        h = 23
        m = 60 + mm
    else:
        if mm >= 60 * 24:
            mm = mm - (60 * 24)
            h -=1

        h = (mm // 60)
        mm -= (h * 60)
        m = mm

    print("{} {}".format(h,m))
            

