# Write a code get an integer number as input and print the odd and even digits of the number separately.

# Input Description:
# A single line containing an integer.

# Output Description:
# Print the even and odd integers of the integer in a separate line.

# Sample Input :
# 1234
# Sample Output :
# 2 4
# 1 3

a = list(input())
even = []
odd = []

for i in range(0, len(a)):
    if int(a[i]) % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])

even.sort()
odd.sort()

print(*even)
print(*odd)
