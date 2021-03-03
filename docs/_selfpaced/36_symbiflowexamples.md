---
layout: page
toc: true
title: symbiflow-examples
lab: 1
type: fpga_opensource
order: 7
---

This is useful because it provides and illustrates an end-to-end flow: Verilog --> yosys/vpr --> bitstream.

One of the goals of the Symbiflow project is to get a complete Verilog-to-Bitstream CAD tool flow out to users.  This can now be found at https://github.com/symbiflow/symbiflow-examples with three example circuits (and they are not necessarily toy circuits!).  

There are instructions at that page for how you can build the sample designs there manually.   The process outlined is fully self-contained - you do not need anything else installed to run these designs - the instructions do it all.  The best way to test it out is to simply copy the entire list of instructions and paste them into a terminal window.  

Once you have done that and the tests have been created, go into the 3 directories with Verilog files in them and examine what you see.  There are just af few files for each example - figure out what they do and how they correspond to the files required for a Vivado compilation.  

Also, find the .bit files generated - if you had the right board you could download them to the board - they do work!

## Some Things to Do
* Make a change to one of the designs and re-make it.  
* Time how long it takes.  
* Carefully read what is printed out as the tools run.  
* Can you figure out how what is printed corresponds to what you know about the synthesis-implementation-bitstreamGeneration process?  
* Are there any steps that seem to take an especially long time?
* From the Symbiflow Github or readthedocs pages, can you figure out what boards are supported?  
* At the current time the board from the digital lab in our department is not supoprted.  But, they would very much like for it to be supported and have provided some thoughts on what needs to be done.  If you are interested, let Prof Nelson know - it could be a fun side project and the department would definitely loan you a board to use for it...

