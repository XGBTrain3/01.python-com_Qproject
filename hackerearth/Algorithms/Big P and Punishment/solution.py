"""
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
"""

# Write your code here
from collections import defaultdict


def calc(p, adjacency, totals, seen):
    if p not in seen:
        seen.add(p)
        totals.add(p)
        friends = adjacency[p]
        for i in friends:
            calc(i, adjacency, totals, seen)


t = int(input())
for _ in range(t):
    n, f, s = map(int, input().strip().split())
    friendships = defaultdict(list)
    for _ in range(f):
        a, b = map(int, input().strip().split())
        friendships[a].append(b)
    sit = set()
    visited = set()
    for _ in range(s):
        x = int(input())
        calc(x, friendships, sit, visited)
    print(len(sit))
