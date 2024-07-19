import sys
sys.stdin = open('JOON_1.txt', 'r')

H,M = map(int,input().split())
C = int(input())
K=M+C

if K>=60:
    M1=K%60
    H1=(K//60)
    newHr = (H+H1)%24
    print(newHr, M1)
else:
    print(H, K)
