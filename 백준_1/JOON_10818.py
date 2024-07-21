import sys
sys.stdin = open('Joon.txt','r')

N = int(input())
listA=list(map(int,input().split()))

max_val = listA[0]
min_val = listA[0]

for num in listA:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
print(min_val, max_val)
