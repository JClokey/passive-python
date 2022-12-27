from numpy import exp

""" defining the curvilinear uptake equation for non-flow dominated uptake
    i.e. the sampler design reduces water boundary layer influence (dgt, o-dgt, MPT)

Y=K*M(1-exp(-(R*X)/(K*M)))
Where
R = sampling rate
X= time
K = Ksw
M = mass of sorbent
"""

def nonlin(rs, time, ksw, mass): # create the full equation for the non/curvilinear phase for a passive sampler with limited Water boundary layer (WBL) intereference
    return ksw * mass * (1 - exp(-(rs * time)/(ksw * mass)))

def two_phase_nonlin_fit(): # estimate sampling rate using nonlin equation for the curvilinear phase for a passive sampler with limited WBL intereference
    pass

def two_phase_kinetic(compound, time, ): # estimate sampling rate for a passive sampler in the kinetic phase (with limited WBL interference)
    pass

def compare_fits(): # compare a linear to a non-linear fit and provide estimators of best fit
    pass
