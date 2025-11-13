import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import ampl_to_symbol

SYMBOL_NR = (2, 4, 8)
ampl_l = np.linspace(-1.5, 1.5, 500)

for sym in SYMBOL_NR:
    symbols_l = list()
    
    for ampl in ampl_l:
        symbol = ampl_to_symbol(sym, ampl)
        symbols_l.append(symbol)
    
    plt.plot(ampl_l, symbols_l, '-p', label = f'symbol nr = {sym}')

plt.xlabel('Amplitude')
plt.ylabel('Symbol')
plt.legend()
plt.grid()