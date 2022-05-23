---
layout: page
toc: true
title: Vivado Block Design Tutorial
slug: vivado
type: fpga_commercial
order: 3
---


## Setup

### Installing Boards
If you are using a Digilent board, such as the Zedboard, you need to setup the board files in Vivado.  See <https://github.com/Digilent/vivado-boards/>.

### Running Vivado
Before you can run the Vivado tools you should first run the configuration script:
```
source /tools/Xilinx/Vivado/2020.2/settings64.sh
```

This will add the tools to your _PATH_.  

To run Vivado, simply run `vivado`.


## Creating a Simple Hardware Project

### Creating the Project
After launching Vivado, follow these steps to create a hardware project:
1. _Create Project_..., and choose a project name and location.  You can name your project whatever you want, but make sure you place the project in it's own directory.  For example, my project was named *625_lab5* and located at *lab_vitis/hw/vivado_proj*. (Note that I chose to add a _hw_ subdirectory and then created a project directory within this.  You will see why this is useful when you get to the section on _Committing to Git_). Click Next.  Choose an RTL project. Click _Next_.  
2. You don't need to add any sources or constraints yet, just click _Next_.
2. On the next you will be asked to choose an FPGA part.  Click _Boards_ at the top, and choose your board (ie. Zedboard).  Click Finish to create your project.

### Creating a Base Design
In these steps we will create a basic system, containing only the Zynq processing system (PS).
1. Click _Create Block Design_, and click _OK_ on the popup.
2. Add the _ZYNQ7 Processing System_ IP to the design (right-click, Add IP).
3. A green banner should appear with a link to _Run Block Automation_.  Run this. This will configure the ZYNQ for your board.
4. The `FCLK_CLK0` output of the _Zynq Processing System_ will serve as your system clock.  It is set to 100MHz by default.  Connect it to the `M_AXI_GP0_ACLK` input.	
5. Generate a top-level module: In the _Sources_ window, expand _Design Sources_ and right-click on your block design (_design_1.bd_) and select _Create HDL Wrapper_. Use the option to _Let Vivado manager wrapper and auto-update_.

### Committing to Git
Want to commit your project to Git? Don't try and commit your actual project files, as this won't work.  Instead, we will instruct Vivado to create a single Tcl script that can be used to re-create our project from scratch:
* Select _File->Project->Write Tcl_. 
* Make sure to check the box _Recreate Block Designs using Tcl_.  
* Those choose a file location.  This should be outside your project directory, since your project directory is temporary and not committed to Git.  My script is located at `lab_vitis/hw/create_hw_proj.tcl`.  Commit this Tcl script to Git.
* Now, feel free to delete your Vivado project folder, and then you can simply recreate it using `vivado -source create_hw_proj.tcl`.  I typically create a simple _Makefile_ such as this:

```
proj:
	vivado -source create_hw_proj.tcl

clean:
	rm -rf 625_lab5
```

### Synthesizing the hardware
1. Run _Generate Bitstream_.
2. Once the bitstream generation is complete, export the hardware:
 *  _File->Export Hardware_.  
 * Chose the _Include Bitstream_ option, and choose a location to store the Xilinx Shell Archive (.xsa). Mine is placed at `lab_vitis/hw/625_lab5_hw.xsa`.  This file will be provided to the software tools in the next section to tell the software tools all about our hardware system configuration.
3. You should commit this _.xsa_ file to Git.

