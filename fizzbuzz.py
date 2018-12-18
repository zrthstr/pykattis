#!/usr/bin/env python3

if __name__ == "__main__":

    a, b, n = list(map(int, input().split()))
    for i in range(1, n+1):
        if not i % a and not i % b:
            print("FizzBuzz")
        elif not i % a:
            print("Fizz")
        elif not i % b:
            print("Buzz")
        else:
            print(i)
