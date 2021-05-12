---
layout: page
toc: true
title: Python Packages/Environments
slug: pythonEnvs
type: development
order: 7
---


# Installing Python Versions and Creating Environments for Them in Ubuntu
These instructions were done for an Ubuntu 16.04 system.  They will work for later versions.  The original system these instructions were created for and tested on contained python=2.7.12 and python3=3.5.2 as the *system python* installation (and no other versions of python were installed).  

Before proceeding carefully consider the goals of what we are trying to achieve:
- We do not want to disturb or touch the *system python* installation since, presumably, parts of the O/S require it *as-is*.  And, if this is a multi-user system, other users won't want us messing with the system python.
- We want to be able to install as many different python versions as desired on the system for our own use.
- We want to create *sand-boxed* virtual environments for running python.  That is, each virtual environment will have its own version of python installed and its own custom set of python modules added to it.  In this way a given environment is totally isolated from the system python and from each other.

There are two ways to do this: using python's `venv` module or using `Conda`.  They will be covered in that order.  There are advantages and disadvantages to each.

# Using `venv`

First, set up a new python version on your machine (you can specify any version you want, we will use 3.9):
```
# Set up a pointer to the repo where you will get python from and some needed packages
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa

# Now install python plus the correct the venv module for that version of python
sudo apt update
sudo apt install python3.9 -y
sudo apt-get install python3.9-venv -y
```
At this point you now have an installation of python3.9 alongside the system one in `/usr/bin` (go look).  But, following this methodology you will only use it for one task - to create a new virtual environment as shown below.   After that, you will always use python from within a virtual environment.

Now, create a virtual environment (a `venv`) based on this python  version rather than the system one:
```
# Create a virtual environment named myvenv using python3.9
python3.9 -m venv ~/myvenv
```

- You now have a self-contained python environment in `~/myvenv`
- In `~/myvenv/bin` there are links for python, python3, python3.9, pip, and pip3.
- You activate the environment by doing: `source ~/myvenv/bin/activate`
    - It puts the environment name in the bash shell prompt text to let you know it is active.
    - It changes your PATH variable to run the python in `~/myvenv/bin` instead of the system one. 
    - These python programs in `~/myvenv/bin` are simply symbolic links to the ones in `/usr/bin`.
    - Both `python` and `python3` map to python3.9.  Both `pip` and `pip3` map to a `pip` suitable for use with python3.9.
- You deactivate the environment by typing `deactivate` in the shell.
    - When you do so it returns your PATH to point to the system python
- When an environment is activated, you can install things into it using `pip`.  
- You could create some aliases in your .bashrc to make it easier to activate and deactivate:
```
alias myvenv='source ~/myvenv/bin/activate'
alias de='deactivate'
```
## Discussion of the `venv` Approach
- The `venv` module is in all python distributions since python 3.3 according to the web so this will work for all versions after that.    So, you need not install any 3rd party software to use `venv`.  
- The instructions above have you install new versions of python on your system in `/usr/bin` alongside the system python.  As a result, you will need `sudo` privileges to install these.
- With the `venv` approach the virtual environments can be located anywhere in the file system you want (unlike with some other approaches where they are all gathered into one place - both a plus and a minus).
- To remove a `venv` environment you simply remove the directory: `rm -rf ~/myvenv` and the environment and everything you have installed into it using `pip` are gone.
- When you run `pip install somePackage` the location it searches for somePackage to install is at PyPI.org - the Python Package Index site.  That is not true for some other approaches which maintain their own distriutions of python and its packages.
- This is the lightest-weight approach for python virtual environments of those we use.
- A caution - there is an alphabet-soup mess of alternate approaches that have been proposed and used in the past that you will see on the web.  Be careful - the names overlap and can easily confuse you - `virtualenv`, `virtualenvwrapper`, `pipenv`, `pyenv`, `pyvenv`, ...  To reiterate - the approach described above uses ONLY the `venv` module built into python to do its work, and does not use any of those others.  
- A possible shortcoming of the `venv` approach is that there is no real environment manager.  As mentioned, environments can live anywhere - there is no central repo or controller for your environments; there is no way to list them or manage them.  You just remember where they are to activate them.  
- As a result it is simple and super easy to use, but other approaches do provide some capabilities to help manage your environments if that is deemed important.
    - One is `pyenv` a github project you can download and build.  When it installs a new python version for an environment on your machine it compiles it from sources.  It then provides facilities to manage your environments and make it easy to switch between them.  It may be useful or it may be overkill, depending on what you need.
    - Another is `conda`, which will be covered next so keep reading.

# Conda
`Conda` was developed by the developers of `numpy`.  The web suggests it was done to solve problems that python, venv, and pip alone could not handle.  And, it works with other languages besides python, something the `numpy` developers thought important.  

It is claimed to be a more full-featured containerization technology compared to `venv` in that nothing is shared, nothing is installed into system areas on your machine but everything lives in the environments themselves. And, it can containerize things other than python installations. 

To get and install Conda:
```
# Get a copy of the conda installer
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Install conda, type yes to all questions (even the ones with No as the default answer).  This will modify .bashrc for conda usage.
bash Miniconda3-latest-Linux-x86_64.sh
```
After doing the above you should restart your bash console so the changes to your `.bashrc` file can take effect.

Now, you can create environments like this:
```
# Make new environment and you are ready
conda create -n condaenv python=3.9
```

- You can activate your new environment at any time using: `conda activate condaenv`
- You deactivate it with `deactivate` (like with `venv`)
- Conda, by default, will autostart a `base` environment which is not needed for our use 
    - You can prevent this base environment from activating by typing this in the console:  `conda config --set auto_activate_base false`
- According to the documentation, the preferred method to install packages is to use `conda install pkgName` instead of `pip install pkgName`.  
    - Many people just use `pip`, however.
    - There are differences between the two but the web suggests they are minor for basic usage.
        - For example, some on the web have pointed out that mixing `pip install` and `conda install` in an environment as you add packages can cause problems in that `conda install` doesn't know what `pip install` has installed.

- As above, you could create aliases to save typing: 
```
alias cac='conda activate'
alias cde='conda deactivate'
alias cel='conda env list'
```
- With these, you would activate the above environment by typing `cac condaenv`.
- As the alias above shows, you can list the environments you have with `conda env list`.
- You can remove an environment by typing `conda env remove -n condaenv`

## Discussion of the `Conda` Approach
- At this point you have not touched any system files, everything that has been installed is inside  `~/miniconda3/envs/condaenv`.  
- You therefore don't need `sudo`
- There is no need for a particular version of python to be already installed in `/usr/bin`.  `Conda` installs a fresh copy from its repo.
- The 'user-space-only' nature of `Conda` is useful for avoiding side effects in the rest of your system.  And, such an approach is required for multi-user systems where you may not have admin privileges.
- The environments it creates are a bit more isolated from one another and from the system than with `venv`.  
- When you create an environment, you can specify the packages to be initially installed right in the create command: `conda create -n condaenv python=3.9 pandas matplotlib`.
- As said above, `conda` can manage other things besides python packages.
- According to the web, its dependency management capabilities are superior to pip's and is able to resolve complex dependencies that pip cannot.  It is unclear how true and/or important that claim is.
- As mentioned above, `conda` provides management capabilities for your environments since they are all located in `~/miniconda3/envs`.  The `conda env list` command is just one of many commands it provides.  
- Finally, note that `conda` maintains its own python distribution instead of using PyPI.  That is generally not a problem, however.

# What to Choose?
## Venv
+: Uses built-in python functionality exclusively.

-: Requires installing python distributions into the system directories using `sudo apt install`. 

-: Only manages python packages

+/-: Can put virtual environment into any directory

## Conda
-: Requires installing external software using `wget`

+: Everything (conda itself, python distributions, python packages) is installed into user directories - nothing placed into system directories - no need to use `sudo`

+: Installing a new version of python, creating an environment that uses that, and installing initial packages is a one-liner.

+/-: Puts virtual envronments into standard shared place and so can provide environment management commands

# Self-Paced Learning Activities
## Experiment with `venv`
    - Create an environment called `env1` using the default system python
    - Activate it, start up python to verify the version being used, then deactivate it.
    - Install a new python version into your system (maybe use 3.9?)
    - Create an environment called `env2` using that python version
    - Create aliases in your `.bashrc` file to activate and deactivate these.
    - Install `pandas` and `matplotlib` into `env1` after activating it using `pip install`.  
        - Then, activate `env1`, start a python REPL, and note the python version being used.
        - In the REPL, import pandas and import matplotlib.  Note that they exist (you get no errors).
    - Deactivate `env1`
    - Activate `env2`, start the REPL, and try to import pandas and note that you get an error.  This is because the pandas you installed above was sand-boxed into `env1` and this environment cannot see it.
    - Deactivate `env2` and then remove it (see above for instructions on how to delete a `venv` environment.
    - Rename the directory `env1` to be something else.  Verify that you can still activate it as long as you use the right path.
    - Remove `env1`.

## Experiment with `Conda`
    - Repeat the above steps but using `Conda`. 
    - Call your environments `cenv1` and `cenv2`.  When you create each just specify a python version to use without first installing any python into your system.
    - When you create `cenv1` specify you want to install `pandas` in the `conda create` command itself (see above).  Then, once you have activated `cenv1` use `conda install` to add `matplotlib` to the environment.
    - As above, experiment to understand how packages added to `cenv1` are not visible when in `cenv2`.
    - Use aliases to make it easy to activate and deactivate environments.  In this case you need not make an alias for each environment due to the structure of the commands.
    - Use `conda env list` to see what it knows about your environments.  Use `conda env remove` to remove `cenv1`.  
    - Experiment to see what you can do with `cenv2`.  Can you rename it?  What else can you do with it?

## Saving and Re-creating Environments
Both `venv` and `Conda` provide mechanisms to freeze an environment (create a listing of the things you have installed in them in a file).  You can then use that file as the template to perfectly re-create that environment again later.

For both environment methods, figure out how to do that and experiment with it.  Can you think of where this might be useful?



