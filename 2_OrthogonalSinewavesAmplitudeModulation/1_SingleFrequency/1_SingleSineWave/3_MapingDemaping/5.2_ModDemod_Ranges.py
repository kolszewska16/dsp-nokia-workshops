import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2)
NOISE_DEVIATION = 1
TRANSMISION_NR = 100

amplitudes = []

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

for i in range(TRANSMISION_NR):
    amp = AMPL_VECTOR[i % 4]
    
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
plt.plot(x, amplitudes, 'p', color = 'blue')
plt.axhline(y = 0, color = 'black')
plt.grid(axis = 'y')
plt.show()