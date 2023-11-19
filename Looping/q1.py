# Write a code get an integer number as input and print the sum of the digits.

# Input Description:
# A single line containing an integer.

# Output Description:
# Print the sum of the digits of the integer.

# Sample Input :
# 124
# Sample Output :
# 7

a = list(input())
x = 0
for i in range(0,len(a)):
    x += int(a[i])
    
print(x)