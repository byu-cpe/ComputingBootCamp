---
layout: page
toc: true
title: symbiflow-examples
slug: symbiflow-examples
type: fpga_opensource
order: 7
---

## Overview

[SymbiFlow Examples](https://github.com/symbiflow/symbiflow-examples) is one of SymbiFlow's most useful repositories because it provides and illustrates an end-to-end flow: Verilog --> Yosys/VPR --> Bitstream.

One of the goals of the SymbiFlow Project is to get a complete Verilog-to-Bitstream CAD tool flow out to users. The repository currently contains some example circuits in its `xc7/` and `eos-s3/` directories (and these are not necessarily toy circuits!)

Every module page associated with SymbiFlow ([Project X-Ray]((https://byu-cpe.github.io/ComputingBootCamp/tutorials/xray)) , [FASM](https://byu-cpe.github.io/ComputingBootCamp/tutorials/fasm/), [bit2fasm](https://byu-cpe.github.io/ComputingBootCamp/tutorials/bit2fasm/), and [fasm2bels](https://byu-cpe.github.io/ComputingBootCamp/tutorials/fasm2bels/)) have all been integral pieces in the toolchain puzzle. Now, with these examples, everything comes together to show the power of what SymbiFlow can truly do.

## Lecture

On June 4, 2021, Professor Nelson gave an overview of the various repositories inside SymbiFlow. The video is embedded below. 

<iframe width="800" height="600" allow="fullscreen" 
src="https://www.youtube.com/embed/zNZND75nQ10"> 
</iframe>

## Follow-Up Activities

There are instructions in the SymbiFlow Examples repository on how to build its sample designs manually. The process outlined is fully self-contained - you do not need anything else installed to run these designs - the instructions do it all. The best way to test it out is to simply copy the entire list of instructions and paste them into your terminal window.

### Explore the Examples

As of August 2021, the `xc7/` directory contains four example designs, the `eos-s3/` contains one.

Run all five example circuit designs in your cloned SymbiFlow Examples repo. Each folder contains a README.rst file. Start there first, follow all the instructions to the letter and run every design.

**Carefully read what is printed as the tools run.**

Once you have done that and the tests have been created, go into each directory with Verilog files in them and examine what you see. There are just a few files for each example - figure out what they do and how they correspond to the files required for a Vivado compilation.  

Also, find the .bit files generated - **if you had the right board, you could download the bitstream right to it. After all, these designs do work!**

**NOTE: As you experiment with all of the currently supported designs, try and answer these questions:**

* If I made a small change to one of the designs, how long would it take to remake it? 
* How does the output printed correspond to what I know about the Synthesis --> Implementation --> Bitstream Generation process?
* Are there any steps that seem to take an especially long time?
* From the SymbiFlow Github or Read The Docs pages, can I figure out what boards are supported? 

### Set Up the Sphinx (Optional)

An optional activity can be found in the SymbiFlow Examples README.md file. Follow the instructions under the "Building those docs" section to get the Sphinx documentation up and running. Explore it and see what is included in the `docs/build/html` directory once it has built successfully.

### Run the CI Tests (Optional)

One more optional activity can also be found in the SymbiFlow Examples README.md file. Follow the instructions under the "Running 'CI' locally" section to find and install the necessary scripts. Read through the terminal output as the CI is run.

## Learn More

* SymbiFlow Examples Github Repository - <https://github.com/symbiflow/symbiflow-examples>
* SymbiFlow Examples Documentation - <https://symbiflow-examples.readthedocs.io/en/latest/>
    * (Pay very close attention to the sections of the SymbiFlow Examples documentation, especially "Building example designs" and "Running example designs")
* SymbiFlow Examples (Open Source Libs) - <https://opensourcelibs.com/lib/symbiflow-examples>


<!-- EASTER EGG for any Future SymbiFlow Examples page editors

At the current time the board from the digital lab in our department is not supported.  But, they would very much like for it to be supported and have provided some thoughts on what needs to be done.  If you are interested, let Professor Nelson know - it could be a fun side project and the department would definitely loan you a board to use for it. -->