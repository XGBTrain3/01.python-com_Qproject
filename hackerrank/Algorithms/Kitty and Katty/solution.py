#!/bin/python3


def winner(n):
    return 'Kitty' if n == 1 or n % 2 == 0 else 'Katty'


if __name__ == '__main__':
    T = int(input())

    for T_itr in range(T):
        n = int(input())
        print(winner(n))
