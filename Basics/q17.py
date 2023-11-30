# Given a number N and an array of N elements, find the Bitwise OR of the array elements.
# Input Size : N <= 100000
# Sample Testcase :
# INPUT
# 2
# 2 4
# OUTPUT
# 6



a = int(input())
b = list(input())
print(b)
for i in range(0,a):
    if b[i] == " ":
        b.pop(i)
        

print(b)
# x = 0
# for i in range(0,a):
#     x += int(b[i])
# print(x)