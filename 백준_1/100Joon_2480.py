import sys
sys.stdin = open('JOON_2.txt','r')

A,B,C = map(int,input().split())
m = 0

if(A==B==C):
    m = 10000+(A*1000)
elif((A==B and A!=C) or (B==C and A!=C) or (A==C and A!=B)):
    if(B==C and A!=C):
        m = 1000+(B*100)
    else:
        m = 1000 + (A * 100)
else:
    m = max(A,B,C)*100

print(m)

