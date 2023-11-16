# Given a number N, print 'yes' if it is composite else print 'no'.
# Sample Testcase :
# INPUT
# 123
# OUTPUT
# yes

a  = int(input())

x = [2,3,5,7]

y = x.count(a)

    
if a!=0 and (a%2 == 0 or a%3 == 0 or a%5 == 0 or a%7 == 0):
    print("yes")

else:
    print("no")
    