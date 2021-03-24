---
layout: page
toc: false
title: bram-patch
lab: 1
type: fpga_opensource
order: 8
---

For Immerse 2019, Jonathan Orgill worked on a BRAM patching project.  It is a good example of how you can use the information provided by `prjxray` to manipulate bitstreams.

The prjxray-bram-patch (`XBP` for short) repo can be found at https://github.com/symbiflow/prjxray-bram-patch.  It started as a byuccl project but was eventually added to the Symbiflow project on Github.  

## Overview

As was described in the final section of the 220 Textbook (Section 19.7 for v2.0 of the textbook), when designing circuits, you can specify what contents a memory should be initalized to when the circuit begins operation.  You can find the relevant [pages here](media/meminit.pdf) (focus on the 2nd page).   This can be done for both ROM or RAM memories (in the case of a ROM the contents will not change as the circuit operates but in the case of a RAM the contents will get overwritten).  These _memory initialization contents_ become part of the bitstream and so when the FPGA is configured it will "wake up" with the memories initialized. 

Since the memory initialization contents are part of the bitstream it should be possible to use prjxray to determine where those bits are and modify them _after_ the bitstream is generated.  For systems where the implementation time takes many hours, this provides a quick way to make changes to the memory contents without having to re-implement the design.  

For example, imagine you are designing a small microcontroller or CPU and the program it is to run on bootup is located in a set of BRAMs on the FPGA.  Using this tool you can change the contents of the BRAMs (and thus the program that will be executed) without re-running Vivado to get a new bitstream.

XBP relies on a FASM file corresponding to the bitstream to be patched.  To use XBP you specify what the new memory contents should be and it will patch those into the FASM file.  The FASM file can then be converted to a bitstream and downloaded to a board.

The Github page for XBP gives instructions for its use.  It assumes you have already fully installed `prjxray`, including sourcing the necessary files to set up the environment.

## Some Things to Do
* Run the designs in the samples directory and examine the differences between the "before" and "after" FASM files.
* Create a new memory init file (maybe all 1's?) and patch one of the examples - then look to see how the FASM file changed - did it change like you expected?
* Look through the code to understand how to deal with FASM files and how convert them to/from bitstream files.

