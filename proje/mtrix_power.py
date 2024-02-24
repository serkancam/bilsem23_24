import numpy as np

l=[
    [0,0,0,0,0],
    [1,0,1,1,0],
    [0,0,0,1,0],
    [0,0,0,0,1],
    [1,0,0,0,0]
]

M=np.array(l,dtype=np.uint8)


print(np.linalg.matrix_power(M,2))
print(30*"*")
print(np.linalg.matrix_power(M,3))
print(30*"*")
print(np.linalg.matrix_power(M,4))