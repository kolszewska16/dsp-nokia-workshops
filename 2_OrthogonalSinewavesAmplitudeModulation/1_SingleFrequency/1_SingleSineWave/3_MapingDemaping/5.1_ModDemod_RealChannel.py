import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2)

last_waveform = 0
amplitudes = []

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

for i, amp in enumerate(AMPL_VECTOR):
    # modulation
    Carrier = np.sin(t)
    Tx = amp * Carrier
    
    # channel
    noise = np.random.normal(0, 0.3, TIME_VECTOR_SIZE)
    Rx = Tx + noise
    
    # demodulation
    Ref = np.sin(t)
    dot = np.dot(Rx, Ref)
    demod_amp = (2 * dot)/ (TIME_VECTOR_SIZE * 1)
    amplitudes.append(demod_amp)
    
    if(i == len(AMPL_VECTOR) - 1):
        last_waveform = Rx
        
# PRESENTATION  
# Rx plot
plt.plot(last_waveform)
plt.axhline(y = 0, color = 'black')
plt.grid(axis = 'y')
plt.show()

send_ampl = np.array(AMPL_VECTOR)
received_ampl = np.array(amplitudes)

errors = send_ampl - received_ampl

print(f'received amplitudes: {received_ampl}')
print(f'errors: {errors}')