---
layout: page
toc: true
title: prjxray Install
lab: 1
---

Installing prjxray is fairly simple and is carefully documented at Github's symbiflow/prjxray website (scroll down to the README.md section).

However, there should be a Step 0 to the installation instructions there - you need to initially get prjxray on your machine.    You do that with:

    git clone https://github.com/symbiflow/prjxray

This will create a "prjxray" directory wherever you executed the above command (best to execute it in your home directory).

## Virtual Environments
One of the installation steps for prjxray has you create a python virtual environment.  You may not know about them - they are an important _containerization_ technology.  Once you create a python virtual environment and activate it, everything you install with "pip" will be placed into that environment and will not affect the rest of your running system.  It is a nice way to get precisely the python environment you need for a project without messing with what came with your Linux installation.

The key steps are Step 5 and Step 6 from the [prjxray install steps](https://github.com/SymbiFlow/prjxray).  Once you create the environment ("env"), you need to activate it any time you are working on the project using the step:

    source settings/artix7.sh

Just remember that that is actually located in the prjxray directory you created when you did a "git clone".  So, in your .bashrc file you probably want something like this:

    source ~/prjxray/settings/artix7.sh

You will know that the virtual environment is activated since the command prompt for your Linux bash shell will have a "(env)" preceding it like this:

    (env) nelson@ubuntu:~$ 

If you later want to deactivate the virtual environment and just work in the regular Linux environment you can execute the command:

    deactivate

You will know it worked when the environment name "(env)" disappears from the command prompt.

Finally, you can have as many virtual environments as you want on your machine, one for each project, for example.  You can customize each to what you need and can go into and out of them at will.  

For example, if you look into the file "~/prjxray/settings/artix7.sh" you will see that, besides setting a bunch of environment variables, it sources ../utils/environment.sh.  That script then, in turn, sets a bunch more environment variables but IMPORTANTLY also activates the virtual environment by doing this:

    source ${XRAY_DIR}/env/bin/activate

Thus, you start a python virtual environment by sourcing its "activate" script and you leave a python virtual environment by running the "deactivate" shell command.


