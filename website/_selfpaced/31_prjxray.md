---
layout: page
toc: true
title: Project X-Ray
slug: xray
type: fpga_opensource
order: 3
---

## Overview

[Project X-Ray](https://github.com/SymbiFlow/prjxray) is a project that documents the [Xilinx 7 Series](https://www.xilinx.com/support/documentation/selection-guides/7-series-product-selection-guide.pdf) bitstream. Essentially, Project X-Ray can build databases that map the elements (Lookup tables, interconnects, muxes, ports, etc.) for an FPGA part to their corresponding bits in the bitstream.

Project X-Ray is being created by [SymbiFlow](https://symbiflow.github.io/), which aims to create a completely open-source [toolchain](https://en.wikipedia.org/wiki/Toolchain) for FPGAs from various vendors (Currently Xilinx and Lattice). In order to create this toolchain, the bitstream needs to be generated after completing implementation. Xilinx does not have documentation open to the public on how their bitstreams are generated, so Project X-Ray aims to fill this gap.

There are many cases where such databases can be useful. For example, let's say that during radiation testing, certain bits that flip will break our design, so we want to further investigate to see why. These databases help so that it can be understood what these bits correspond to inside the FPGA i.e. whether they affect a PIP, a LUT, etc. 

## Install

Follow the [Project X-Ray quickstart guide](https://github.com/SymbiFlow/prjxray#quickstart-guide) on their GitHub repository to install Project X-Ray. The guide was written for Ubuntu 16.04, but is also known to work on Ubuntu 18.04. Any other version of Ubuntu is not guaranteed to work (The roadblock would probably Vivado 2017.2. That version is required, and other versions of Vivado will not work. It is an older version that may not work with newer versions of Ubuntu)

Here are some extra notes for each of their install steps that might be helpful:

* Step 1: Project X-Ray sometimes needs to use Vivado, so it needs to know where you have it install on your system. By default, it is installed in the `/opt/` directory, but it may be in some other place on you system. Double check where you have it installed, and then  You should add this export command to your [.bashrc file](https://www.journaldev.com/41479/bashrc-file-in-linux) so you don't have to type this in each time you start a terminal. 
* Step 2: This step downloads their directory to your system. The command they provide uses SSH to clone the directory. This probably won't be set up on your system, but you can set it up by following [these instructions](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). You can also easily clone the directory with HTTPS instead of SSH by running the following command:
```
git clone https://github.com/SymbiFlow/prjxray.git
``` 
Run either the command for SSH cloning or HTTPS cloning within the home directory. By default, you should be in the home directory. If not, just run `cd` in the terminal, and you should be there (alternatively, you can run `cd ~/`). This will create a directory called `prjxray` where the GitHub repo will then be stored. 
* Step 4: When running `make`, it will look for a file called `Makefile`. For Project X-Ray, this will be in the `prjxray` directory on the top level, so make sure you are there by running `cd ~/prjxray`
* Step 5: Go with option 1.  This will create a self-contained python virtual environment that will not interfere with your system setup.
* Step 8: Choose option 1. It is possible that your system may not even have the resources (not enough RAM) to recreate the entire database.
* Step 9: Complete this step exactly as written. This runs a single "fuzzer". If it works, you system is setup correctly. Since you downloaded the database in step 8, you don't actually have to run any of the fuzzers to start using the Project X-Ray tools.

One of the installation steps for prjxray has you create a [python virtual environment](https://byu-cpe.github.io/ComputingBootCamp/tutorials/pythonEnvs/) (the 'make env' step).  You may not know about them - they are an important _containerization_ technology.  Once you create a python virtual environment and activate it, everything you install with "pip" will be placed into that environment and will not affect the rest of your running system.  It is a nice way to get precisely the python environment you need for a project without messing with what came with your Linux installation.

The key steps are Step 5 and Step 6 from the [prjxray install steps](https://github.com/SymbiFlow/prjxray).  Once you create the environment ("env"), you need to activate it any time you are working on the project using the step:

    source settings/artix7.sh

Just remember that that is actually located in the prjxray directory you created when you did a "git clone".  So, in your .bashrc file you probably want something like this:

    source ~/prjxray/settings/artix7.sh

You will know that the virtual environment is activated since the command prompt for your Linux bash shell will have a "(env)" preceding it like this:

    (env) nelson@ubuntu:~$ 

The best way to get out of the environment is to edit your .bashrc file to not source the above .sh file, kill your terminal, and re-open a new one.  You will tell it worked if the "(env") is gone from your command prompt.

Finally, you can have as many virtual environments as you want on your machine, one for each project, for 
example.  You can customize each to what you need and can go into and out of them at will.  


For example, if you look into the file "~/prjxray/settings/artix7.sh" you will see that, besides setting a bunch of environment variables, it sources ../utils/environment.sh.  That script then, in turn, sets a bunch more environment variables but IMPORTANTLY also activates the virtual environment by doing this:

    source ${XRAY_DIR}/env/bin/activate

Thus, you start a python virtual environment by sourcing its "activate" script and you leave a python virtual environment by running the "deactivate" shell command.

## Lecture

On June 2, 2021, we had a lecture from Professor Nelson about Project X-Ray and [FASM](https://byu-cpe.github.io/ComputingBootCamp/tutorials/fasm/). The video is embeddded below.

<iframe width="800" height="600"
src="https://www.youtube.com/embed/6HGN8pQn_jA">
</iframe>

## Follow-Up Activities

Project X-Ray includes many tools, which is where you'll find out more about its capabilites. See the [FASM](https://byu-cpe.github.io/ComputingBootCamp/tutorials/fasm/), [bit2fasm](https://byu-cpe.github.io/ComputingBootCamp/tutorials/bit2fasm/), and [fasm2bels](https://byu-cpe.github.io/ComputingBootCamp/tutorials/fasm2bels/) modules to learn more. 

Below are some activities associated with the fuzzers.

### Recreate the database (optional)
Only complete this step if your advisor has asked you to.

Go back and recreate the database (run the fuzzers). This involves Step 7, option 2 in the quickstart guide. This will take a very long time so just get the process started. While this process is running, you can go back and do plenty of reading in the XRAY documentation. Check on the process periodically to make sure it is still working and it hasn't crashed. While the fuzzers are running there are a number of things you can do to learn about the XRAY system:
  * The output stream will provide an indication on where you are in the build process. The following line demonstrates what you may see. The key here is the text "005-tilegrid" which indicates that the process is currently operating on fuzzer "005-tilegrid" (stil a long way to go)
    2020-05-14T17:10:01 - xc7a50tfgg484-1/005-tilegrid  - 1h02m: make---make---sh---make---sh---bash---vivado.sh---vivado---loader---vivado---2*[{vivado}]  
  * When a fuzzer has finished, you can enter the fuzzer directory to browse information about the fuzzer result. The fuzzers run in sequential order (using the first three digits of the fuzzer name) so you can tell which fuzzers have comleted. If the build process is currently on "005-tilegrid" then the fuzzers "000-init-db" and "001-part-yaml" have been completed. The following information is helpful to review in each fuzzer directory:
  * The file "run.xc7a50tfgg484-1.ok" is an empty file that indicates that the fuzzer has successfully completed. If this file does not exist then the fuzzer has not been completed.
  * Each fuzzer directory has a sub-directory named "logs_xc7a50tfgg484-1" that contains the output logs of the fuzzer run. The file "stdout.<date>.log" contains the output to standard out and the file "stderr.<date>.log" contains the output to standard error. It is useful to browse through these files to get a feel for what is involved running each fuzzer. You can view the real-time output generated by a fuzzer by running the "tail -f" unix command to follow the file.
  * It is useful to browse a bit in each fuzzer directory to see what types of files are there. Fuzzers often have a Makefile, Verilog files, Vivado .tcl files, a Readme.md markdown file, and Python scripts.
 
### Run a fuzzer by hand

Run and Understand the CLB LUT Initialization Contents Fuzzer. In this step, you will learn the details of a single fuzzer. In particular you will run the [clb-lutinit](https://symbiflow.readthedocs.io/projects/prjxray/en/latest/db_dev_process/fuzzers/clb-lutinit.html) fuzzer. The purpose of this fuzzer is to determine where in the bitfile the LUT initialize constants are found. Review the fuzzer documentation (there is not much here!) and then run the fuzzer individually. Review the console output while the fuzzer is running.

    cd fuzzers/010-clb-lutinit
    make -j$(nproc) run

After running the fuzzer successfully, go back to the fuzzer directory and review the following files:
File | Purpose
------------ | -------------
top.v | Verilog file to use for running fuzzer. Try to figure out what this circuit is doing.
generate.tcl | Vivado .tcl file for generating bitfile

## Learn More

* SymbiFlow Website - <https://symbiflow.github.io/>
* Toolchain Wikipedia - <https://en.wikipedia.org/wiki/Toolchain>
* Project X-Ray GitHub Repository - <https://github.com/SymbiFlow/prjxray>
* Project X-Ray Documentation (Particularly the first three sections of "Xilinx 7-series Architecture": Overview, Configurdation, Bitstream Format) - <https://symbiflow.readthedocs.io/projects/prjxray/en/latest/>

