---
layout: page
toc: true
title: "Microblaze Soft Processor"
slug: microblaze
type: fpga_commercial
order: 7
---

## Create a New Vivado Project
*  Run Vivado (`vivado`)
*  Create Project
*  Click Next
*  Choose a project name and location and click next
*  Choose RTL Project and check "Do not spicify sources at this time" and click next
*  At the top of the window select Boards
*  From the list of boards highlight the Nexys4 DDR and click next
  *  If the board is not shown in the list, you need to download and add the board file to vivado. 
  *  Follow this tutorial for instructions on how to obtain and add the board file
*  Click Finish
## Create Block Design
*  On the left in the Flow Navigator, under IP INTEGRATOR, select "Create Block Design"
*  Choose a design name and click OK
*  Select the board tab
*  Right click on the Push Buttons entry
*  Select Connect Board Component
*  In the popup, select Create new IP -> AXI GPIO -> GPIO and click OK
*  In the board tab, right click on the LEDs
*  Select Connect Board Component
*  In the popup, select existing IP -> axi_gpio_0 -> GPIO2 and click OK
*  In the board tab, right click on System Clock
*  Select Connect Board Component
*  Check the box next to "clock_CLK_IN1" and click OK
*  Double click on the clk_wiz_0 block in the block diagram
*  On the Board Tab, make sure that CLK_IN1 has sys clock selected
*  For EXT_RESET_IN select reset
*  Select Output Clocks tab
*  Make sure that the clk_out1 box is checked and that the Requested Frequency is 100 MHz
*  Select Active Low for the Reset Type
*  Click OK
*  Click "Run Connection Automation"
*  Make sure the resetn box is checked
*  Click OK
*  In the Board tab, right click on USB UART
*  Select Connect Board Component
*  Select AXI Uartlite -> UART
*  Click OK
  *  You can double click the new UART Block to check the UART settings
*  Click the "Add IP" (Plus sign at the top of the block diagram)
*  Search Microblaze
*  Double click microblaze
*  Click Run Block Automation
*  Set Local Memory to 32 KB
*  Click OK
*  Click Run Connection Automation
*  Check the box next to All Automation
*  Click OK
## Generate Bitstream
*  Click the Validate design button
*  Click OK
*  On the sources tab, right click your block design and select Creat HDL Wrapper
*  Check Let Vivado manage wrapper and auto-update
*  Click OK
*  Under the Flow Navigator select "Generate Bitstream"
*  Click Yes
*  Click OK
*  Wait
*  On the next pop up click Cancel
*  In the File drop-down select Export, then Export Hardware,
*  Check Include bitstream and click OK
*  
## Launch Vitis

## Create the Platform Project

## Create the Application Project

## Run Your Applicaton on the Board
*  Right-click on your executable folder (down one level from the *_system* project created in the last step -- see image below), choose *Run As->Launch on Hardware (Single Application Debug*.  
<img src = "{% link media/vitis/run_program.png %}" width="800">


* You should see the message *Hello World*.

