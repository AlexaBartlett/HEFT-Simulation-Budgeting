# Emulator Errors #
## Description of Files ##
- `*_kerr.txt`: File containing 50th, 68th, 95th, and 99th percentile emulator error as a function of $k.$ The contents thus has shape $(4, N_{k}).$
- `*_stderr.txt`: File containing the 50th, 68th, 95th, and 99th percentile error for each training point. These files are not used in the notebooks in this repository.

## In this Directory ##
This directory contains `kerr` and `stderr` files for emulators trained on the following:
- Tier 1 $w_0w_a{\rm CDM}+m_{\nu}$ train/test data, full $k$ range
- Tier 2 $w_0w_a{\rm CDM}+m_{\nu}$ train/test data, full $k$ range
- Example tier 1 train/test data, to $k_{\rm max}=1 h {\rm Mpc}^{-1}$
