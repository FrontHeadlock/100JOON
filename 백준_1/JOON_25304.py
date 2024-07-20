import sys
sys.stdin = open("input_1.txt","r")

X=int(input())
N=int(input())
totalPrice = 0

for i in range(N):
    a,b = map(int,input().split())
    totalPrice += (a*b)

if X == totalPrice:
    print("Yes")
else:
    print("No")


