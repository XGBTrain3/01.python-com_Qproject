#!/bin/python3

import os


# Complete the factorial function below.
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
