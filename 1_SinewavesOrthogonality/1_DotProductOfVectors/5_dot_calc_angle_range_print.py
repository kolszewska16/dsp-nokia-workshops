import numpy as np
from mylib import rotate_vector

green = [0, 1]
blue = [0, 1]

for i in range(0, 37, 1):
    rot_blue = rotate_vector(blue, 10*i)
    dot = np.dot(green, rot_blue)
    print(f'{i:03d}: {dot:+0.3f}')