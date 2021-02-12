
---
layout: page
toc: true
title: VTR
lab: 1
---

# Symbiflow and VTR
VTR is a suite of academic tools for doing FPGA synthesis/tech mapping/placement/routing.  The bulk of the code comes from Univ of Toronto with parts coming from other places.

An overview can be found at: https://docs.verilogtorouting.org/en/latest/vtr/cad_flow/.  The flow through the VTR tools used by  Symbiflow includes HDL -> YOSYS -> ABC -> VPR (Pack/Place/Route/Analysis) -> Bitstream Gen. -> Bitstream.

Historically, devices were described to VTR using an architectural description file, which were required to be fairly uniform and repetitive as far as the routing architecture goes.  Recently, VTR was modified to allow arbitrary routing resource specifications to be supplied (the RR-Graph in the upper left).

At https://github.com/SymbiFlow/fasm there is a nice graphic showing the various ways (including VTR/VPR) that designs can be mapped to FPGAs.

Much of the documentation you will need for VTR will be found at https://docs.verilogtorouting.org/en/latest/vtr/cad_flow/.  The remainder will be found in https://prjxray.readthedocs.io/en/latest/ and in https://symbiflow-arch-defs.readthedocs.io/en/latest/.

And, while there is a symbiflow/vtr-verilog-to-routing Github repo, it is focused on making changes to VTR to work within the Symbiflow ecosystem.  You don't just download it and start running it (you could and there are some simple acceptances tests there but they are not integrated with the symbiflow project)  To use it with symbiflow and commercial devices you need to use the repo mentioned below (symbiflow-examples).

## symbiflow-examples
This Github repo is intended to be how users will access the symbiflow CAD flow described above.  It packages all the needed architecture description files into one large .tar file and also provides what you need from other tools such as VTR, FASM, and prjxray.  This simplifies using the tool since you need not generate a device database yourself.

See https://github.com/byuccl/GoogleDeviceRep/wiki/Symbiflow-ExamplesBootcamp for information on how to run from here.

## symbiflow-arch-defs
This is the repo where complete FPGA device descriptions for FPGA CAD tools are developed.  For example, the .tar file required for the `symbiflow-examples` repo comes from here.  

Although the symbiflow-examples repo mentioned above is where you should be doing your tests, you could build and run the tools in this repo and see how it uses > 200 example designs to to do its work.

### Using symbiflow-arch-defs
* First, you will need a more recent version of cmake.  [This location](https://stackoverflow.com/questions/49859457/how-to-reinstall-the-latest-cmake-version) has a relatively easy way to get the latest cmake:
   ```
   # Will remove if it is exists
   sudo apt remove cmake

   # Install pip if needed
   sudo apt install python-pip -y

   # Install cmake
   pip install cmake --upgrade
   ```
* Next, clone the package from github:

   ```git clone https://github.com/SymbiFlow/symbiflow-arch-defs.git```

* After changing to the symbiflow-arch-defs directory, then follow the instructions at the repo page to make an environment.  After doing so, you can:
   ```
   # Build all 7-series demo bitstreams 
   # Takes forever...
   make all_xc7

   # Try a simpler one - still will take a long time
   # This will simply compile to eblif.  There are other steps
   # such 'route' and 'bin' which will then do place/route and bitgen.
   make simple_ff_eblif
   ```

### Documentation on symbiflow-arch-defs
Docs on this can be found at: https://symbiflow-arch-defs.readthedocs.io/en/latest/.

### Updating symbiflow-arch-defs With Submodules
Doing a ``git pull`` will not update the submodules of a repo.  To update them too after a pull, you need to do ``git submodule update --init --recursive`` too.


----------------------------------
Created by Brent Nelson, June 2020.