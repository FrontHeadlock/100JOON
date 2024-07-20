import sys
sys.stdin = open('../1차원배열/Joon.txt', 'r')

while(1):
        A,B = map(int,input().split())
        if A==0 and B==0:
            break
        print(f'{A+B}')
