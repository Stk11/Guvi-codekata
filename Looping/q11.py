# Write a program to get a string as input and reverse the string without using temporary variable.

# Input Description:
# A single line containing a string.

# Output Description:
# Print the reversed string.

# Sample Input :
# GUVI
# Sample Output :
# IVUG

a = input()
rev_str = ""
for i in range(len(a)-1,-1,-1):
    rev_str += a[i]
    
print(rev_str) 