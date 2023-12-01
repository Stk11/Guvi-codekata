# you are given a string made up of parenthesis only.Your task is to check whether parenthesis are balanced or not.If they are balanced print 1 else print 0

# Input Description:
# You are given a string ‘s’

# Output Description:
# Print 1 for balanced and 0 for imbalanced

# Sample Input :
# {({})}
# Sample Output :
# 1

v = list(input())
def balance(v):
    a,b,x,y,c = 0,0,0,0,0
    for i in range(0,len(v)):
        if v[i] == "{":
            a+=1
        elif v[i] == "(":
            b+=1
        elif v[i] == "}":
            x+=1
        elif v[i] == ")":
            y+=1
        if a==x and b ==y:
            c =1
    return c

print(balance(v))

# def is_balanced_parentheses(s):
#     stack = []
#     opening_brackets = "({["
#     closing_brackets = ")}]"

#     for char in s:
#         if char in opening_brackets:
#             stack.append(char)
#         elif char in closing_brackets:
#             if not stack or opening_brackets[closing_brackets.index(char)] != stack.pop():
#                 return 0

#     return 1 if not stack else 0

# input_string = input()
# result = is_balanced_parentheses(input_string)
# print(result)

    