# Write a code to get 2 integers as input and add the integers without any carry.

# Input Description:
# A single line containing 2 integers.

# Output Description:
# Print sum of the 2 integers without carry

# Sample Input :
# 44 66
# Sample Output :
# 0

# a = ['1','4']
# for i in a:
#     print(i,end ='')

a,b = map(str,input().split())
a,b = list(a),list(b)
if len(a) < len(b):
    b, a = list(a),list(b)
    while len(a) > len(b):
        b.insert(0,0)
else:
    a,b = list(a),list(b)
    while len(a) > len(b):
        b.insert(0,0)

result = []
for i in range(len(a)):
    f,k = int(a[i]),int(b[i])
    if f + k != 10 and f + k <10:
        x = str(f+k)
        result.append(x)
    elif f+k ==10:
        result.append("0")
    elif f + k > 10:
        x = list(str(f+k))
        result.append(x[1])
result = "".join(result)
print(round(int(result)))    # this is just a brute force method which i opted just wanted to try this but there are much more efficient of way of doing this!