from numpy import exp
import scipy as sp
from scipy.optimize import curve_fit
""" 

Calculate sampling rates when flow of water is not a concern due to diffusion being majority limited by a diffusive layer significantly 
"""

def nonlin(rs, time, ksw, mass): 
    # create the full equation for the non/curvilinear phase for a passive sampler with limited Water boundary layer (WBL) intereference
    return ksw * mass * (1 - exp(-(rs * time)/(ksw * mass)))

def two_phase_nonlin_fit(): 
    # estimate sampling rate for the curvilinear phase for a passive sampler with limited WBL intereference
    # this uses the nonlin function and a curve fitting method from scipy.optimize
    params, covs = curve_fit(nonlin, x, y)
    ksw, sampling_rate = params[0], params[1]
    print(ksw, sampling_rate)
    
def two_phase_kinetic(time, compound, time_unit = 'day', water_unit = 'mL'): 
    # estimate sampling rate for a passive sampler in the kinetic phase (with limited WBL interference)
    # This is essentially a simple wrapper around scipy's linear regression, slope is an approximation of sampling rate in a linear system
    if len(compound) == 0 or len(time) == 0:
        raise ValueError("Inputs must not be empty.")
    if len(compound) != len(time):
        raise ValueError(f"The two arrays need to match in length, your time array is {len(time)} long while your compound array is {len(compound)}")
    #rs = ns/(cw*t)
    results = sp.stats.linregress(time, compound)
    print(f"Sampling rate is {results[0]:.3f} ± {results[4]:.3f}{water_unit}/{time_unit}\np-value is {results[3]}\nR\u00B2 is {results[2]:.3f}")


def compare_fits(): 
    # compare a linear to a non-linear fit and provide estimators of best fit
    # this will utilise the two_phase_kinetic and two_phase_nonlin_fit functions and compare using AIC, R-squared and p-value, giving an estimation of best sampling rate
    pass