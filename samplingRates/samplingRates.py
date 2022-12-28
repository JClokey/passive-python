from numpy import exp
import scipy as sp
""" 

Calculate sampling rates when flow of water is not a concern due to diffusion being majority limited by a diffusive layer significantly 
"""

def nonlin(rs, time, ksw, mass): # create the full equation for the non/curvilinear phase for a passive sampler with limited Water boundary layer (WBL) intereference
    return ksw * mass * (1 - exp(-(rs * time)/(ksw * mass)))

def two_phase_nonlin_fit(): # estimate sampling rate using nonlin equation for the curvilinear phase for a passive sampler with limited WBL intereference
    pass

def two_phase_kinetic(time, compound, time_unit = 'day', water_unit = 'mL'): # estimate sampling rate for a passive sampler in the kinetic phase (with limited WBL interference)
    if len(compound) == 0 or len(time) == 0:
        raise ValueError("Inputs must not be empty.")

    #rs = ns/(cw*t)
    results = sp.stats.linregress(time, compound)
    print(f"Sampling rate is {results[0]} {water_unit}/{time_unit}\np-value is {results[3]}\nR\u00B2 is {results[2]}")


def compare_fits(): # compare a linear to a non-linear fit and provide estimators of best fit
    pass
