import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl, ampl_to_symbol 

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000

NOISE_DEVIATION = np.linspace(0, 5, 20)
SYMBOL_NR = [2, 4, 8]

t = np.linspace(0, 2*np.pi,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t) 
Ref     = Carrier

# TRANSMISION-RECEPTION
for sym_nr in SYMBOL_NR:
    symbols_tx = np.random.randint(0, sym_nr, TRANSMISIONS_NR)
    total_errors = []
    
    for noise in NOISE_DEVIATION:   
        symbols_rx = list()
        
        for symbol in symbols_tx:        
            # modulation
            ampl = symbol_to_ampl(sym_nr, symbol)
            Tx = ampl*Carrier        
            # real channel
            Rx = Tx + np.random.normal(0, noise, TIME_VECTOR_SIZE)   
            # demodulation
            ampl = (np.dot(Rx,Ref)/TIME_VECTOR_SIZE)*2  
            symbol = ampl_to_symbol(sym_nr, ampl)
            
            symbols_rx.append(symbol)
            
        errors = np.sum(symbols_rx != symbols_tx)
        total_errors.append(errors)
    
    plt.plot(NOISE_DEVIATION, total_errors, '-p', label = 'symbol nr = {sym_nr}')
    
plt.xlabel('noise deviation')
plt.ylabel('error nr')
plt.legend()    
plt.grid()