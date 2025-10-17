# HEFT Simulation Budgeting
## Requirements
To use just the train/test data generating and emulator training notebooks, in addition to typical Anaconda packages, this code requires [CLASS](https://github.com/lesgourg/class_public) and [velocileptors](https://github.com/sfschen/velocileptors) (which requires [pyFFTW](https://hgomersall.github.io/pyFFTW/)). These packages can be installed as follows:
```
pip install pyFFTW
pip install -v git+https://github.com/sfschen/velocileptors
git clone https://github.com/lesgourg/class_public
cd class_public
make clean
make
```
To use other notebooks, you may need to additionally install [CCL](https://ccl.readthedocs.io/en/latest/index.html), [py-SP(k)](https://github.com/jemme07/pyspk), and [Aemulus HEFT](https://github.com/AemulusProject/aemulus_heft), which can be easily installed as follows:
```
pip install pyccl
pip install pyspk
pip install -v git+https://github.com/AemulusProject/aemulus_heft
```

## In this Repository
This repository contains the code and information used to produce figures and most of the data in (paper). If you wish to generate your own train/test data and train your own emulator, the notebooks you will need to use are **generate_training_data.ipynb** and **emulator_training**. The other notebooks produce the figures appearing in our paper. All data needed to run those notebooks is contained in the other folders in this repository. For more details on what each notebook does, click on it and read the description near the top. 

## Not in this Repository ##
The extra-large tier 2 train/test data files (1000 and 100 cosmologies, respectively) are too large to store in this repository. They can instead be accessed through [Zenodo](https://zenodo.org/records/17363645?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjRiOWY4Y2NjLWVhNTQtNDRiMi05Y2ViLTI5MTllYmIyYmYwNiIsImRhdGEiOnt9LCJyYW5kb20iOiI4ZWUwODYzMGQ4NDViNTU5NGE0ZDBkNzhiMTFiZDRkZSJ9.AX8oTxNaEpM7KXMdT8sBADY_mK-ALOi9d6Yb4HPvlXPnO5vfYJ1Z4h0vTejzTm34EHoRTKP8Sd0kDZ1JEzrJnA). The corresponding DOI is 0.5281/zenodo.17363645.
