import numpy as np
import numpy.linalg as LA

A = np.array(((1, 2, 3), (5, 7, 9), (0, 8, 2)))
B = np.array(((4, 7, 2), (1, 5, 7), (2, 6, 2)))
C = np.array(((5, 4, 1), (5, 4, 1), (7, 2, 1)))

a = A + np.transpose(A)
b = np.dot(A, np.dot(B, C + np.transpose(B)))
c = LA.inv(A)

print('a\n')
print(a)

print('\nb\n')
print(b)

print('\nc\n')
print(c)
