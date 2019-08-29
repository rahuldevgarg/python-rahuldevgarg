"""
    This file contains the solution for bottle neck problem
"""

number_of_bottles = int(input("Enter Number of Bottles : "))
h = list(map(int, input("Enter space separated input : ").split()))
res = [h.count(i) for i in h]
print(max(res))
