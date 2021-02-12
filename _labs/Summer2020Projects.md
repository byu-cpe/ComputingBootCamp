# Projects for Summer 2020
Short explanations are provided for each project.  The cognizant faculty members are also listed for each for questions.  The tasks listed are not meant to be exhaustive but rather the first steps to being with.

# Google Database - Michael
Develop an understanding of our device representations as well as those from VTR.

* Faculty: Wirthlin and Nelson

1. Generate RS2 device files for multiple parts in the Artix7 family and verify it works (using DeviceBrowser for example).
1. Collect statistics on size of the files generated (the .xdlrc, .db, as well as .xml files)
1. Get memory usage report for RS2 before and after loading a given device file. In addition, measure how much time it takes to load each design into RS2.
    * *Crude*: look at process size before load is executed vs. after
    * *Better*: find Java runtime tools that can measure memory size of a data structure and apply it to the entire device representation and all its children and constituent parts.
1. The above device file describes the device only.  Programs like routers will elaborate on that data structure as they trace out and use wires.  In the process they will create added data structures to hold that info.  In the limit, such a representation should be as large as a fully elaborated graph like VTR's rr-graph.  We would like to understand the relative costs of the two ways of doing things.
    1. Understand costs of enumerating different fractions of the wires in the device.  If you enumerate 1% vs. 10% vs. 50% vs. 100% what are the sizes of the memory needed as well as the number of objects created?
        * Enumerate how many wire segments total there are in a device
        * Do a BFS over the entire device from a given source (like the output of a flip flop or an IOB).  What fraction of the device's wiring does that cover?
        * As you do so, you will need to avoid revisiting same place twice (there may/will be cycles in the routing graph).
1. Start working with the Symbiflow VTR data structures
    1. Build a map of the various data structures used and a description of what they are used for
    1. Run the symbiflow/fpga-tool-perf tools to measure runtime of VTR vs. Vivado

  * [Project Documentation](GDR-Project-Documentation)

# ICAP Bitstream Extraction - Mason
Develop a SystemVerilog design which uses the Xilinx ICAP primitive to extract the bitstream from a running design and output it on a pin in some form.  This project is the "getting started" step in a bitstream security project where the goal is to analyze bitstreams to detect embedded malware (called "hardware trojans").

* Faculty: Nelson, Wirthlin

1. Using external tools (Vivado GUI, Vivado Tcl, possibly Python or C) - experiment with configuring and doing readback of a FPGA chip.  Verify you can get the actual bitstream and is correct.  Verify that you can get the FPGA state.  Figure out how to map locations in the readback values to FF's and BRAM's in the design. 
1. Do a SystemVerilog design targeting the same board we use in 220.  It should have the ability, on command (from a button or switch for example) to use the ICAP primitive to read out the bitstream from the FPGA it is running on.
1. Output the bitstream using one of the I/O channels on the board (could be serial, USB, or just raw data on a pin).  The exact delivery mechanism may or may not be important and will be decided later.
1. Determine under what conditions the ICAP can extract the bitstream?  For example, what can be done at design time to either allow or prevent this kind of  *readback* from occurring?  Are there  options available to prevent it?  
1. How does encrypting the bitstream affect your design's ability to extract a bitstream?  Does it totally prevent it?  Is there a way to allow your design to do it (by giving it a key, for example)?  Are there ways around this?
1. Reading the Xilinx documentation, determine when this capability (ICAP) was first introduced into Xilinx devices.  Determine if/how it has changed between families - has it been modified from Virtex5 until Virtex7?  Does Ultrascale change it in any way?
1. There are at least two kinds of readback.  One retrieves just the bitstream.  Another retrieves the data in the flip flops and memories (and possibly maybe the bitstream too).  Modify your design to support both.
1. Initially your design could retrieve the entire bitstream.  Now, modify it so it retrieves only selected frames of data - this shoudl apply to both modes.

  * [Project Documentation](https://github.com/byuccl/gmt/blob/master/icap_project/ICAP-Project-Documentation.md)

# BRAM Patch Tool: Bitstream to mem.init File Conversion - Orgill

The prjxray-bram-patch tool provides some nice design <-> FASM <-> bitstream modification capabilities.  This project will make it possible to take the contents of a memory as contained in a bitstream and convert it back into a `mem.init` file of the type that Verilog's `$readmemb()` function can parse.

* Faculty: Nelson, Wirthlin

1. Create a `fasmToMemInit()` routine to do the conversion back to memory init file.
1. Refactor code to eliminate duplication between existing `mempatch()` and new `fasmToMemInit()` code.
1. Make a microtests directory.  Each test will be run when a .sh script is executed.
1. Verify that XBP supports both binary and hex file formats for memory initialization files.
1. Setup Travis CI to do testing of pull requests to the repo in Github
    * Consider building and using a Docker system for it if it makes sense
1. Learn how to use `sphinx` to create a `readthedocs.io` documentation site.
1. Develop patch code for LUTRAM designs
1. Develop patch code for individual LUTs

# Bitstream Tools for prjxray - Benjamin

It can be useful to be able to identify how a given bit maps back to feature in the FPGA architecture.  For example, if the corruption in a certain bit causes a design to quit working (even if it has had TMR applied), it would be important to find out why.  This project will deal with creating the software and techniques to do that.

* Faculty Wirthlin, Nelson

1. Use the bits2fasm tools to generate the FASM for several bitstream designs.
1. Modify $XRAY_BIT2FASM to have a mode where it prints out both the FASM string but also the bit location and values.  
1. Create a "single-bit" to FASM tool. This tool will take parameters for a single bit in the bitstream and print out all FASM associated with that bit.
1. Bring up the symbiflow-bitstream-viewer tool and learn what it can do.  Will likely need fixing since it is out of date with the rest of symbiflow.  Propose new useful features for it and implement those deemed useful by the faculty.
1. Generate a new database for a different part.  Identify holes in the prjxray fuzzers.  Propose and possibly implement new fuzzers to fill these holes.
1. Begin work on a DSP fuzzer for 7 Series devices.

# BRAM Patch Tool Extensions (prjxray-bram-patch) - Jonny

prjxray-bram-patch (XBP for short) was developed last year by Jon Orgill.  It takes a bitstream which contains RAM or ROM structures implemented using BRAM sites, pulls out the memory initialization contents information, and allows you to patch in new information.  For example, if you have a ROM acting as a lookup table for a computation in your design you can patch the table contents without re-running the synthesis/implement/bitgen flow.  

* Faculty Nelson, Wirthlin

1. Learn how the generate_tests.py and run_tests.py programs work.  
   * See how run_test.py calls the bitstream patch routine to do the actual patching.
   * See how you can run a whole collection of tests or you can run a single test from the program.
1. Modify XBP to support/produce partial bitstreams.  
   * Make is so that it can output just the changed frames to the new FASM file.  To do this, learn how existing patch code works.
   * Figure out how to convert a partial FASM file to a partial bitstream (Dallon's stuff will help).
   * Demo: patch the memory of a running design on a board.
1. Given a description of a memory (provided by a .mdd file), create a list of the just the configuration frames that correspond to that memory.  This will enable us to pull out just the frames from a running FPGA that we want, modify them, and send them back in (someone else will do the pulling and sending steps).
1. Determine whether the partial bitstream code that Dallon Glick created in his MS thesis on Maverick was ever contributed back to symbiflow as a pull request.  If not, get it added into symbiflow via a pull request.
1. Learn how to use the above partial bitstream and test its use on some designs with boards.
1. Loop back with Benjamin's project and learn how the bitstream viewer works and could be used in this project.

### Part 2:
* Using a sample design where the BRAM was initialized to all 1's, be able to find the blocks of 1's in a fasm2frames file.  There is no output for this, just to demonstrate to yourself you know how to locate the frames and words that contain a BRAM's data.  You will need to use the tilegrid.json file.  You will also need to use the MDD file to figure out what tiles the BRAM covers so you can then lookup the frame #'s.
* Using a sample design, the tilegrid.json, and the segments part of the prjxray database, verify that you can look in a .fasm file's INIT string, and find specific bits bits in a fas2frames file.  No output for this, just to demonstrate that you understand the structure of the segments file for BRAM's in the prjxray database.
* Using a sample design (4kb16 for example) and the prjxray database, generate a file that gives info on each  BRAM primitive in it.  For each, give its name (which will contain its location), give the range of frames it has bits in, the word offset, and the # of words.  This will be sent to Matthew when completed so he can decide which frames to do with his partial reads.  You will need to use the MDD file to figure out what BRAM primitives are a part of the desired memory (since there may be multiples in a design).


# Symbiflow FPGA Tool Performance - Ryan

The symbiflow group has created a repo called symbiflow/fpga-tool-perf.  Its role is to help measure the performance of various FPGA tool flows.  Not only can it help compare their tools' performance against commercial tools, it can compare new versions of the same tools to evaluate the benefits of any modifications/enhancements that might be made.  This project is a key piece of the Google Device Representation project.

* Faculty: Nelson, Wirthlin

1. Install the tool and learn to use it for some basic tasks.  
1. Compare Vivado to the Yosys/VTR/prjxray flow on the 3 example circuits found in the symbiflow-examples repo. See notes [here](https://github.com/byuccl/GoogleDeviceRep/wiki/fpga-tool-perf#fpga-tool-perf-comparison-examples).
1. Learn how to check out different commits of the symbiflow tool flow and compare different versions of those tools to one another.
1. The tool operates by parsing the output of the various tools.  The tool's support for parsing the output of commercial tools need improvement.  Work with Google's Tim Ansell to understand the issues and upgrade the tool.

#### Project Notes:
- [fpga-tool-perf](https://github.com/byuccl/GoogleDeviceRep/wiki/fpga-tool-perf)
- [my contributions to fpga-tool-perf](https://github.com/byuccl/GoogleDeviceRep/wiki/RyanContributions).
- [notes on making pull requests and contributions](https://github.com/byuccl/GoogleDeviceRep/wiki/PullRequests) to open-source projects. I had some help from the other contributors in SymbiFlow and learned lots of helpful tips and best practices.
- [conda](https://github.com/byuccl/GoogleDeviceRep/wiki/Conda)
##### Fall 2020 Work and Notes:
- [vtr](https://github.com/byuccl/GoogleDeviceRep/wiki/VTR)
- [fpga-tool-perf_vtr](https://github.com/byuccl/GoogleDeviceRep/wiki/fpga-tool-perf_vtr)
- [symbiflow-arch-defs](https://github.com/byuccl/GoogleDeviceRep/wiki/symbiflow-arch-defs)

# Create Test Designs on Arty V7 Board - Jason

One of the goals of the symbiflow-examples repo is to provide a collection of functioning designs across a variety of boards.  By doing so, the hope is that the community will be drawn to using (and contributing to) the tools.  This project is to add to the sample designs collection (there are currently only 3).

* Faculty: Wirthlin, Nelson

1. Checkout the repository, build the full flow, and run the 3 examples in the repo.
   * Document any issues you had during hte process
   * Enable "watching" of the repository. Rerun the 3 examples if there are any major changes to the repository.
1. Create a full self-test design in SystemVerilog for the Basys3 board.  It should test every part of the board in a way that it can be determined that it is functioning completely.
   * Look for existing sample code (the board ships with such a design - is its source available?)
   * Dr. Wirthlin has some VGA code if you need it
   * Use Vivado to synthesize the design and download the design to the Basys3 board
   * Commit your files in this repository (not sure where yet)
1. Run your design through the symbiflow tools and get a working bitstream
   * You will need to modify the .xdc files to the symbiflow files
   * Document any issues you run into
   * Once the design is working, add it to the symbi-flow examples repository
1. Port design to the Arty A7 35T (Prof Nelson has one to use)
        * Add support for DDR
        * Add support for ethernet
1. Port design to the NEXYS4 DDR board (the one we use in 220)
        * Confer with Tim Callahan of Google - he is the one adding support for the chip on the NEXYS4 board (a xc7a100T)
        * Add more features to test everything on it.  The bootup design on the 220 boards could be a starting point if the source is available.

[Jason's Notes](jason2020)

