---
layout: page
toc: true
title: Project X-Ray
slug: xray
type: fpga_opensource
order: 3
---

# Project XRAY Bootcamp

These instructions provide the "bootcamp" steps for learning about the ProjectXRAY. You can access the project on GitHub at: https://github.com/SymbiFlow/prjxray

## Big Picture

Where does Project X-Ray come from?

There is a project called [SymbiFlow](https://symbiflow.github.io/) which aims to create a completely open-source [toolchain](https://en.wikipedia.org/wiki/Toolchain) for FPGAs from various vendors (Currently Xilinx and Lattice). In order to create this toolchain, a lot of information about different FPGAs is required --i.e. the bit-stream contents and their meanings, how different FPGAs work, and how they are configured. Unfortunately, these FPGA vendors do not have documentation open to everyone on how these things work, so several projects were created in order to 
document the inner-workings of these different FPGAs.

Project X-Ray deals specifically with the [Xilinx 7 Series FPGAs](https://www.xilinx.com/support/documentation/selection-guides/7-series-product-selection-guide.pdf). This project was created in order to document the bit-stream of these FPGAs. Essentially a database has been created (and is still a work in progress) that maps out all of the elements
for these FPGAs according to the bit-stream. This allows us to correlate specific bits from somewhere in a bit-stream to specific elements on an FPGA, and also understand how these elements are configured. If we know where in the bit-stream we are finding a fault or some unexpected behavior, we can use the database created by Project X-Ray to further investigate and discover what may be happening in the device. 

## Step 1: Complete "Quickstart Guide"

Follow the “QuickStart Guide” and complete the steps to install XRAY. Note that some of these steps take some time to execute. You are encouraged to jump ahead to step 2 (documentation) while a long step is executing. There are a few extra notes with each of the steps in the quickstart guide:
  * Step 0: Before starting the quickstart guide, clone the XRAY project somewhere in your Ubuntu filespace. The directory you place it in will be named `<XRAY>` for the rest of this boot camp instruction.
  * Step 1: You should add this export command to your .bashrc file so you don't have to type this in each time. However, you should use the actual directory where Vivado is installed - it is probably in "~/Xilinx_2017.2/vivado/2017.2/settings64.sh".
  * Step 2: Run this command within the root project XRAY directory (`<XRAY>`)
  * Step 4: You should be in the prjxray directory when you do this.
  * Step 5: Go with option 1.  This will create a self-contained python environment that will not interfere with your system setup.  See below for a description of what virtual environments are all about.
  * Step 6: Run this in the `<XRAY>` directory.  Better yet, add it to your .bashrc file so it will always get executed when you start a new terminal (you can always comment it out later when you don't want to run xray).  If you do so, note that the .bashrc runs from your home directory so you will have change the path in the command to make sure it gets found...
  * Step 7: Go with option 1 (you will run option 2 later in the bootcamp)
  * Step 8: Complete this step exactly as written. This runs a single "fuzzer". If it works, you system is setup correctly. This takes a bit of time.
  * Step 9: After completing this step, open the following file in your browser: `<XRAY>/htmlgen/html/artix7/index.html` Browse through this page and its links.


## Step 2: Start Reading through XRAY documentation

Read through the [Project XRAY documentation](https://symbiflow.readthedocs.io/projects/prjxray/en/latest/). The main section to read is the section on the [Xilinx 7-series Architecture](https://symbiflow.readthedocs.io/projects/prjxray/en/latest/architecture/overview.html). You can do this while working on long compilation runs in step 1 or in step 3. The focus should be to get the big picture from the first 3 subsections of the Xilinx 7-Series Architecture part (Overview, Configuration, Bitstream Format).  Once it gets into the details of how various device features are handled you can just quickly skim.

Keep a list of questions you have in terms of terminology you don’t understand or concepts you don’t understand. Save your questions so we can create a “FAQ” for the bootcamp that answers your questions. It is important for you to list all your questions - don’t be bashful if you don’t understand any term or concept. 


## Step 3: Recreate the database (optional)
Only complete this step if your advisor has asked you to.

Go back and recreate the database (run the fuzzers). This involves Step 7, option 2 in the quickstart guide. This will take a very long time so just get the process started. While this process is running, you can go back and do plenty of reading in the XRAY documentation. Check on the process periodically to make sure it is still working and it hasn't crashed. While the fuzzers are running there are a number of things you can do to learn about the XRAY system:
  * The output stream will provide an indication on where you are in the build process. The following line demonstrates what you may see. The key here is the text "005-tilegrid" which indicates that the process is currently operating on fuzzer "005-tilegrid" (stil a long way to go)
    2020-05-14T17:10:01 - xc7a50tfgg484-1/005-tilegrid  - 1h02m: make---make---sh---make---sh---bash---vivado.sh---vivado---loader---vivado---2*[{vivado}]  
  * When a fuzzer has finished, you can enter the fuzzer directory to browse information about the fuzzer result. The fuzzers run in sequential order (using the first three digits of the fuzzer name) so you can tell which fuzzers have comleted. If the build process is currently on "005-tilegrid" then the fuzzers "000-init-db" and "001-part-yaml" have been completed. The following information is helpful to review in each fuzzer directory:
  * The file "run.xc7a50tfgg484-1.ok" is an empty file that indicates that the fuzzer has successfully completed. If this file does not exist then the fuzzer has not been completed.
  * Each fuzzer directory has a sub-directory named "logs_xc7a50tfgg484-1" that contains the output logs of the fuzzer run. The file "stdout.<date>.log" contains the output to standard out and the file "stderr.<date>.log" contains the output to standard error. It is useful to browse through these files to get a feel for what is involved running each fuzzer. You can view the real-time output generated by a fuzzer by running the "tail -f" unix command to follow the file.
  * It is useful to browse a bit in each fuzzer directory to see what types of files are there. Fuzzers often have a Makefile, Verilog files, Vivado .tcl files, a Readme.md markdown file, and Python scripts.
 
 ## Step 4: Run a fuzzer by hand

Run and Understand the CLB LUT Initialization Contents Fuzzer. In this step, you will learn the details of a single fuzzer. In particular you will run the [clb-lutinit](https://symbiflow.readthedocs.io/projects/prjxray/en/latest/db_dev_process/fuzzers/clb-lutinit.html) fuzzer. The purpose of this fuzzer is to determine where in the bitfile the LUT initialize constants are found. Review the fuzzer documentation (there is not much here!) and then run the fuzzer individually. Review the console output while the fuzzer is running.

    cd fuzzers/010-clb-lutinit
    make -j$(nproc) run

After running the fuzzer successfully, go back to the fuzzer directory and review the following files:
File | Purpose
------------ | -------------
top.v | Verilog file to use for running fuzzer. Try to figure out what this circuit is doing.
generate.tcl | Vivado .tcl file for generating bitfile


# Virtual Environments
One of the installation steps for prjxray has you create a python virtual environment (the 'make env' step).  You may not know about them - they are an important _containerization_ technology.  Once you create a python virtual environment and activate it, everything you install with "pip" will be placed into that environment and will not affect the rest of your running system.  It is a nice way to get precisely the python environment you need for a project without messing with what came with your Linux installation.

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

-----------------------------
Originally created by Ben Glines, May 2020.


