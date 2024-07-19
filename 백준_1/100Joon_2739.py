import sys
sys.stdin = open('JOON_4.txt','r')
A = int(input())
for i in range(1,10):
    print(A,'*',i,'=',A*i)
    #print(f'{A}*{i}={A*i})