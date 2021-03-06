#!/bin/python3

import os


# Complete the pokerNim function below.
def pokerNim(k, c):
    import functools
    import operator

    return 'First' if functools.reduce(operator.xor, c) else 'Second'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        c = list(map(int, input().rstrip().split()))

        result = pokerNim(k, c)

        fptr.write(result + '\n')

    fptr.close()
