# RapidSmith - A Libary to Allow The Creation of Custom CAD Tools for Xilinx FPGAs

## Instructions for acquiring and working with RapidSmith

 * Go to the [RapidSmith](https://sourceforge.net/projects/rapidsmith/) project on sourceforge.net. This is the sourceforge repository for the RapidSmith project that has a lot of important background information and historical context to the project.
 * Click the link for the "/rapidSmith-0.5.3-linux64.tar.gz" file at the bottom of the page to download the project.
 * Uncompress the image in your linux virtual machine (tar -xvf rapidSmith-0.5.3-linux64.tar.gz)
 * Read the document in the ./rapidSmith/doc/TechReportAndDocumentation.pdf file

GOAL: read through the RapidSmith documentation just to see what is there.  You are not to become an expert in any way.  We just want you to understand how this research project worked.  Specific questions you should look for answers to include the following.  A few web searches for terms like NCD will be helpful as well:

1. What Xilinx tool was RapidSmith designed for? (HINT: it is not Vivado).  It is the predecessor to Vivado - what is that called?
1. Just how old are the parts supported by RS?
1. What's all this stuff about Java package names?  Do you understand Java packages?  If not, can you learn just a bit so you will understand its structure?
1. What does the "design" package describe for your design?
1. What does the "device" package describe for your design?
1. Can you follow the example program on page 21?
1. What is an XDL file?
1. How do you get an XDL file from Xilinx?
1. Can you see how an instance in XDL represents what we would call a slice?  Do you see where the LUT contents are programmed?  How about the MUX-based routing resources inside the slice?
1. What is an XDLRC file?
1. How do you get an XDLRC file from Xilinx? 
1. How are wire resources represented in RS?
1. Walk your way through and read the various code samples given in the document.  From these, can you start to understand how you might be able to use RS instead of Tcl to do some of the exercises you just completed in Tcl?  From the first program on page 12 here are some examples of thing you should look for:
    * How to create a design, give it a name, and specify what part it uses.
    * How to create a new SLICE instance.
    * How to set the logic equation for the D LUT in the slice.
    * What call is used to place an instance onto a site in the FPGA.
    * How to create and set the properties of an IOB.
    * How to read and write XDL files.

## Readings

Below are links to papers on RapidSmith which will help you start to understand the context of what we have been doing creating custom CAD tools for FPGA's.  

These are at IEEE's website, **if you log in with CAEDM's VPN, you will be able to get to the PDF's for them**.

Paper #1 was an early paper, Paper #2 is better.  The papers on HMFlow give you an idea of why RapidSmith was originally written - they _use_ it.

* [RapidSmith - paper #1](https://ieeexplore.ieee.org/document/5681429)
* [RapidSmith - paper #2](https://ieeexplore.ieee.org/document/6044842)
* [Paper #1 on HMFlow - a Use of RapidSmith](https://ieeexplore.ieee.org/document/5694290)
* [Paper #2 on HMFlow - a Use of RapidSmith](https://ieeexplore.ieee.org/document/5771262)

The last link (below) will take you to Chris Lavin's PhD Dissertation.  His dissertation was on rapid prototyping using HMFlow.  In that work, the development of RapidSmith was done by Chris to provide the tool he needed to build HMFlow.  While you may not want to read the entire thing (a) it is very readable and (b) parts of it will really help you understand better how RapidSmith works and what HMFlow is all about.

* [Chris Lavin Dissertation](https://scholarsarchive.byu.edu/cgi/viewcontent.cgi?article=3932&context=etd)



----------------------------------
Initially created by Brent Nelson, April 2020.