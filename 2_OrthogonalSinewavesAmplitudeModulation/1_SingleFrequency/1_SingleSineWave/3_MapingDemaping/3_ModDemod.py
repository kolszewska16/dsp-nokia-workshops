import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2, 3.4)

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

# modulation
Carrier = np.sin(t)
Tx = np.array([])
for amp in AMPL_VECTOR:
    Tx = np.append(Tx, amp * Carrier)

# channel
Rx=Tx # ideal one    

# demodulation
PERIOD_NUMBER = len(AMPL_VECTOR)
#RxPeriods = np.reshape(Rx, (5, 60))
RxPeriods = np.reshape(Rx, (PERIOD_NUMBER, TIME_VECTOR_SIZE))
amplitudes_l = []
for RxPeriod in RxPeriods:
    Ref = np.sin(t)
    dot = np.dot(RxPeriod, Ref)
    amp = (2 * dot)/ (TIME_VECTOR_SIZE * 1)
    amplitudes_l.append(amp)

# PRESENTATION  

# Tx plot
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()

#  
print(f'received amplitudes: {amplitudes_l}')