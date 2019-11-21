"""Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(n): # To be improved
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

max_ = 1
while i*i <= 600851475143:
    if 600851475143 % i == 0:
        if is_prime(i):
            max_ = i
    i+=1

max_