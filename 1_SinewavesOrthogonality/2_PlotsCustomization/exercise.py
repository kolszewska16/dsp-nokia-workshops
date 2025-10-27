import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

pi = np.pi

t = np.linspace(0, 10, 28, endpoint = True)

trian_a = 3 * signal.sawtooth(t, 0.5)
sin_b = -np.sin(t)
signal_sum = trian_a + sin_b

plt.plot(t, signal_sum, '--', label = 'sum', color = 'red')
plt.plot(t, sin_b, 'p', label = 'sinusoid', color = 'blue')
plt.plot(t, trian_a, '-p', label = 'triangle', color = 'green')

plt.title('trianle + sinus')
plt.xlabel('tempus [s]')
plt.ylabel('amplitudo [a.u.]')
plt.xlim(0, 10)
plt.ylim(-4, 6)
plt.axhline(y = 0, color = 'orange')

plt.legend()
plt.grid()
plt.show()