import sys
sys.stdin = open('../input_1.txt', 'r')

sum=0;
A = int(input())
for i in range(A+1):
    sum+=i
print(sum)