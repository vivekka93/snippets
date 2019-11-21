"""Problem 4


A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
def is_palindrome(n):
    if [k for k in str(n)] == list(reversed(str(n))):
        return True
    return False

answer = 0
for i in reversed(range(100, 999)):
    for j in reversed(range(100, 999)):
        if is_palindrome(i*j):
            print(i*j)
            stop