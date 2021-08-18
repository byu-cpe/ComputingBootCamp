---
layout: page
toc: true
title: fasm2bels
slug: fasm2bels
type: fpga_opensource
order: 6
---

## Overview

FASM2BELs (FPGA Assembly to Basic Elements of Logic) is a tool that takes FASM files, generates a new file containing techmapped Verilog (the BEL connections) and TCL commands that, if all placed into Vivado, allows for production of an identical bitstream (see the FASM2BELs README.md file below). With the BELs and the TCL commands, if fed through Vivado, an identical bitstream can be produced that would match one generated from the FASM file on its own.

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

