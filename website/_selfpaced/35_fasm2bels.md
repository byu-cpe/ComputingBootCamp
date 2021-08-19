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

<!--capnproto java has to be installed first, then rapidwright-->

**The FASM2BELS Installation instructions are currently under construction.**

## Lecture

On June 4, 2021, Professor Goeders gave an overview of the FASM 2 BELs repository. The video is embedded below. 

<iframe width="800" height="600" allow="fullscreen" 
src="https://www.youtube.com/embed/58wXkBlyu-Q"> 
</iframe>

## Follow-Up Activities

### Bringing It All Together

**Follow up activity is under construction**

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

