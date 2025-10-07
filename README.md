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
