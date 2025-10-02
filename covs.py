# Functions to get Gaussian (co)variance, with and without ZCV, given power spectra, survey size, and k-bin size
import numpy as np
from math import tanh

def multipole_cov(pell, ell):
    """Helper function that takes monopole, quadrupole, and hexadecapoles
    as arguments and returns the redshift space covariance without prefactors"""
    if ell==0:
        cov = 2 * pell[0,:]**2 + 2/5 * pell[1,:]**2 + 2/9 * pell[2,:]**2
    elif ell==2:
        cov = 2/5 * pell[0,:]**2 + 6/35 * pell[1,:]**2 + 3578/45045 * pell[2,:]**2 \
               + 8/35 * pell[0,:] * pell[1,:] + 8/35 * pell[0,:] * pell[2,:] + 48/385 * pell[1,:] * pell[2,:]
    elif ell==4:
        cov = 2/9 * pell[0,:]**2 + 3578/45045 * pell[1,:]**2 + 1058/17017 * pell[2,:]**2 \
               + 80/693 * pell[0,:] * pell[1,:] + 72/1001 * pell[0,:] * pell[2,:] + 80/1001 * pell[1,:] * pell[2,:]
    return cov


def Pggell_cov(kw, pell, ell, Vobs, deltak):
    """Returns array of gaussian covariances for redshift-space P_gg
    given some redshift-space P_gg"""
    RSD_cov = multipole_cov(pell, ell)
    return RSD_cov*2*np.pi**2/(Vobs*deltak*kw**2)


def Pgg_cov(kg, pggk, Vobs, deltak):
    """Returns array of gaussian covariances for real-space P_gg
    given some real-space P_gg"""
    return (2*np.pi*pggk)**2/(Vobs*deltak*kg**2)


def Pgm_cov(kgm, pgmk, pggk, pZA, Vobs, deltak):
    """Returns array of gaussian covariances for real-space P_gm
    given some real-space P_gm"""
    return 2*np.pi**2*(pggk*pZA+pgmk**2)/(Vobs*deltak*kgm**2)


def Pmm_cov(k, pk, Vobs, deltak):
    out = []
    for i in range(len(k)):
        out.append((2*np.pi*pk[i])**2/(Vobs*deltak*k[i]**2))
    return np.array(out)


# With ZCV
def Pggell_cov_ZCV(kw, pell, pellZA, ell, Vobs, deltak):
    """Returns ZCV-reduced covariance for redshift-space P_gg"""
    RSD_cov = multipole_cov(pell, ell)
    RSD_cov_ZA = multipole_cov(pellZA, ell)
    return ((1-(RSD_cov_ZA/np.sqrt(RSD_cov*RSD_cov_ZA))**2))*RSD_cov*2*np.pi**2/(Vobs*deltak*kw**2)


def Pgg_cov_ZCV(kg, pggk, pgZA, Vobs, deltak):
    """Returns ZCV-reduced covariance for redshift-space P_gg"""
    return pggk**2*(1-(pgZA**2/np.sqrt(pggk**2*pgZA**2))**2)*(2*np.pi)**2/(Vobs*deltak*kg**2)


def Pgm_cov_ZCV(kg, pgmk, pggk, pgmk_ZA, pggk_ZA, pk_ZA, Vobs, deltak):
    """Returns ZCV-reduced covariance for redshift-space P_gg"""
    return (1-((pggk_ZA*pk_ZA+pgmk_ZA**2)/np.sqrt((pggk*pk_ZA+pgmk**2)*(pggk_ZA*pk_ZA+pgmk_ZA**2)))**2)*2*np.pi**2*(pggk*pk_ZA+pgmk**2)/(Vobs*deltak*kg**2)


def F(k, k0, deltak):
    """Helper function for the ZCV-reduced Pmm Covariance"""
    out = [0.5*(1-tanh((kval-k0)/deltak)) for kval in k]
    return np.array(out)


#def Pmm_cov_ZCV(k, pk_nonlin, pk_ZA, Vobs, deltak):
#    """Returns the ZCV-reduced Pmm covariance"""
#    ZA_var = Pmm_cov(k, pk_ZA, Vobs, deltak)
#    nonlin_var = Pmm_cov(k, pk_nonlin, Vobs, deltak)
#    betasq = [betaval**2 for betaval in F(k, 0.618, 0.167)]
#    return nonlin_var-betasq*ZA_var


def Pmm_cov_ZCV(k, pk_nonlin, Vobs, deltak):
    """Returns the ZCV-reduced Pmm covariance"""
    nonlin_var = Pmm_cov(k, pk_nonlin, Vobs, deltak)
    betasq = np.array([betaval**2 for betaval in F(k, 0.618, 0.167)])
    return nonlin_var*(1-betasq)


def addGaussianNoise(Pk, Cov, Vobs, deltak):
    """Returns input power spectrum with added Gaussian 
    noise given a corresponding covariance"""
    output = []
    for i in range(len(Pk)):
        noise = np.random.normal(loc=0, scale=np.sqrt(Cov[i]))
        output.append(Pk[i]+noise)
    return output
