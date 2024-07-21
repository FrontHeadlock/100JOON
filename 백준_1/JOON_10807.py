import sys
sys.stdin = open('Joon.txt', 'r')

N = int(input())
listA = list(map(int,input().split()))
v = int(input())
print(listA.count(v))






