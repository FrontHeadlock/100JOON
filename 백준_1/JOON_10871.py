import sys
sys.stdin = open('Joon.txt', 'r')

N,X = map(int,input().split())
list_A = list(map(int,input().split()))

for a in list_A:
    if a<X:
        print(a,end=' ')



