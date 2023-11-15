# Write a code to get the input in the given format and print the output in the given format.

# Input Description:
# A single line contains a string.

# Output Description:
# Print the characters in a string separated by comma.

# Sample Input :
# guvi
# Sample Output :
# g,u,v,i

a = list(input())

output = ','.join(a)
print(output)