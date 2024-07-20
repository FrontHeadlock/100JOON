import sys
sys.stdin = open("../input_1.txt", "r")

A = int(input())

for i in range(0,A+1,1):
    try:
        X,Y=map(int,input().split())
        print(f'{X+Y}')
    except EOFError:
        break;