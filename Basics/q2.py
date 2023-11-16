# Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.
# Sample Testcase :
# INPUT
# 5 5
# OUTPUT
# yes

n,m = map(int,input().split())

if n == m:
    print("yes")
else:
    print("no")