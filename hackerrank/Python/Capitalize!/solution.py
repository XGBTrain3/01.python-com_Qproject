#!/bin/python3

import os


# Complete the solve function below.
def solve(s):
    import string
    return string.capwords(s, ' ')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
