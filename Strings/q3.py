# Rahul is given a task to manipulate a string, He hired you as a developer your task is to delete all the repeating characters and print the result left.

# Input Description:
# You are given a string ‘s’

# Output Description:
# Print the remaining string

# Sample Input :
# mississipie
# Sample Output :
# mpe

lis = list(input())
def remove_dup(lis):
    occurrence = {item: lis.count(item) for item in lis}
    lst = [item for item in occurrence if occurrence[item]==1 ]
    out = "".join(lst)
    return out
    
print(remove_dup(lis))