---
layout: page
toc: true
title: Xilinx 7 Series FPGA Deep Dive
slug: xilinx_deep_dive
type: fpga_commercial
order: 3
---

# Introduction
One of the biggest challenges new research students faced is actually understanding what is in a real FPGA.  Prof. Goeders gave a talk earlier this week where he went through the features of typical FPGAs, similar to the 220 textbook's treatment.  He covered LUTs, flip flops, routing, wiring channels, etc. But, he did it in the context of generic FPGA technology.

In this self-paced activity the purpose is for you to look deeply "under the hood" to see what is in a real FPGA, specific a series 7 Artix part from Xilinx.

The major concepts you are to become familiar with include the following:
- How the FPGA contains a 2D array of tiles and what the major groups of tiles are (logic interconnect, memory, arithmetic, I/O, clocking, ...).
- How each tile contains one or more sites and what typical sites are (slices, memories, ...).
- That tiles have wires and PIPs which connect the wires.
- That sites have pins where signals go into and out of the sites.
- That sites contain BELs such as LUTs, flip flops, and routing MUXes.
- That LUTs contain configurable properties such as configuration strings, that flip flops have configurable properties to make them rising-edge vs. falling-edge triggered, etc.

In addition, you will become familiar with the extensive documentation Xilinx has provided on how to take advantage of the many special-purpose functions built into FPGAs such as dense memories, arithmetic units, different I/O capabilities, clock generation and management modules, etc. 

The hope is that you will have 10x the understanding of what is in an FPGA than you previously had, and you will be more able to use those features to your advantage when you do design.

# CLB's and Slices
A CLB (configurable logic block) tile is where general logic is found in an FPGA.  A CLB contains two slices.  Each slice contains LUTs, flip flops, arithmetic logic, and routing.  

- To learn about these,  search the web and find a version of the "7 Series FPGAs Configurable Logic Block User Guide".  Find this version: "UG474 (v1.8) September 27, 2016" if you can.
- Work your way through skimming it.  Pay particular attention to Fig 1-1 and then Fig 2-4.  Fig 2-4 shows what is inside a SLICEL, the most commonly encountered way of forming logic.  Using the rest of the document to help you, figure out where the LUTs are and where the flip flops are.  You should be able to find 4 LUTs and 8 flip flops in the SLICEL drawing.
- There are two kinds of MUXes drawn in this figure.  One kind has select lines drawn in and are normal MUXes like you have always used.  Others have no select lines drawn and therefore no signal which selects among their inputs.  How do you think those MUXes are told which input to select?  HINT: it is done at configuration time.
- The LUTs have two outputs (O6 and O5) - you may ignore the O5 output for now and just assume they are 6-input LUTS with their output on O6.
- Look at the four flip flops down the right side and how they share some key control signals (CK, CE, SR).  How do you make them rising edge triggered vs. falling edge triggered? Hint: follow the clock line to the left and look for a funny 2:1 MUX - what is it doing.  Note, it is one of those MUXes without a select line - how does the MUX know which of its 2 inputs to select and how does that change the flip flops from rising to falling edge triggered?
- Note at the bottom there is a CIN signal coming in and a COUT going out the top.  These are the carry-in and carry-out signals if this SLICE is configured as a 4-bit adder or counter.  The circuitry consisting of MUXes and XOR gates between these two signals is called the CARRY4 or CY4 block.  Look elsewhere in the document and learn how this carry logic block works.
- Print out a few copies of Fig 2-4.  On one, draw in how you would create a 6-input logic function and nothing else in the SLICE.  Where would the inputs come in?  Where would the output come out of the slice?  What routing MUXes (if any) would have to be configured to get the output routed from the output of the LUT to a slice output pin?
- Repeat this but run the logic function output signal through a flip flop before exiting the slice. 
- Draw on a copy of the figure to show how you could use the SLICE simply as a register.  That is, inputs come in from outside but no logic is done on them and they run directly into flip flops.  What inputs would they need to come in on?  
  - Show how to do it using one of the rightmost flip flops.  
  - Now, show how to do it a different way using one of the flip flops toward the center of the diagram.  
  - For each case, how would the various routing MUXes need to be programmed to accomplish this.

## Distributed RAM in SLICEM's
- First turn to Figure 2-3 to see that a SLICEM is close to, but not exactly the same as a SLICEL.  
- Read the section titled "Distributed RAM" for an introduction to how to make small memories in a SLICEM.
- If you are struggling with what they mean by "ports" and the like, a review of Chapter 19 of the 220 textbook might help.
- Note that distributed RAM (or LUTRAM as it is sometimes called) results in non-registered outputs (like the register file of the 220 textbook).
  - How do they suggest you convert the outputs to synchronous outputs?
- Pay attention to the variations you can create in terms of sizes and numbers of ports.  The 4 LUTs in a SLICEM are not totally independent as far as creating LUTRAMs is concerned.  Note that you always have to use the D LUT since that is how writing is done.  But, after that you need not use all of the A, B, and C LUTs.
- Since distributed RAM is available only in SLICEM's, go find out how many SLICEL's and how many SLICEM's are in a typical device.  Hint: the tile names reflect whether they contain two SLICEL's or one SLICEL and one SLICEM - you ought to be able to write about 4 lines of Tcl code to see how many of each type of CLB tile is in a device to see how many of each there are.  Given that, just how much memory can you implement using distributed memory (LUTRAMs) in a typical FPGA?

## Shift Registers in SLICEM's
Next, read about the Shift Registers that are available in a SLICEM.  
- Figure out the basic operation.
- Learn how you can program the length of the shift register.
- Learn how you can cascade them to make longer shift registers.
- Learn why they recommend you make them one stage shorter and then put a flip flop after it to complete it.
- Learn how you can dynamically change a shift register's length while it is operational.

## Wide MUXes in Both SLICEL's and SLICEM's
Quickly identify and then readup on the F7 and F8 MUXes in a slice.   Learn from Figure 2-21 through 2-23 how you can combine LUTs together with these F7 and F8 muxes to make larger muxes.

## Carry Logic
Finally, read the section titled "Carry Logic" and figure out how the CARRY4 block works.

---

# On-Chip Xilinx Memory Resources
- To learn about these look up and find a document on the web called "7 Series FPGAs Memory Resources User Guide".  Find this version: "UG473 (v1.14) July 3, 2019" if you can.
- Chapter 1
  - What sizes and shapes can the basic RAMB36 be configured into?  Can it be any arbitrary shape or are there set possibilities?  What are they?
  - Focus on Figure 1-1.  What does "True Dual-Port" mean?   How do the various input and output signals work?
  - What does write-first and read-first mean?  Hint: they relate to what the 220 textbook Chapter 19 calls "bypass".
  - Learn about how a RAMB36 tile can be used as a RAMB36 memory or two RAMB18 memories.  
  - How many BRAMs are in various devices - how many are in the FPGA you used in your beginning digital course?
  - How are they arranged in the chip?  Are they scattered throughout, are they in rows, are they in columns?
- Chapter 2
  - This chapter shows how instead of a memory, that a RAMB primitive can be configured to be a FIFO.
  - What is a FIFO?  What is it used for?
  - What sizes/shapes of FIFO's can be created?
  - Key concepts:
    - You write things into one end of the FIFO and read things out of the other end.
    - The FIFO will tell you when it is full and can accept no new values;
    - The FIFO will tell you when it is empty and has nothing for you to read out
    - The write port into the FIFO and the read port from the FIFO can run with different clocks.  This provides a convenient way to move signals between two clock domains in a multi-clock system - for example, you could write things in one end at 33 MHZ and could read them out from the other end at 75 MHz.
  - What are the various pins on a FIFO that you use to communicate with it?

# DSP Arithmetic Blocks
- To learn about these look up and find a document on the web called "7 Series DSP48E1 Slice User Guide".  Find this version: "UG479 (v1.10) March 27, 2018" if you can.
- Typically the synthesis tools will understand when and how to use a DSP block for arithmetic in your circuit.  
- The purpose of this is to simply familiarize yourself with what is in a DSP block to understand its power for doing arithmetic.
- Figures 1-1 and 2-1 give an overview of what is inside a DSP block.  Can you see how you might build multiply-accumulate circuits using it?  How about straight accumulators?
- How many DSP blocks are in a typical FPGA?  More than there are BRAM's or fewer?  
- How are they arranged in the chip?  Are they scattered throughout, are they in rows, are they in columns?
- Are there any in the FPGA you used in your introductory digital design class or are they only in larger parts?

# I/O BLocks
- To learn about these look up and find a document on the web called "7 Series FPGAs SelectIO Resources User Guide".  Find this version: "UG471 (v1.10) May 8, 2018" if you can.
- There is simply too much to learn about I/O's due to the variety of I/O standards and voltages they support.  We will focus just on the basics of how an I/O pin can be configured to be either an input, an output or a tri-state.
- Look at Figure 1-1.  How would you configure this to be an input pin?  That is, the outside world would drive the PAD wire and that signal would be fed into your chip as an input.
  - Hint: you will have to figure out how to turn off anything that could drive any signals to the PAD so it can be used as an input.  This turning things off could be done by tying some signals high or low or by using configuration bits.
  - You have likely seen normal buffers before.  They look like inverters without the output circle (this is a non-inverting buffer).  They have no logic function (that is, OUT == IN), but they are used to change the drive characteristics of a signal (make it able to drive larger loads, change its voltage range, etc).  
  - You may not have seen a tri-state driver before - it looks like a buffer but has a second signal coming into its side - when that signal is asserted the buffer drives the input to the output, when that signal is deasserted the buffer doesn't drive anything (its output is high-impedance).  
  - Sometimes such tri-state buffers are drawn with multiple control inputs, meaning any of the control inputs can turn the buffer on (or possibly it requires all of them to be asserted to turn it on).
  - In order to make Figure 1-1 an input pin you will likely have to disable one or more tri-state buffers.  Figure out which ones.
  - So, if the external signal was coming in on the PAD, which signal(s) could it use to come into the chip (there are 2 that could be used)?   Which one would you use and why?  Hint: you usually buffer an input signal up when it comes in before you let it drive any internal logic.  This ensures it has the proper voltage level and drive characteristics you want before it reaches the chip interior.
- Now, Figure out how to use this as an output pin, meaning the FPGA can drive values out to PAD.  Which buffers might you want turned on and which ones might you want turned off.  Hint: if you hook nothing up to the signals entering the chip from the PAD then it won't be an input - it is that simple.  But, you do need to figure out how to have the FPGA interior be able to drive a signal out to the PAD.
- Finally, figure out how to use it as a tri-state I/O, meaning you can use it as an output or you can disable it (by disabling its tri-state buffer).

The above illustrates the basics of programmable I/O blocks.  There are a million other things you could learn about the super-flexible I/O that FPGA's provide, feel free to read more.

---

# Xilinx FPGA Families
Next, spend some time looking at the range of size of devices that are in the 7 Series Family from Xilinx.   It is broken into the following  divisions: Spartan 7, Artix 7, Kintex 7, and Virtex 7.    

- What family part is in the FPGA board you used in your beginning digital design course?
- What are the features of the various divisions of parts?
- What is the smallest part in the 7 Series Family in terms of numbers of CLBs, BRAMs, DSPs, and I/O?
- What is the largest?
- How much total BRAM storage is in the largest part in MBytes?
- How many total DSPs are in the largest part?  Can you find where Xilinx gives a total computational power of those DSP's (in terms of GOPs/sec)?

# Xilinx Coding Guidelines
Although this is the last topic in this self-paced review of what is inside a Xilinx FPGA, it is perhaps the MOST IMPORTANT.

- You can write arbitrary HDL code any way you want and the synthesis and implementation tools will try their best to map it efficiently onto the FPGA.  After all, you can build absolutely anything with gates and flip flops, right?
- While that is true, there is a lot you can do to ensure that:
  1. Your design is mapped as efficiently as possible onto the FPGA.
  2. Your design is able to use all the specialized features found in the FPGA.  
- To help with these goals (especially the second one), Xilinx has published detailed documentation on how you should write your HDL to take maximal advantage of their FPGA's features.
- To learn about this, search for and find a copy of "Vivado Design Suite User Guide - Synthesis", get this one if you can find it: "UG901 (v2019.2) January 27, 2020".  While the entire document has information of interest (features of the various HDL's support for synthesis, for example), we will focus on Chapter 4.  In this chapter they discuss how to code your HDL to get just what you want.
- For example, in Chapter find the section titled "RAM HDL Coding Guidelines".  Here, they describe how to write your HDL code in a way that the synthesis tool can *infer* what you want at a high level and choose an appropriate RAM building block (distributed RAM or block RAM) to efficiently implement what you want.
  - For the various types of memories you might want in your design, they give sample code snippets showing how to *behaviorally* describe the memory so that synthesis will infer it correctly.
  - Carefully studying the correct way to write your code will save you much time trying to figure out why you didn't get what you wanted.  Example: if you code it wrong you might end up with a huge pile of flip flops for your supposed memory block, something that would be slow, large, and use lots of power.  But, if you code it correctly (according to Xilinx's guidelines) then you will get a single BRAM and it will be fast, small, and low power.
- Look through Chapter 4 at the various ways of coding common blocks such as shift registers, memories, and arithmetic blocks.
- Now, remember that this document exists so in the future you will think to refer to it when needed.

But, wait, there's more...

## The Xilinx Libraries Guide
- The above all works well when what you want to express can be written behaviorally and then recognized by the synthesizer.  However, there are some things for which there is no behavioral code that will suffice.  In these cases you will be required to to *structually instance* Xilinx primitives to get what you want.
- A prime example of this is a clock synthesizer PLL.  There is no behavioral description of this, what you need to do is to find the proper library element and then figure out how to instantiate it in your design.
- To learn about this, search for and find a copy of "Vivado Design Suite 7 Series FPGA and Zynq-7000 SoC Libraries Guide", get this version if you can: "UG953 (v2019.1) May 22, 2019"
- Chapter 4 lists the various design elements by functonal category.  Go to the beginning of Chapter 4 (about page 250) and click on "MMCME2_BASE".  
  - This is a multi-mode clock generator/synthesis block.  You can bring an input clock into it and it will generate additional clocks at multiples or fractions of the incoming clock frequency for use in your circuit.  It will also allow you to shift the phase of the incoming clock before distribution to the rest of your circuit.   In short, this is a must-have block for large, multi-clock designs.  
  - The *only* way to get an MMCME2_BASE block into your circuit is to instantiate it.
  - This document shows you how to do so.
  - Similarly, the RAMB36E1 entry will show you how to structurally instantiate a BRAM rather than code it behaviorally if that is what you want.
- Look through the various elements by category and read up on a few to get a feel for what else is in an FPGA that you can structurally instance.  

# Summary
Learning to be a competent FPGA designer depends on your ability to understand how to take advantage of many of these special purpose blocks, either by coding behaviorally correctly or by structurally instantiating them.  If you are only able to write basic Verilog code for designs like you encountered in your undergraduate courses you will never move beyond being a novice designer.

A second major take-away from this self-paced learning unit is that Xilinx does provide extensive documentation about what is "under the hood" in their FPGA designs and also plenty of information on how to take advantage of those blocks in your designs.  Merely being aware of the existence and nature of this documentation is a first step toward becoming a capable designer.





