# Training Data #
## Contents of this Directory ##
- `example_data`: a smaller example set of training data (100 cosmologies) over the tier 2 parameter space
- `pmm_w0wamnu_noisy_ZCV_tier1`: large (400 cosmologies) base training set for $w_0w_a{\rm CDM}+m_\nu$ tier 1. Gaussian noise was added in the data generation process, and ZCV was used to reduce the low- $k$ variance for realism. 
- `pmm_w0wamnu_noisy_ZCV_tier1`: the same as `pmm_w0wamnu_noisy_ZCV_tier1`, but for tier 2 bounds. This is a smaller training set, with only 200 cosmologies. 

## Sub-directory Structure ##
Within each training set directory, there are several files. The testing data directory has the same structure.
- `info.txt`: Parameters used to generate the training data: $V_{\rm obs}$ $(h^{-3}{\rm Mpc}^3)$, $\Delta k$ $(h{\rm Mpc}^{-1})$, ZCV (true for yes, false for no)
- `k_out.txt`: contains the ks corresponding to all powerspectra (aside from `pk_lin.npy`, see below). By default, $k$ values are expressed in $h\,{\rm Mpc}^{-1}$.
- `params.txt`: File containing cosmologies in this training set. The number of rows should equal the number of cosmologies used to create the training data (not including the header)
- `pk_1L.npy`: File containing 1-loop power spectra computed using velocileptors RKECLEFT. Once read in using numpy, the result is a 3D array of shape ($N_{\rm cosmo}, N_{z}, N_{k}$). For all training sets here, $N_z=30$ and $N_k=700$.
- `pk_hmcode.npy`: File containing nonlinear spectra computed using HMcode. Once read in using numpy, the result is a 3D array of shape ($N_{\rm cosmo}, N_{z}, N_{k}$). 
- `pk_lin.npy`: File containing linear power spectra computed using CLASS. Once read in using numpy, the result is a 3D array of shape ($N_{\rm cosmo}, N_{z}, N_{k}$). *Important*: note that the $k$ s corresponding to these $P(k)$ s are not those in `k_out.txt`. The linear power spectra are computed over a larger $k$ -range. $k_{\rm lin}$ is an array of 700 $k$ values logarithmically spaced between $10^{-3} h {\rm Mpc}^{-1}$ and $10 h{\rm Mpc}^{-1}$.
- `sigma_8.txt`: File containing $\sigma_8(z)$ for all cosmologies and redshifts in datset. The shape of the array once read in is $(N_{\rm cosmo}, N_{z})$.
