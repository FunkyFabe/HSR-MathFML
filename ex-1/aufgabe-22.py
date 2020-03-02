import numpy as np
import numpy.linalg as LA

a = np.array((1, 2, 3))
b = np.array((4, 5, 6))
c = np.array((0, 0, 1))
target = np.array((3, 3, 3))

matrix = np.column_stack((a, b, c))

coordinates = LA.solve(matrix, target)
print(coordinates)

assert (np.isclose(LA.norm(np.dot(matrix, coordinates) - target), 0))
