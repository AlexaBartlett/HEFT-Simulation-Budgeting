# Abacus Spectra #
This directory contains measurements of various power spectra from the base [AbacusSummit](https://abacussummit.readthedocs.io/en/latest/simulations.html) boxes. The contents of this directory are described below:

- `Pmm/`: Matter power spectrum measurements from 13 boxes. The two columns correspond to $k, P(k)$. The "ph0XX" in the file names corresponds to an individual simulation.
- `ZD_ZD/`: Zel'dovich approximation power spectrum measurements from 10 boxes. As above, the two columns correspond to $k, P(k),$ and the "ph0XX" in the file names corresponds to an individual simulation.
- `ZeNBu_pred_cross.txt`: Analytic predictions for the ZA cross-spectrum from [ZeNBu](https://github.com/sfschen/ZeNBu)
- `pk_000_gm.txt`: Measured $P_{gm}(k)$ for AbacusSummit base box 000
- `pk_000_gm_zcv.txt`: Measured $P_{gm}(k)$ for AbacusSummit base box 000 with ZCV variance reduction applied
- `pk_gm_avg.txt`: Mean $P_{gm}(k)$ measured from 10 AbacusSummit base boxes
- `pk_gm_errs.txt`: Standard deviation of $P_{gm}(k)$ measured from 10 AbacusSummit base boxes
- `pk_gg_abacus.txt`: Average of ZCV-variance-reduced $P_{gg}(k)$ measured from all 25 base AbacusSummit boxes. This is the $P_{gg}(k)$ used for the HEFT bias fits.
- `pk_gm_abacus.txt`: Average of ZCV-variance-reduced $P_{gg}(k)$ measured from all 25 base AbacusSummit boxes. This is the $P_{gg}(k)$ used for the HEFT bias fits.
