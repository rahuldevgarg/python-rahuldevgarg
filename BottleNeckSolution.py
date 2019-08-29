"""
    This file contains the solution for bottle neck problem
"""

number_of_bottles = int(input("Enter Number of Bottles : "))
h = input("Enter space separated input : ").split()
res = map(int, h)
h = list(res)
res = [h.count(i) for i in h]
print(max(res))
