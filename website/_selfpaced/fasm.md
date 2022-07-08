---
layout: page
toc: true
title: FASM (FPGA Assembly)
slug: fasm
type: fpga_opensource
order: 4
---

## Overview

FASM (FPGA Assembly) is a textual representation of a bitstream. By assigning a symbolic name to each configurable thing in the FPGA, the resulting FASM file shows what features are specifically configured "on". These files provide an easy way to write programs that manipulate bitstreams. Modifying a textual FASM file is far easier than trying to modify a binary bitstream.

## Install

Follow the instructions for installing [Project X-Ray](https://byu-cpe.github.io/ComputingBootCamp/tutorials/xray/). 

## Lecture

On June 2, 2021, we had a lecture from Professor Nelson about [Project X-Ray](https://byu-cpe.github.io/ComputingBootCamp/tutorials/xray/) and FASM. The video is embeddded below.

<iframe width="800" height="600" allow="fullscreen" 
src="https://www.youtube.com/embed/6HGN8pQn_jA">
</iframe>

## Follow-Up Activities

### Make a FASM File

The best way to understand the inner workings of a FASM file is to generate one through the FASM tools in Project X-Ray. [Bit2Fasm](https://byu-cpe.github.io/ComputingBootCamp/tutorials/bit2fasm/) is one of these tools, but it will be explained in greater depth in the next module. 

To create a FASM file, you first need to generate a bitstream from a design of your choice. The simplest one you can make in Vivado is a 2-input AND gate, so for this example, that design will be referenced.

* Generate a bitstream for a design using Vivado. Any version used to make your design should be satisfactory. Since Project X-Ray cannot handle all FPGA devices, you will have to use this specific part: <!---`xc7a50tfgg484-1`-->`xc7a100tfgg676-1`.

* If you don't have your top level ports mapped to physical pins, you will likely get Vivado errors. Below is some code you can use in your .tcl script to resolve the errors. These TCL commands set the IOB voltages and also tell Vivado to be happy with unconstrained pins.

```
set_property CFGBVS VCCO [current_design]
set_property CONFIG_VOLTAGE 3.3 [current_design]
set_property BITSTREAM.GENERAL.PERFRAMECRC YES [current_design]
set_property BITSTREAM.General.UnconstrainedPins {Allow} [current_design]
```

* After creating the bitstream, find it and move it from wherever it was stored on your computer into your main `~/prjxray` directory.

* Run the following command (substituting "andgate" for whatever your design is named if applicable): `$XRAY_BIT2FASM andgate.bit > andgate.fasm`.

If successful, your resulting FASM file should appear just below your bit file and should not be empty. 

### Examine a FASM File

Now that the FASM file has been created, it can be examined. In this activity, there are several suggestions below on how to parse through the file efficiently. Again, the 2-input AND gate will be the design being referenced, so adjust the instructions accordingly if your design differs.

* Open the FASM file. Can you find the LUT that implements the 2-input AND gate? There are a number of reasons why the LUT INIT values may not be what you expect.

    * The most common reason is the Vivado router will often rearrange the pin ordering on a LUT so it is easier to route signals to the LUT. If it does this, that is equivalent to changing the order of the input columns in the truth table the LUT is implementing. This means it also has to rearrange the ordering of the rows in the truth table to match. Can you tell if that was done here?

    * The second most common reason is that a 6-input LUT in Artix7 is really two 5-input LUTs which share all their inputs. They then have a MUX on their outputs which is controlled by the 6th input. The tools may choose to use the 6-LUT for a function or it may choose to treat it like two 5-LUTs and use both of its outputs.  If you look at the [diagram for a SLICEL](https://www.xilinx.com/support/documentation/user_guides/ug474_7Series_CLB.pdf) in the Xilinx documentation, you will see that the LUTs have **two** outputs. Those are the outputs of the two 5-LUTs. However, if the tools choose to treat it as a single big LUT, then it uses the **O6** output and ignores the **O5** output.

* Repeat the above for other kinds of gates.

* Do the same with counters, shift registers, and various types of memories. Look into the the FASM file further to determine how LUTs, flip flops, and BRAMs are represented.

    * **Please note**: Unless your memory is large enough, the tools will build the memory from flip flops or LUTRAMs instead of BRAMs. If you want to know how to force the tools to use BRAM instead, pull down the Github [SymbiFlow/prjxray-bram-patch](https://github.com/SymbiFlow/prjxray-bram-patch) Project and look at the Verilog files in the "samples" directory. They each have a directive in them that forces Vivado to use BRAMs, even if the memory they implement is small.

**Hold on to the FASM file you created during this activity. It will be essential for the activities on the bit2fasm and FASM2BELs module pages.**

## Learn More

* FASM GitHub Repository - <https://github.com/SymbiFlow/fasm>
* FASM Documentation - <https://fasm.readthedocs.io/en/latest/>
* FASM Output Support - <https://docs.verilogtorouting.org/en/latest/utils/fasm/>
* SLICEL Diagram (Figure 2-4, Page 20) - <https://www.xilinx.com/support/documentation/user_guides/ug474_7Series_CLB.pdf>

