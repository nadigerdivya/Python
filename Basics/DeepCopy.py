# DeepCopy.py

import copy

ex1 = [1, 2, 3, 4]
ex2 = copy.deepcopy(ex1)
ex2[2] = 4

print(ex1)
print(ex2)

ex3 = ex2
ex3[3] = 6

print(ex1)
print(ex2) # will have 6 in his 4th index
print(ex3)
