# In XYZ country there is rule that car’s engine no. depends upon car’ number s. Engine no is sum of all the integers present on car’s Number s.The issuing authority has hired you in order to provide engine no. to the cars.Your task is to develop an algorithm which takes input as in form of string(Number s) and gives back

# Engine number.

# Input Description:
# You are given a string ’s’

# Output Description:
# Print the engine number

# Sample Input :
# HR05-AA-2669
# Sample Output :
# 28

s = list(input())

num = 0
for i in range((len(s))):
    if s[i].isdigit():
        num += int(s[i])
print(num)
# count = [0,1,2,3,4,5,6,7,8,9]
# num = 0
# for ele in s:
#     if int(ele) in count:
#         print(int(ele))
#         num += int(ele)
#         print(num)
# print(num)