#!/bin/python3

import os
import re


# Complete the hackerrankInString function below.
def hackerrankInString(s):
    return 'YES' if re.search(r'.*?'.join(list('hackerrank')), s) else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
