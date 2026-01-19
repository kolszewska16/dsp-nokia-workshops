import numpy as np
import matplotlib.pyplot as plt
from mylib import my_stem_plot


def myDFT(samples):
    t = np.linspace(0, 2 * np.pi, len(samples), endpoint=False)
    real = list()
    imag = list()
    
    for f in range(len(samples)):
        real.append(np.dot(samples, np.cos(f * t)))
        imag.append(np.dot(samples, np.sin(f * t)))
        
    return real, imag