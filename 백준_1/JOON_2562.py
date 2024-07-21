import sys
sys.stdin = open('Joon.txt','r')

listA = []
while(1):
    try:
        A = int(input())
        listA.append(A)
    except EOFError:
        break
max_value = max(listA)
max_index = listA.index(max_value) + 1
print(max_value)
print(f'{max_index}')




