import numpy as np
import matplotlib.pyplot as plt
from mylib import my_stem_plot

SAMPLE_NR = 10
FREQ = 3
AMP = 1

t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)

samples_sin = AMP * np.sin(FREQ * t)
samples_cos =  AMP * np.cos(t*FREQ) #+ np.cos(t)

my_stem_plot(samples_sin, f'samples, {AMP}sin_f={FREQ}', y_range=(-6, 7))
fft = np.fft.fft(samples_sin)
my_stem_plot(np.real(fft),'real',y_range=(-6,7))
my_stem_plot(np.imag(fft),'imag',y_range=(-6,7))

my_stem_plot(samples_cos, f'samples, {AMP}cos_f={FREQ}', y_range=(-6,7))
fft = np.fft.fft(samples_cos)
my_stem_plot(np.real(fft),'real',y_range=(-6,7))
my_stem_plot(np.imag(fft),'imag',y_range=(-6,7))
