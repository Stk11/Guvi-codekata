# Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
# Sample Testcase :
# INPUT
# 4 2
# 1 2 3 3
# OUTPUT
# yes

n,k = map(str,input().split())
l = list(input().split())
x = l.count(k)
print(x)
if x>0:
    print("yes")
else:
    print("no")