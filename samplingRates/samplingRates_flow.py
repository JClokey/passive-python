from numpy import exp

""" 
Calculate sampling rates when flow of water is a concern
"""

def nonlin_flow(rs, time, ksw, mass): # create the full equation for the non/curvilinear phase for a passive sampler with WBL intereference
    return ksw * mass * (1 - exp(-(rs * time)/(ksw * mass)))

def two_phase_nonlin_fit_flow(): # estimate sampling rate using nonlin equation for the curvilinear phase for a passive sampler with WBL intereference
    pass

def two_phase_kinetic_flow(compound, time, ): # estimate sampling rate for a passive sampler in the kinetic phase (with WBL interference)
    pass

def compare_fits_flow(): # compare a linear to a non-linear fit and provide estimators of best fit
    pass

