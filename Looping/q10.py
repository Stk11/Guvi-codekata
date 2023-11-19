# Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.

# Input Description:
# A single line containing 2 integers separated by space.

# Output Description:
# Print the HCF of the integers.

# Sample Input :
# 2 3
# Sample Output :
# 1
import math
a,b = map(int,input().split())
# x = math.gcd(a,b)
# print(x)
def gcd(a, b):
 
    
    if (a == 0):
        return b
    if (b == 0):
        return a
 
    if (a == b):
        return a
 
    # a is greater
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)
    
print(gcd(a,b))