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

These instructions will help you get the fasm2bels repository up and running on your machine. The official install instructions on the BYU fork and the main fasm2bels repo differ slightly from the instructions below, but the extra tips will ensure fasm2bels runs properly:

Before cloning this repo, the RapidWright and capnproto-java repos must be installed first.

Follow the instructions to install RapidWright [here](https://github.com/Xilinx/RapidWright) and clone capnproto-java [here](https://github.com/capnproto/capnproto-java).

After RapidWright and capnproto-java are installed, clone the [SymbiFlow fasm2bels repo](https://github.com/SymbiFlow/symbiflow-xc-fasm2bels.git) and run the following commands:
  - `make env`: For this to be successful, python3.7 or above is required - you may have to upgrade and then change the Makefile to use the new version (same for Invoking below)
    - To get python3.7 on Ubuntu 16.04 (or above) do the following:
      - sudo apt update
      - sudo apt install software-properties-common
      - sudo add-apt-repository ppa:deadsnakes/ppa
      - sudo apt update
      - sudo apt install python3.7
    - Then, had to modify the Makefile to use python3.7 instead of python3
    - Then, modify the Makefile to use python3.7 instead of python3.
 - `make build`
 - `make test-py` - Before running, go into `.github/workflows/test.sh` and change the directory path from $GITHUB_WORKSPACE to your directory path for CAPN_PATH and INTERCHANGE_SCHEMA_PATH (fpga-interchange-schema is inside `RapidWright/interchange`). It should look something like this when completed:

`export CAPNP_PATH="/home/username/capnproto-java/compiler/src/main/schema/"`
`export INTERCHANGE_SCHEMA_PATH="/home/username/RapidWright/interchange/fpga-interchange-schema/interchange"`

Source the `test.sh` from the main fasm2bels directory (`source .github/workflows/test.sh`) and `make test-py` will run automatically. It takes a few minutes to run all 22 tests.

An `OK` should appear at the bottom of the terminal run if successful.

## Lecture

On June 4, 2021, Professor Goeders gave an overview of the FASM 2 BELs repository. The video is embedded below. 

<iframe width="800" height="600" allow="fullscreen" 
src="https://www.youtube.com/embed/58wXkBlyu-Q"> 
</iframe>

## Follow-Up Activities

**THIS FOLLOW UP ACTIVITY SECTION IS STILL UNDER CONSTRUCTION. ESTIMATED COMPLETION/FINAL PUSH FRIDAY NIGHT, SATURDAY NIGHT, or MONDAY MORNING.**

### Run FASM2BELs

In the BYU FASM2BELs repo `README.md` file, it describes how to run a test of fasm2bels once it has been fully installed... continue this once all fasm2bels problems are resolved 


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

