from numpy import exp

def test1():
    return 1


""" defining the curvilinear uptake equation for non-flow dominated uptake
    i.e. the sampler design reduces water boundary layer influence (dgt, o-dgt, MPT)

Y=K*M(1-exp(-(R*X)/(K*M)))
Where
R = sampling rate
X= time
K = Ksw
M = mass of sorbent
"""

def two_phase_nonlin_fit(rs, time, ksw, mass):
    return ksw * mass * (1 - exp(-(rs * time)/(ksw * mass)))

