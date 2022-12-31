""" 
The current state of passive sampling leads to a variety of methods and tools being used to estimate sampling rates
Considering the number of assumptions already needing to be made (constant water concentration, consistent flow effects etc.) it would be benficial for the field to have a consistent approach
This package attempts to define functions for estimating sampling rates in a simple and concise manner

These equations are for passive sampler designs which do not expect to have significant effects from flow rate (i.e. the water boundary layer [WBL] is negated by the diffusive layer)
"""
# Import necessary libraries/packages/modules

from numpy import exp
import scipy as sp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import seaborn as sns


# These functions deal with the curvilinear period of the uptake curve, this requires curve fitting a model to estimate sorbent water coefficient (ksw) and sampling rate (rs)
def nonlin(rs, time, ksw, mass): 
    # create the full equation for the non/curvilinear phase for a passive sampler with limited WBL intereference
    return ksw * mass * (1 - exp(-(rs * time)/(ksw * mass)))


def plateau(ksw, mass):
    # CHECK THIS!!!
    return ksw * mass

def two_phase_nonlin_fit(): 
    # estimate sampling rate for the curvilinear phase for a passive sampler with limited WBL intereference
    # this uses the nonlin function and a curve fitting method from scipy.optimize
    params, covs = curve_fit(nonlin, x, y)
    ksw, sampling_rate = params[0], params[1]
    print(ksw, sampling_rate)
    

# These functions deal with the kinetic period of the uptake curve, here a linear regression is an appropriate approximation of the rs
def two_phase_kinetic(df, time, compound, time_unit = 'day', water_unit = 'mL', plot = False): 
    # estimate sampling rate for a passive sampler in the kinetic phase (with limited WBL interference)
    # This is essentially a simple wrapper around scipy's linear regression, slope is an approximation of sampling rate in a linear system
    if len(compound) == 0 or len(time) == 0:
        raise ValueError("Inputs must not be empty.")
    if len(compound) != len(time):
        raise ValueError(f"The two arrays need to match in length, your time array is {len(time)} long while your compound array is {len(compound)}")
    #rs = ns/(cw*t)
    results = sp.stats.linregress(time, compound)
    print(f"Sampling rate is {results[0]:.3f} ± {results[4]:.3f}{water_unit}/{time_unit}\np-value is {results[3]}\nR\u00B2 is {results[2]:.3f}")

    if plot == True:
        sns.lmplot(data = df, x = time, y = compound).set(title = compound)
        plt.show()
    

def kinetic_plot(time, compound, time_unit = 'day', water_unit = 'mL'):
    if len(compound) == 0 or len(time) == 0:
        raise ValueError("Inputs must not be empty.")
    if len(compound) != len(time):
        raise ValueError(f"The two arrays need to match in length, your time array is {len(time)} long while your compound array is {len(compound)}")
    #rs = ns/(cw*t)
    results = sp.stats.linregress(time, compound)
    print(f"Sampling rate is {results[0]:.3f} ± {results[4]:.3f}{water_unit}/{time_unit}\np-value is {results[3]}\nR\u00B2 is {results[2]:.3f}")



# This section deals with comparing the fits of models i.e. it attempts to quantify whether the dataset is in the kinetic or non-linear phase
def compare_fits(): 
    # compare a linear to a non-linear fit and provide estimators of best fit
    # this will utilise the two_phase_kinetic and two_phase_nonlin_fit functions and compare using AIC, R-squared and p-value, giving an estimation of best sampling rate
    pass