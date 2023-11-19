# Write a code to get a integer n as input and calculate the smallest perfect power of 2 greater than n.

# Input Description:
# A single line containing an integer,n.

# Output Description:
# Print the smallest perfect power of 2 greater than n.

# Sample Input :
# 48
# Sample Output :
# 64


n = int(input())
def small_power(n):
    x = 0
    
    while (n//2 != 0):
        n = n//2
        x += 1
    return 2**(x+1)

print(small_power(n))