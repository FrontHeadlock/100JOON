import sys
sys.stdin = open('../1차원배열/Joon.txt', 'r')

T = int(input())

for x in range(1,T+1):
    a,b = map(int,input().split())
    print(f'Case #{x}: {a}+{b}={a+b}')



