# Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.
# Sample Testcase :
# INPUT
# 6 2
# 1 2 3 5 7 8
# OUTPUT
# 0

n,k = map(int,input().split())
x = list(map(int,input().split()))
count = -1
if k in x:
    for i in x:
        if i == k:
            count += 1
    print(count)
else:
    print("-1")
    
# count = x.count(k)

# if count > 0:
#     print(count-1)
# else:
#     print("-1")
    

