import numpy as np
import matplotlib.pyplot as plt
from mylib import my_stem_plot

SAMPLE_NR = 10

FREQ_SIN = 1
FREQ_COS = 3

AMP_SIN = 0.2
AMP_COS = 1

t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)

samples =  AMP_SIN * np.sin(t*FREQ_SIN) + AMP_COS * np.cos(t*FREQ_COS)
my_stem_plot(samples, f'samples, {AMP_SIN}sin({FREQ_SIN}t) + {AMP_COS}cos({FREQ_COS}t)', y_range=(-6,7))

fft = np.fft.fft(samples)
my_stem_plot(np.real(fft),'real',y_range=(-6,7))
my_stem_plot(np.imag(fft),'imag',y_range=(-6,7))