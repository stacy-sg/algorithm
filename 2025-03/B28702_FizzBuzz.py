import sys
input = sys.stdin.readline

list1 = []

for i in range(3):
    list1.append(input().strip())

for i in list1:
    if i not in ['Fizz', 'Buzz', 'FizzBuzz']:
        ans = int(i) + 3 - list1.index(i)
        break
print('Fizz'*(ans%3==0) + 'Buzz'*(ans%5==0) or ans)

########두번째 방법###############
#for i in range(3, 0, -1):
#    n = input()
#    if n not in ['Fizz', 'Buzz', 'FizzBuzz']:
#        ans = int(n) + i
#        break
#print('Fizz'*(ans%3==0) + 'Buzz'*(ans%5==0) or ans)