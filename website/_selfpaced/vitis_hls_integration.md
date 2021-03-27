---
layout: page
toc: false
title: "HLS System Integration"
type: fpga_commercial
order: 6
---

### Previous: [Vitis Tutorial]({% link _selfpaced/24_vitis_hls.md %})

This page discusses how you can export your IP from Vitis HLS to be used in a Vivado project, and ultimately to communicate with the HLS accelerator from a Vitis software proj ect.

## Modifying Your Hardware

### Exporting your HLS as IP
  Since our goal is to communicate with the HLS IP from software, we will add a Slave AXI connection to our HLS IP core so that it can be connected to the ARM AXI bus.

* Run Vitis HLS and open your project from the last assignment.
* Add a directive to your top-level hardware function.  Choose the *INTERFACE* directive type, and change the mode to an AXI4-Lite Slave (*s_axilite*).
* Set the *INTERFACE* of the *input* parameter to also be the AXI4-Lite bus.
* Run C Synthesis.
* Click *Solution->Export RTL*, and make sure the Format Selection is set to * Vivado IP (.zip)*.
* Close Vivado HLS.
* Unzip your IP to a folder, for example, I used `unzip digitrec.zip -d lab_vitis/ip/digitrec/`

**Bug fix**: I ran into a bug in Vitis 2020.2 that I had to fix.  Look in your *\<ip_dir\>/drivers/digitrec_v1_0/src/Makefile* and look for **three** commented out lines that start with '#echo'.  Remove these lines from the Makefile.  See <https://forums.xilinx.com/t5/High-Level-Synthesis-HLS/Bug-HLS-2020-2-generated-makefile-compilation-error-in-vitis/td-p/1206772>


### Adding your IP to Vivado
* Run Vivado, open your existing project, and open the block design.
* If you do not already have a `Processor System Reset` IP, add one to your design.  This will use the reset signal output by the processing system to reset IP in the FPGA fabric.  
	* Connect the system clock ( `FCLK_CLK0` from *ZYNQ7 Processing System*) to the *slowest_sync_clk* input.
	* Connect the processor reset output (*FCLK_RESET0_N*) to the *ext_reset_in* input.		
* If you do not already have an *AXI Interconnect* IP, add one to your design.  This is the bus that will allow the ARM CPU to communicate with the IP implemented in the FPGA fabric.
	* Configure the bus to have 1 Slave Interface and 1 Master Interface.
	* Connect the PS bus master (*M_AXI_GP0* from *ZYNQ7 Processing System*) to the *S00_AXI* slave port.
	* Connect your clock (*FCLK_CLK0* from *ZYNQ7 Processing System*) to all the clock inputs (_*ACLK_)
	* Connect your interconnect reset (*interconnect_aresetn* from *Processor System Reset*) to the *ARESETN* input.
	* Connect your peripheral reset (*peripheral_aresetn* from *Processor System Reset*) to the other reset inputs (_*ARESETN_)


* Add your HLS IP:
	* Open the IP catalog
		* Right-click, *Add Repository*
		* Navigate to the *ip* folder that contains your HLS IP extracted in the earlier step, and add this directory.
	* Go back to your block design and add the HLS IP to your design.
	
* Connect up your HLS IP:
	* Connect the clock (*FCLK_CLK0*) to the clock input (*ap_clk*)
	* Connect the reset (*peripheral_aresetn*) to the reset input (*ap_rst_n*)
	* Connect the bus (*M00_AXI* from the *AXI Interconnect*) to the bus slave port (*s_axi_control*)
	
* Assign an address to your HLS IP:
	* Open the *Address Editor*, find your IP, right-click *Assign*.
	* Save the block design.
	
* Run *Generate Bitstream*.
	
* Export the new XSA file and overwrite your old one.  

* Close Vivado


## Communicating with your HLS IP from Software

### Updating Platform Project
* Launch Vitis and reopen your existing workspace.
* Right-click on your platform project, and choose *Update Hardware Specifiction*. Make sure you select your new XSA file.
* If done correctly, you should see your HLS driver located at *ps7_cortexa9_0/standalone_ps7_cortexa9_0/bsp/ps7_cortexa9_0/libsrc/digitrec_v1_0/src.  Inspect the source code and locate:
	* *xdigitrec_hw.h* has register offsets for your IP core.  If you followed the steps correctly, you should have:
	  * control register (*XDIGITREC_CONTROL_ADDR_AP_CTRL*)
	  * interrupt registers
	  * return value register (*XDIGITREC_CONTROL_ADDR_AP_RETURN*)
	  * function argument register (*XDIGITREC_CONTROL_ADDR_INPUT_R_DATA*) and more.
	* *xdigitrec.h* provides a higher-level driver interface, with functions for starting your accelerator, checking if it's done, setting argument inputs, etc.
* Build your platform project.

### Using the Driver in Your Code
* Include the necessary header file in your application code and write software to test that you can start your IP, wait for it to complete, and retrieve the return value.  
* You will need to initialize the HLS device driver before you can call any of the function.  As with most Xilinx drivers, this is done by calling *_LookupConfig*, providing the device ID from *xparameters.h*, and then calling *_CfgInitialize*:
```
XDigitrec digitrec;
XDigitrec_Config* digitrec_config = XDigitrec_LookupConfig(XPAR_DIGITREC_0_DEVICE_ID);
XDigitrec_CfgInitialize(&digitrec, digitrec_config);
```

* Try running the HLS accelerator and waiting for it to complete.  Provide a test value and check the return value.
