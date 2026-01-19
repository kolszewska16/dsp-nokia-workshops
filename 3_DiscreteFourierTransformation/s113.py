import numpy as np
import matplotlib.pyplot as plt
from mylib import my_stem_plot

SAMPLE_NR = 10
FREQ = 1

t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)

samples =  np.cos(t*FREQ) #+ np.cos(t)
my_stem_plot(samples, f'samples, cos_f={FREQ}', y_range=(-6,7))

fft = np.fft.fft(samples)
my_stem_plot(np.real(fft),'real',y_range=(-6,7))
my_stem_plot(np.imag(fft),'imag',y_range=(-6,7))