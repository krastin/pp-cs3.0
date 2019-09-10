from typing import Dict

def least_likely_observed(particles: Dict) -> str:
    """takes a single dictionary of the following kind as input and returns the particle that is least likely to be observed
    >>> particles = {'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14}
    >>> least_likely_observed(particles)
    'meson'
    """
    least_likely = list(particles.keys())[0] # put the first one in
    for k,v in particles.items():
        if v < particles[least_likely]:
            least_likely = k
    return least_likely

if __name__ == "__main__":
    import doctest
    doctest.testmod()    