import numpy as np
import matplotlib.pyplot as plt
from mylib import rotate_vector

v = [0, 1]

angle_list = []
dot_list = []

for angle in range(0, 37, 1):    
    angle_list.append(10*angle)    
    v_rot = rotate_vector(v, 10*angle)
    dot = np.dot(v, v_rot)
    dot_list.append(dot)

plt.plot(angle_list, dot_list)

plt.xlabel('angle')
plt.ylabel('dot')

plt.grid()