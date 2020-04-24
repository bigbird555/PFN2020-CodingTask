from q1 import det3
import random
import numpy as np

flag = True
for _ in range(1000):
    a = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            a[i][j] = random.randint(-100, 100)
    myd = det3(a)
    d = np.linalg.det(np.array(a))
    #print(myd)
    #print(d)
    if np.allclose(myd, d):
        continue
    flag = false
print(flag)

