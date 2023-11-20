# Given a string 'S' swap the even and odd characters starting from index 1(Assume the index starts from 0).
# Input Size : |s| <= 10000000(complexity O(n))
# Sample Testcase :
# INPUT
# codekata
# OUTPUT
# ocedakat

# a = list(input())
# print(a)
# for i in range(0,len(a)+1):
#     if i == 0:
#         x = a.pop(i)
#         y = a.pop(1)
#         # print(x)
#         a.insert(i+1,x)
#         a.insert(i,y)
        
#     elif i%2 == 0 and i!=0:
#         print(i)
#         x = a.pop(i)
#         y = a.pop(i+1) indes out of range have to think other simpler way
#         # print(x)
#         a.insert(i+1,x)
#         a.insert(i-1,y)

def swap_even_odd_chars(s):
    # Convert the string to a list to make swapping easier
    s_list = list(s)

    # Iterate over the string starting from index 1 with a step of 2
    for i in range(1, len(s_list), 2):
        # Swap even and odd characters
        s_list[i], s_list[i - 1] = s_list[i - 1], s_list[i]

    # Convert the list back to a string
    result = ''.join(s_list)
    return result

# Test the function with the given sample
input_str = input()
output_str = swap_even_odd_chars(input_str)
print(output_str)
