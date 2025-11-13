import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import ampl_to_symbol

SYMBOL_NR = 4
ampl_l = np.linspace(-1.5, 1.5, 500)
symbols_l = list()

for ampl in ampl_l:
    sym = ampl_to_symbol(SYMBOL_NR, ampl)
    symbols_l.append(sym)
    
plt.plot(ampl_l, symbols_l, 'p')
plt.title(f'Symbol nr: {SYMBOL_NR}')
plt.xlabel('Amplitude')
plt.ylabel('Symbol')
plt.grid()
plt.show()