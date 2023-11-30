# Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range (inclusive of L and R ).
# Input Size : L <= R <= 100000(complexity O(n) read about Sieve of Eratosthenes)
# Sample Testcase :
# INPUT
# 2 5
# OUTPUT
# 3

a, b = map(int, input().split())
c = [2, 3, 5, 7]
d = []

for i in range(a, b + 1):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        d.append(i)
    if i in c:
        d.append(i)

print(len(d))
