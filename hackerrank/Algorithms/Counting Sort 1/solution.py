#!/bin/python3

import os


# Complete the countingSort function below.
def countingSort(arr):
    count = [0] * 100
    for i in arr:
        count[i] += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
