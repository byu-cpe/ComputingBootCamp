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

### Install Fasm2Bels

1. Clone the [SymbiFlow fasm2bels repo](https://github.com/SymbiFlow/symbiflow-xc-fasm2bels.git) and build (you will need Python 3.7 or above):

        git clone https://github.com/SymbiFlow/symbiflow-xc-fasm2bels.git
        cd symbiflow-xc-fasm2bels/
        make env
        make build

1. Set your `INTERCHANGE_SCHEMA_PATH` environment variable:
    
        export INTERCHANGE_SCHEMA_PATH="<your_rapidwright_path>/interchange/fpga-interchange-schema/interchange"

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



## Runing FASM2BELs

Go to:

    <bootcamp_repo>/fasm2bels

In this directory you will see a simple 16-bit adder design (*add16.v*), with an associated constraints file (*constraints.xdc*).  A bitstream has already been generated for you, and is provided as *add16.bit*.

We will now convert this bitstream back to a Verilog netlist.

1. To perform the first step of the conversion, and convert the bitstream to fasm, run (and check out the Makefile to see how this is done):

        make bit2fasm

2. You may want to inspect the produced *add16.fasm* file.

3. Next, convert the fasm file to a Verilog netlist (and check out the Makefile to see how this is done):

        make fasm2verilog


## Follow-Up Activities

**THIS FOLLOW UP ACTIVITY SECTION IS STILL UNDER CONSTRUCTION. ESTIMATED COMPLETION/FINAL PUSH FRIDAY NIGHT, SATURDAY NIGHT, or MONDAY MORNING.**



### Bringing It All Together




Using fasm2bels would be a useful activity because it would:

* It is a 2nd Symbiflow repo with its own install instructions to get them use to the idea of Symbiflow having multiples
* Provide an example of a program that uses the prjxray database
* Show them Verilog schematics and introduce Xilinx primitives - something they will have never seen before
* Help them see the complete cycle - they could go from behavioral Verilog --> Vivado --> bitstream --> FASM --> Verilog Schematic --> Vivado --> bitstream

## Learn More

* FASM2BELs Github Repository (BYU CCL Fork) - <https://github.com/byuccl/symbiflow-xc-fasm2bels>
* FASM2BELs Github Repository - <https://github.com/SymbiFlow/symbiflow-xc-fasm2bels>
* FASM2BELs Introduction - <https://github.com/SymbiFlow/symbiflow-xc-fasm2bels/blob/master/README.md>
* How to Install RapidWright - <https://www.rapidwright.io/docs/Automatic_Install.html>

