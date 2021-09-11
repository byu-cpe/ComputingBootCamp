---
layout: page
toc: true
title: fasm2bels
slug: fasm2bels
type: fpga_opensource
order: 6
---

## Overview

"fasm2bels [(FPGA Assembly to Basic Elements of Logic)] is a tool designed to take a FASM file into Vivado. It does this by generating a file describing the BEL connections (techmapped Verilog) and TCL commands for Vivado which lock the BEL placements. This makes it possible to perform simulation and analysis of a FASM file inside Vivado.

In the absence of bugs, it is expected that after consuming the BEL connections and TCL constraints Vivado will produce a bitstream identical to the bitstream the FASM file would generate." (see the FASM2BELs README.md file below)

## Install

### Install Prerequisite Tools

Before you begin, make sure you have Python3.7 or later, and the python3-virtualenv package installed.

1. Follow the instructions to install RapidWright [here](https://github.com/Xilinx/RapidWright)

        wget http://www.rapidwright.io/docs/_downloads/rapidwright-installer.jar
        java -jar rapidwright-installer.jar -t
        source rapidwright.sh
        cd RapidWright

1. Install capnproto (<https://capnproto.org/>):

        cd /tmp && curl -O https://capnproto.org/capnproto-c++-0.8.0.tar.gz
        cd /tmp && tar zxf capnproto-c++-0.8.0.tar.gz
        cd /tmp/capnproto-c++-0.8.0 && ./configure
        cd /tmp/capnproto-c++-0.8.0 && make -j6 check
        cd /tmp/capnproto-c++-0.8.0 && sudo make install

1.  Install capnproto-java (<https://github.com/capnproto/capnproto-java>).

        cd /tmp && git clone https://github.com/capnproto/capnproto-java
        cd /tmp/capnproto-java && make
        cd /tmp/capnproto-java && sudo make install

1. Build the Interchange Scheme

        cd <your_rapidwright_path>/interchange
        make

### Install FASM2BELs

1. Clone the [SymbiFlow Fasm2bels repo](https://github.com/SymbiFlow/symbiflow-xc-fasm2bels.git) and build (you will need Python 3.7 or above):

        git clone https://github.com/SymbiFlow/symbiflow-xc-fasm2bels.git
        cd symbiflow-xc-fasm2bels/
        make env
        make build

1. Set your `INTERCHANGE_SCHEMA_PATH` environment variable:
    
        export INTERCHANGE_SCHEMA_PATH="<absolute path to your_rapidwright_directory>/interchange/fpga-interchange-schema/interchange"

 1. Run the fasm2bels tests:
 
        make test-py

    If this works correctly, you should see something like this at the end of the output:

        Ran 22 tests in 145.281s

        OK
    

## Lecture

On June 4, 2021, Professor Goeders gave an overview of the FASM 2 BELs repository. The video is embedded below. 

<iframe width="800" height="600" allow="fullscreen" 
src="https://www.youtube.com/embed/58wXkBlyu-Q"> 
</iframe>


## Follow-Up Activities

### Running FASM2BELs

Go to your local BYU Computing Boot Camp repository (or [clone it](https://github.com/byu-cpe/ComputingBootCamp.git) if you haven't already):

    cd <bootcamp_repo>/fasm2bels

In this directory you will see many files. We will focus on the add16 files for this activity. There is a simple 16-bit adder design (`add16.v`) with an associated constraints file (`constraints.xdc`). A bitstream has already been generated for you, and is provided as `add16.bit`.

Before running the instructions below, make sure you modify the Makefile to route the FASM2BELS_PATH variable to your local fasm2bels path:

`FASM2BELS_PATH=/home/username/symbiflow-xc-fasm2bels`

We will now convert this bitstream back to a Verilog netlist.

1. To perform the first step of the conversion, and convert the bitstream to a fasm file, run the following (and check out the Makefile to see how this is done):

        make bit2fasm

2. You may want to pause and inspect the produced `add16.fasm` file.

3. Next, convert the fasm file to a Verilog netlist by running the following (and check out the Makefile to see how this is done):

        make fasm2verilog


A fasm file, a reversed Verilog file, and an output.xdc file should have been produced from the steps above. 

**The final step is to open a new project in Vivado (make sure the part matches the Makefile), import the `output.xdc` and `reversed.v` files, synthesize, implement, and generate the bitstream. After this process is complete, if you took this new bitstream and compared it with the `add16.bit` file, they would be identical!**


### Bringing It All Together

Now that you have run fasm2bels successfully and gotten an identical bitstream from Vivado successfully, it is time to bring it all together. On the FASM page, you should've generated a fasm file from a 2-input AND gate design and kept that handy for this activity. Move your fasm file, your original andgate.bit file, and your Vivado constraints file into your `bootcamp/fasm2bels` directory.

Modify the appropriate Makefile variables to reflect the newly imported files. Then, follow the same steps as above (but skip Steps 1 and 2 since you already have the fasm file) and run Step 3 to make the reversed Verilog and output.xdc files. Finally, repeat the same last step as before and put those two files into Vivado to produce the identical bitstream!

**Repeat this with the cnt design files already in the folder and any other designs of your choice to become familiar with all fasm2bels has to offer.**


## Learn More

* FASM2BELs Github Repository (BYU CCL Fork) - <https://github.com/byuccl/symbiflow-xc-fasm2bels>
* FASM2BELs Github Repository - <https://github.com/SymbiFlow/symbiflow-xc-fasm2bels>
* FASM2BELs README.md - <https://github.com/SymbiFlow/symbiflow-xc-fasm2bels/blob/master/README.md>
* How to Install RapidWright - <https://www.rapidwright.io/docs/Automatic_Install.html>

