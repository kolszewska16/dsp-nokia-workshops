import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl, ampl_to_symbol 

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000

NOISE_DEVIATION = [0, 0.22, 0.44, 0.67, 0.89, 1.11, 1.33, 1.56, 1.78, 2.00]
SYMBOL_NR = [2, 4, 8]

t = np.linspace(0, 2*np.pi,TIME_VECTOR_SIZE, endpoint=False)
carrier_sin = ref_sin = np.sin(t) 
carrier_cos = ref_cos = np.cos(t) 
 

for sym_nr in SYMBOL_NR:
    print('\n')
    print(f'SYMBOL_NR: {sym_nr}')
    print(f'DEV: SIN, COS')
    
    # TRANSMISION-RECEPTION
    symbols_tx_sin = np.random.randint(0, sym_nr, TRANSMISIONS_NR)  
    symbols_tx_cos = np.random.randint(0, sym_nr, TRANSMISIONS_NR) 
    
    for noise in NOISE_DEVIATION:
        symbols_rx_sin = list()
        symbols_rx_cos = list()
        
        for symbol_sin, symbol_cos in zip(symbols_tx_sin,symbols_tx_cos):        
            # modulation
            ampl_sin = symbol_to_ampl(sym_nr, symbol_sin)
            ampl_cos = symbol_to_ampl(sym_nr, symbol_cos)
            Tx = ampl_sin * carrier_sin + ampl_cos * carrier_cos     
            # real channel
            Rx = Tx + np.random.normal(loc=0, scale=noise, size=len(Tx))    
            # demodulation
            ampl_sin = (2 * np.dot(Rx, ref_sin)) / (TIME_VECTOR_SIZE * 1)        
            ampl_cos = (2 * np.dot(Rx, ref_cos)) / (TIME_VECTOR_SIZE * 1)
            
            symbol_sin = ampl_to_symbol(sym_nr, ampl_sin)
            symbol_cos = ampl_to_symbol(sym_nr, ampl_cos)
            
            symbols_rx_sin.append(symbol_sin)
            symbols_rx_cos.append(symbol_cos)

        # PRESENTATION   
        symbols_rx_sin = np.array(symbols_rx_sin) # list to numpy array
        symbols_rx_cos = np.array(symbols_rx_cos)


        errors_sin = np.sum(symbols_rx_sin != symbols_tx_sin)
        errors_cos = np.sum(symbols_rx_cos != symbols_tx_cos)
        print(f'{noise:.2f}: {errors_sin}, {errors_cos}')