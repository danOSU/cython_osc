# cython_osc
To run the cython in OSC first need to install cython.
Easiest way is to create a conda environment.

First load conda module

> module load python/3.6-conda5.2

Create conda env

> module create -name cython_env

Get cython and numpy

> conda install cython

> pip install numpy

Now invoke the conda environment

> conda activate cython_env

Now compile the cython code to calculate sin of a five dimensional array.

> python setup.py build_ext --inplace

Change the credentials in submit script accordingly and run

> sbatch submit

This should give a slurm output file similar to what you find in the repo. 
