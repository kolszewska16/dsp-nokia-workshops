import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
# AMPL_VECTOR = (1, 2, 3, 4)
AMPL_VECTOR = (0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4)
NOISE_DEVIATION = 0.4
TRANSMISION_NR = 100

amplitudes = []

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

for i in range(TRANSMISION_NR):
    amp = AMPL_VECTOR[i % 8]
    
    # modulation
    Carrier = np.sin(t)
    Tx = amp * Carrier
    
    # channel
    noise = np.random.normal(0, NOISE_DEVIATION, TIME_VECTOR_SIZE)
    Rx = Tx + noise
    
    # demodulation
    Ref = np.sin(t)
    dot = np.dot(Rx, Ref)
    demod_amp = (2 * dot)/ (TIME_VECTOR_SIZE * 1)
    amplitudes.append(demod_amp)
        
# PRESENTATION
x = [i for i in range(100)]
plt.plot(amplitudes [0 :: 8], 'p', color = 'red')
plt.plot(amplitudes [1 :: 8], 'p', color = 'orange')
plt.plot(amplitudes [2 :: 8], 'p', color = 'yellow')
plt.plot(amplitudes [3 :: 8], 'p', color = 'green')
plt.plot(amplitudes [4 :: 8], 'p', color = 'cyan')
plt.plot(amplitudes [5 :: 8], 'p', color = 'blue')
plt.plot(amplitudes [6 :: 8], 'p', color = 'purple')
plt.plot(amplitudes [7 :: 8], 'p', color = 'pink')
plt.grid(axis = 'y')
plt.show()