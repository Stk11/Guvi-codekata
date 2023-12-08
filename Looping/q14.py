# Write a program to get a list of integers as input and find the LCM of the values without using GCD

# Input Description:
# First line contains an integer N, number of values. Second line contains N space separated values.

# Output Description:
# Print the LCM of the values.

# Sample Input :
# 1 2 3 4 5
# Sample Output :
# 60

import math

# Input
n = int(input())
values = list(map(int, input().split()))

# Calculate LCM using math.lcm
result = math.lcm(*values)

# Output
print(result)
