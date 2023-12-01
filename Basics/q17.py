# Given a number N and an array of N elements, find the Bitwise OR of the array elements.
# Input Size : N <= 100000
# Sample Testcase :
# INPUT
# 2
# 2 4
# OUTPUT
# 6



a = int(input())
b = list(map(int,input().split()))
# print(b)
# b = list(filter(lambda x: x != " ", b))
x =0
for i in b:
        x |= i
print(x) 
