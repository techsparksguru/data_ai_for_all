# New Kernel(s)
Often you would want to use a virtualenv and not use system python to keep things separated and clean on your machine. The list of all possible kernels (depending on your jupyter version) are listed [here](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels). Kernel Zero is IPython, which you can get through ipykernel, and is still a dependency of jupyter.  

# Virtualenv
If you want jupyter to refer to the virtualenv environment and NOT system python, then do the following  

- `jupyter kernelspec list` - List the available kernels first
- From the project directory, create a virtualenv as you would always `virtualenv venv --python=$(which python3)`
- `source venv/bin/activate` - activate your python environment
- `pip install jupyter` - This will install jupyter in your venv
- `ipython kernel install --name "venv" --user` - This will create a new kernel in jupyter's managed folders. For e.g. on mac it creates `~/Library/Jupyter/kernels/venv`
- Now launch `jupyter lab` and then Kernels > Change Kernel. venv will be listed there. From here on, whatever libraries you install in venv, will be available to the notebook that uses this kernel
- You can execute `jupyter kernelspec list` to see the location of the kernel. From there you can modify `kernel.json` file for more changes

# Navigation
I tend to use most of the below

## Add a cell above current focused cell
`Esc a` - a stands for above
`Esc b` - b stands for below

## Auto complete

`tab` - for autocomplete
`shift + tab` - tool tip. Very useful in writing code and calling API/functions

## Run

`Shift + Enter` - Run current cell
`Ctrl + Enter` - Run all selected cells

# Magic Functions


    

    