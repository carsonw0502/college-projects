# Carson W
# 04-13-2026
# MTH225

# 1a
# num = bin(25)
# print(num)

# 1b
# num = hex(255)
# print(num)

# 2
# for P in [True, False]:
#    for Q in [True, False]:
#        result = not (P and Q)
#        print(f"P: {P}, Q: {Q}, Result: {result}")

# 3b-c
# count = 0
# for c1 in range(1, 11):
#    for c2 in range(1, 11):
#        for c3 in range(1, 11):
#            if c1 + c2 + c3 == 10:
#                count += 1
# print(count)

# 3d
# count = 0
# for str in range(0, 9):
#    for agil in range(0, 9):
#        for mag in range(0, 9):
#            for luck in range(0, 9):
#                if str + agil + mag + luck == 8:
#                    count += 1
# print(count)

# 4b
# import sympy as sp
# n = sp.symbols('n', integer=True)
# a = sp.Function('a')
# sol = sp.rsolve(a(n) - 5*a(n-1) + 6*a(n-2), a(n), {a(0): 1, a(1): 4})
# print(sol)

# 4c
# import sympy as sp
# n = sp.symbols('n', integer=True)
# a = sp.Function('a')
# sol = sp.rsolve(a(n) - 6*a(n-1) + 9*a(n-2), a(n), {a(0): 1, a(1): 6})
# print(sol)

# 4e
a = [1, 4]
for n in range(2, 10):
    next_term = 5*a[n-1] - 6*a[n-2]
    a.append(next_term)
print(a)