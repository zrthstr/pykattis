#!/usr/bin/env python3

if __name__ == "__main__":
    d, m = list(map(int, input().split()))
    dow = ["Thursday","Friday","Saturday","Sunday","Monday","Tuesday","Wednesday"]
    dim = [31, 28, 31,
           30, 31, 30,
           31, 31 ,30,
           31, 30, 31]
    print(dow[((d + sum(dim[0:m-1])) % 7) -1])
