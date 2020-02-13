# REPL
A REPL (say it, “REP-UL”) is an interactive way to talk to your computer in Python. To make this work, the computer does four things:

- Read the user input (your Python commands).
- Evaluate your code (to work out what you mean).
- Print any results (so you can see the computer’s response).
- Loop back to step 1 (to continue the conversation).
The term “REPL” is an acronym for Read, Evaluate, Print and Loop because that’s precisely what the computer does..!. Generally launched by typing `python` or `python3` from shell/command line

# IPython vs. Jupyter vs. Jupyterlab vs. Jupyterhub

- IPython (Interactive Python) is a command shell for interactive computing in multiple programming languages, originally developed for the Python programming language, that offers introspection, rich media, shell syntax, tab completion, and history. IPython itself is ultimately a python codebase and library to be installed
- Basically all 3 are presentation layers
- Jupyter is the evolution from IPython. It is a REPL interface over web, with additional intellisense.
- JupyterLab is Jupyter’s Next-Generation Notebook Interface
- By default IPython kernel is available when Jupyter is installed, however if other kernels (julia, R etc.) are required, we have to explictly install the kernel for e.g. IJulia for Julia (assuming Julia runtime is available and [IJulia](https://github.com/JuliaLang/IJulia.jl) finds it when installed). To avoid manually configuring kernels, various language runtimes and its packages etc. is why Anaconda exists
- JupyterHub brings the power of notebooks to groups of users. It gives users access to computational environments and resources without burdening the users with installation and maintenance tasks. Users - including students, researchers, and data scientists - can get their work done in their own workspaces on shared resources which can be managed efficiently by system administrators.

# Anaconda vs. Miniconda vs. Conda

- Many scientific packages require a specific version of Python to run. It’s difficult to keep various Python installations on one computer from interacting and breaking, and harder to keep them up-to-date. 
- Anaconda Distribution makes management of multiple Python versions on one computer easier, and provides a large collection of highly optimized, commonly used data science libraries to get you started faster.
- An easy-to-install collection of high performance Python libraries along with Conda, a tool for managing packages and environments. Beyond the collection of open source packages in the Anaconda installer, you can use Conda to install over 1.5k packages (including the R language) from the Anaconda public repository and more than 20k packages from community channels, such as Conda-forge and bioconda.
- Basically Anaconda is like RVM (ruby version manager) , that can manage multiple python environments and other kernels like R, Julia and more as it evolves. [Anaconda Cheat Sheet](https://docs.anaconda.com/_downloads/9ee215ff15fde24bf01791d719084950/Anaconda-Starter-Guide.pdf)
- Miniconda is Conda and its dependencies. With Miniconda, you can build your environments from scratch by installing only the packages needed to run the Conda command. It’s a much smaller installer, typically used with an active internet connection
- [Managing Environments with Conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- [Managing Python with Conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-python.html)
- [Conda Cheat Sheet](https://conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)


# Anaconda vs. Jupyter

Anaconda is package manager. Jupyter is a presentation layer. Anaconda tries to solve the dependency hell in python—where different projects have different dependency versions—so as to not make different project dependencies require different versions, which may interfere with each other.

# conda vs pip

Pip installs Python packages whereas conda installs packages which may contain software written in any language. For example, before using pip, a Python interpreter must be installed via a system package manager or by downloading and running an installer. Conda on the other hand can install Python packages as well as the Python interpreter directly.  

Conda is a cross platform package and environment manager that installs and manages conda packages from the Anaconda repository as well as from the Anaconda Cloud. Conda packages are binaries. There is never a need to have compilers available to install them. Additionally conda packages are not limited to Python software. They may also contain C or C++ libraries, R packages or any other software.  

Another key difference between the two tools is that conda has the ability to create isolated environments that can contain different versions of Python and/or the packages installed in them. This can be extremely useful when working with data science tools as different tools may contain conflicting requirements which could prevent them all being installed into a single environment. Pip has no built in support for environments but rather depends on other tools like virtualenv or venv to create isolated environments
