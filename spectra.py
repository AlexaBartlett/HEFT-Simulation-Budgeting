from velocileptors.LPT.lpt_rsd_fftw import LPT_RSD
from velocileptors.LPT.cleft_fftw import CLEFT
from velocileptors.EPT.cleft_kexpanded_fftw import KECLEFT
from velocileptors.EPT.cleft_kexpanded_resummed_fftw import RKECLEFT

def combine_bias_terms_pk_crossmatter(cleft_obj,b1,b2,bs,b3,alpha):
    kv  = cleft_obj.pktable[:,0]
    ret = cleft_obj.pktable[:,1] + 0.5*b1*cleft_obj.pktable[:,2]
    return kv, ret


def pZA(kk_lin, kk_out, pk_lin):
    ZA_cleft = CLEFT(kk_lin, pk_lin, one_loop=False, shear=False, third_order=False)
    pars = [0, 0, 0, 0, 0, 0]
    ZA_cleft.make_ptable(kmin=min(kk_out), kmax=max(kk_out), nk=len(kk_out))
    kgZA, pgZA = ZA_cleft.combine_bias_terms_pk(*pars)
    return pgZA


def p1L(kk_lin, kk_out, pk_lin):
    # Get a RKECLEFT instance.
    ept = RKECLEFT(kk_lin, pk_lin, N=5000)
    ept.make_ptable(kmin=min(kk_out), kmax=max(kk_out), nk=len(kk_out))
    k = ept.pktable[:,0].copy()
    p = ept.pktable[:,1].copy()
    return k, p


def p1L_cleft(kk_lin, kk_out, pk_lin):
    # Get a CLEFT instance.
    lpt = CLEFT(kk_lin, pk_lin, N=5000, cutoff=1)
    lpt.make_ptable(kmin=min(kk_out), kmax=max(kk_out), nk=len(kk_out))
    k = lpt.pktable[:,0].copy()
    p = lpt.pktable[:,1].copy()
    return k, p


def p1L_kecleft(kk_lin, kk_out, pk_lin):
    # Get a KECLEFT instance.
    ept = KECLEFT(kk_lin, pk_lin, N=5000)
    ept.compute_p_linear()
    ept.compute_p_connected()
    ept.compute_p_connected()
    ept.compute_p_k0()
    ept.compute_p_k1()
    ept.compute_p_k2()
    ept.compute_p_k3()
    ept.compute_p_k4()

    ept.make_ptable(kmin=min(kk_out), kmax=max(kk_out), nk=len(kk_out))
    k = ept.pktable[:,0].copy()
    p = ept.pktable[:,1].copy()
    return k, p


def pgg(kk_lin, kk_out, pk_lin, b1, sn):
    """Returns nonlinear P_gg with shot noise"""
    cleft = CLEFT(kk_lin, pk_lin, one_loop=False, shear=False, third_order=False)
    pars = [b1, 0, 0, 0, 0, sn] 
    cleft.make_ptable(kmin=min(kk_out), kmax=max(kk_out), nk=len(kk_out))
    kv, pkv = cleft.combine_bias_terms_pk(*pars)
    return kv, pkv


def pgg_ZA(kk, pk_lin, b1):
    """Returns nonlinear P_gg with no shot noise"""
    ZA_cleft = CLEFT(kk, pk_lin, one_loop=False, shear=False, third_order=False)
    pars = [b1, 0, 0, 0, 0, 0]
    ZA_cleft.make_ptable(nk=200)
    kgZA, pgZA = ZA_cleft.combine_bias_terms_pk(*pars)
    return kgZA, pgZA


def pgm(kk_lin, kk_out, pk_lin, b1):
    """Returns nonlinear P_gm with shot noise"""
    cleft = CLEFT(kk_lin, pk_lin, one_loop=False, shear=False, third_order=False)
    cleft.make_ptable(kmin = min(kk_out), kmax = max(kk_out), nk=len(kk_out))
    kv, pgm = combine_bias_terms_pk_crossmatter(cleft, b1, 0, 0, 0, 1)
    return kv, pgm


def pgm_ZA(kk, pk_lin, b1):
    """Returns nonlinear P_gm with no shot noise"""
    ZA_cleft = CLEFT(kk, pk_lin, one_loop=False, shear=False, third_order=False)
    ZA_cleft.make_ptable(nk=200)
    kgZA, pgmZA = combine_bias_terms_pk_crossmatter(ZA_cleft, b1,0,0,0,1)
    return kgZA, pgmZA


def pgg_ell(kk, pk_lin, fval, b1, sn):
    """Returns nonlinear P_gg_ell monopole, quadrupole, 
    and hexadecapole with shot noise"""
    lpt = LPT_RSD(kk,pk_lin,kIR=0.2)

    biases = [b1,0,0,0]
    cterms = [0,0,0,0]
    stoch  = [sn,0,0]
    pars   = biases + cterms + stoch

    lpt.make_pltable(f=fval, kmin=1e-3, kmax=0.5)
    kw, pw0, pw2, pw4 = lpt.combine_bias_terms_pkell(pars)

    return kw, pw0, pw2, pw4


def pgg_ell_ZA(kk, pk_lin, fval, b1):
    """Returns nonlinear P_gg_ell monopole, quadrupole, 
    and hexadecapole without shot noise"""
    lpt = LPT_RSD(kk,pk_lin,kIR=0.2)

    biases = [b1,0,0,0]
    cterms = [0,0,0,0]
    pars_ZA = biases + cterms + [0,0,0]

    lpt.make_pltable(f=fval, kmin=1e-3, kmax=0.5)
    kwZA, pw0_ZA, pw2_ZA, pw4_ZA = lpt.combine_bias_terms_pkell(pars_ZA)
    return kwZA, pw0_ZA, pw2_ZA, pw4_ZA
