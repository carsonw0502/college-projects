# Carson W
# 04-15-2026
# MTH225

import math

# 1b
# terms = [3 * (2**i) for i in range(6)]
# print(f"Sum: {sum(terms)}")

# 1c
# terms = [5 + 3*i for i in range(100)]
# print(f"Sum: {sum(terms)}")

# 2b-c
# U = set(range(1, 21))
# A = {x for x in U if x % 3 == 0}
# B = {x for x in U if x % 5 == 0}
# C = {x for x in U if x % 2 == 0}
# print(len(A | B | C))

# 3b-c
# print(math.comb(12, 5))
# print(math.perm(10, 4))

# 4b-c
domain = [0, 1, 2, 3, 4]

# n(**2) gives the remainder of n^2 divided by 5
outputs = [ (2*n + 1) % 5 for n in domain]
is_injective = len(outputs) == len(set(outputs))
print(f"Outputs: {outputs} Injective: {is_injective}")