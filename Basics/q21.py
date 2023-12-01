# Given a number N and an array of N elements ,find the Bitwise AND of the array elements.
# Input Size N <= 100000
# Sample Testcase :
# INPUT
# 4
# 4 3 2 1
# OUTPUT
# 0

a = int(input())
b = list(map(int,input().split()))
# print(b)
# b = list(filter(lambda x: x != " ", b))
x = b[0]
for i in b:
        x &= i
print(x)