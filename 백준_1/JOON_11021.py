import sys
sys.stdin = open('../input_1.txt', 'r')

T = int(input())
for i in range(T):
    A,B=map(int,input().split())
    print(f'Case #{i+1}: {A+B}')








