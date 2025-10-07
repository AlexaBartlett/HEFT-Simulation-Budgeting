# Results #
Within each sub-directory here, each corresponding to one sub-section in (will link paper), are the following files:
-  `tier1_results_ktrunc_kerr_full.txt`: Tier 1 emulator error for the number of simulations indicated in the paper. The shape of the loaded array should be (4, $N_k$). The 4 rows correspond to the 50th, 68th, 95th, and 99th percentile errors.
-  `tier2_results_ktrunc_kerr_full.txt`: Tier 2 emulator error for the number of simulations indicated in the paper. Again,  the shape of the loaded array should be (4, $N_k$). The 4 rows correspond to the 50th, 68th, 95th, and 99th percentile errors.

There may be additional files if the emulator was (re)trained over a truncated $k$-range. In this case, the file name will include something like, e.g., `kmaxp6` if the $k_{\rm max}$ used was $0.6h/{\rm Mpc}$. The shapes of the loaded arrays should be the same as above.
