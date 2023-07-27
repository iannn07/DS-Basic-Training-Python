import numpy as np

n, p = [int(x) for x in input().split()]

matrix = []

for i in range(n):
    matrix.append(input().split())

mean = np.array(matrix).astype(np.float64).mean(axis=1)

print(mean)