import sys
sys.stdin = open('JOON_3.txt','r')

H,M=map(int,input().split())

if M < 45 :             # M이 45보다 작을 때
    if H == 0 :         # H는 0일때
        H = 23
        M += 60
    else :
        H -= 1          #H=H-1
        M += 60         #M=M+60
print(H,M-45)












'''
C와 M을 계산
만약 newMin이 60이상이라면



'''