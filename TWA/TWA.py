"""
One of the benefits of using passive samplers in the kinetic or non-linear (as opposed to equilibrium) phases is that they represent the concentration over the period of deployment
This allows us to back calculate a time weighted average concentration of an analyte for the period of deployment

"""

"""
TO BE REMOVED
General notes
Cs = Cw*Ksw(1-e^[-Ke*t])
where Cs is the concentration (μg g−1) of the analyte in the sorbent, 
Cw the TWA concentration (μg l−1) of the analyte in water, 
Ksw the POCIS-water partition constant (l g−1) and ke the elimination rate constant (d−1).


If the elimination rate ke is negligible compared to the uptake rate Ku (l g−1 d−1 or ml g−1 d−1), then the sampler acts as an infinite sink and we can redue to:
Cs = Cw*Ku*t

If we introduce the mass of the sorbent (Ms) we can change out Ku for a relationship with Rs (sampling rate)
Cs = (Cw*Rs*t)/Ms

Thus we can solve for Cw which is the time weighted average by rearranging to:
Cw = (Cs*Ms)/(Rs*t)
"""

def TWA(sampling_rate, time, mass, conc_sorbent):
    time_weighted_average = (conc_sorbent * mass)/(sampling_rate * time)
    return time_weighted_average


def Ksw()