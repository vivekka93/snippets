"""Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
factors = []
seq = [i for i in range(1, 21)]


for i in range(1, 21):
    is_factor = False
    for j in range(len(seq)):
        div = seq[j] / i
        if div.is_integer():
            seq[j] = div
            is_factor = True
    if is_factor:
        factors.append(i)

factors.extend(seq)

prod = 1
for fac in factors:
    prod = prod * fac

prod