---
layout: page
toc: true
title: Tcl and Vivado
lab: 1
---

Tcl is a command language used in a variety of CAD tools.  Our interest in it is for use with Vivado - it is the scripting language that Vivado's command line capability is based on.  Using it you can do 2 main things:

1. Write scripts to automate the processes we typically used the Vivado GUI for.  These include design creation, synthesis, implementation, and bitstream generation.
2. Write scripts to create, modify, or query designs.  That is, Vivado contains methods to add cells and wires to a design and place and route them individually.  It also contains methods to query and analyze existing designs in terms of determining the cells, wires, and placement information in the design as well as querying Vivado's device representation.

The goal of this unit is to help you get comfortable with running Vivado from the command line to accomplish these tasks.

# Task 1: Refresh Your Vivado Abilities With the GUI
* Take an FPGA design from a previous class you have had
* Using the Vivado (GUI mode) in your VM:
  * Open it
  * Modify it
  * Re-simulate it using the built-in simulator
    * Figure out how to add just the signals you care about to the waveform display.  There is a tutorial [here from ECEn 323](http://ecen323wiki.groups.et.byu.net/dokuwiki/doku.php?id=tutorials:simulation_tutorials) which may help in the next few steps.
    * Figure out how to add dividers between groups of signals in the waveform display
    * Figure out how to change the radix used to display the values of multi-bit signals
    * Figure out how to jump to the next signal transition for a selected signal in the waveform display
    * Figure out how to save the waveform display setup you have created and then re-load it for a later simulation
  * Write you own SystemVerilog-based testbench for it and simulate it that way instead of with a Tcl file.  You can find details on testbenches [at this BYU tutorial](https://github.com/byu-cpe/BYU-Computing-Tutorials/wiki/SVTestbenches).  Note that that tutorial is outside this Github repository so use the Back button to return to here...

# Task 2: Learn How to Do All the Above Using Tcl
You can do everything from above (except physically view simulation waveforms) using a script containing Tcl commands.  That is, you can compile code, start a simulation, synthesize/implement/generate bitstreams, etc.
This is often a preferred way to work since you want to be able to write a complete Tcl script to do what you want (create, implement, and then analyze a design) without your having to manually drive the GUI click by click.

To learn how to use Tcl, work your way through this [BYU Tcl Tutorial](https://github.com/byu-cpe/BYU-Computing-Tutorials/wiki/TclVivado).

Then:
* Repeat all the steps from above with your previous class's design. 
* For things that require the GUI to see the effects (like some simulations), have the GUI open.
* For things that don't require the GUI (like synthesizing), do everything by running "vivado -mode tcl" and just do it from the command line.
* Experiment with starting and stopping the GUI.

Finally, a hint: anything you do in the GUI in Vivado (with some exceptions) will put the resulting Tcl command to accomplish that into the Tcl console.  So, one way to learn how to do things is to do them graphically and then look to see what the equivalent Tcl commands to accomplish that are.  

Just remember that you usually are in project mode when you create and work with projects from the GUI.  And, you are in non-project mode when you create designs solely using Tcl commands.  And, note that the commands for doing certain tasks in project mode are different for non-project mode.  So you can only take the above paragraph's hint so far in learning Tcl commands.

# Task 3: Write Some Additional Tcl Scripts to Learn More

## Mini-project 1
You can prevent what sites Vivado will use when doing 'place_design'.  If a site has a PROHIBIT property attached to it then Vivado will avoid using it.  This experiment entails:

1. Write a Tcl script to attach the PROHIBIT property to every SLICE, BRAM, and DSP site in the chip.  You can do a "get-sites" call to get all sites.  Look at what comes back and figure out what names you can filter on  (like SLICE*).  You then attach the property to each thing returned.  
1. Now, remove the property at specific locations (maybe a rectangle or donut shaped area in the middle or corner of the chip.  
1. Run the design through the tools from the command line, start the gui, and observe whether it followed your placement directives.  Iterate until you figure out how to make it do so.

## Mini-project 2
Create an 'analyze_design' script in Tcl.

1. Print out the name of the design and the name of the part it is mapped to.
1. For each port on the top-level of the design print out all the identifying information you can gather for that port (its location, its direction, its type, ...)
1. For each cell in the logical design, print out information about it:
   1. Its name, type, etc.
   1. Its placed location if placed, "UNPLACED" otherwise.
   1. Any of its cell properties that have different values from the default values for such a cell.  This one can be a bit tricky to figure out - search the web for some ideas or create your own.  If this turns out to be too hard, just print out all the properties.
   1. A list of the cell's pins along with the name (or other identifying information) of the net (wire) attached to that pin.
1. For each net in the logical design, print out information about it:
  1. Its name, type, etc.
  1. A listing of the pins on cells that it is connected to.
  1. If it is routed then print out a listing of the pins on sites or cells it is connected to.  For each such connected pin, print out enough identifying information so it is obvious where that can be located.
  1. If it is routed then print out a listing of the wires/nodes and PIPs making up its route.  For each such wire/node and PIP print out enough identifying information so it is obvious where they are located.  This last one is prett difficult until you figure out what a PIP is.   You might want to leave it until you have read through the RapidSmith docs.

In short, from the above info you print out one should be able to re-create the entire design from cells and nets to placement and routing (but you do not need to do the re-creation).

## Mini-project 3
Print an analysis of a device. 
1. How many rows and columns does it have? 
1. How many I/O pins? 
1. How many I/O banks? 
1. How many CLB tiles? 
1. How many LUT BELs? 
1. How many BRAM tiles and/or sites?  
1. How many SLICEL vs. SLICEM sites does it have?
etc.

## Mini-project 4
For a given wiring switchbox in the device:
1. Print out all the wires in the switchbox
1. For each wire, print out:
   1. The possible connections from that wire. For each such connection:
      1. Give the destination wire and whether the connection to that wire is programmable or permanent (yes, Xilinx parts actually have non-programmable PIPs - they are always on).
      1. The tile location of the other wire.

