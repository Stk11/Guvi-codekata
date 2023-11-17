# Given 3 numbers A,B,C print 'yes' if they can form the sides of a scalene triangle else print 'no'.
# Input Size : A,B,C <= 100000
# Sample Testcase :
# INPUT
# 3 4 5
# OUTPUT
# yes

a,b,c = map(int,input().split())
if a!=b & b!=c & a!=c:
    print("yes")
else:
    print("no")