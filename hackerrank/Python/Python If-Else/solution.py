#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())

    check = {True: 'Not Weird', False: 'Weird'}
    print(check[n % 2 == 0 and n not in range(6, 21)])
