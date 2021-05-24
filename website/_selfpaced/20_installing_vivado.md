---
layout: page
toc: true
title: Install Vivado/Vitis
slug: install_vivado
type: fpga_commercial
order: 1
---


We will be using several Xilinx software tools, including Vivado, Vitis, and Vitis HLS.  These can all be installed using a single _Vitis_ installer.  

### Download

1. Go to <https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis.html>

2. On the left-hand bar, select _2020.2_, and find the section _Vitis Core Development Kit - 2020.2  Full Product Installation_.

3. You can either:
    * Download all the files upfront (_All OS installer Single-File Download_), or 
    * Download files as you install using the Web Installer:
      * Windows: _Xilinx Unified Installer 2020.2: Windows Self Extracting Web Installer_ 
      * Linux:  _Xilinx Unified Installer 2020.2: Linux Self Extracting Web Installer_

4. You will need a free Xilinx account in order to download the software.

### Running the Installer
Depending on how you downloaded the files, you will run the installer differently:
  * _All OS installer Single-File Download_:
    * Windows 
        * Extract the files from the _Xilinx_Unified_2020.2_1118_1232.tar.gz_ archive using a program like 7-zip.
        * Run _xsetup.exe_
    * Linux:
        * Extract the files from the _Xilinx_Unified_2020.2_1118_1232.tar.gz_ archive: `tar -xvf Xilinx_Unified_2020.2_1118_1232.tar.gz`
        *  Run the installer: `sudo ./xsetup`

  * Web installer:
    * Windows: 
      * Run _Xilinx_Unified_2020.2_1118_1232_Win64.exe_
    * Linux: 
      * Run the installer: `sudo ./Xilinx_Unified_2020.2_1118_1232_Lin64.bin`

### Installer Options
  1. Enter your Xilinx account information, and select _Download and Install Now_.
  2. On the _Select Product to Install_ screen, choose _Vitis_.
  3. On the customization screen, uncheck everything, except make sure you have:
     *  _SoCs/Zynq-7000_ or _SoCs/Zynq Ultrascale+ MPSoC_, depending on which board type you are using.
     * Make sure you install the 7 Series parts
     *  Install Cable Drivers

  4. On the next screen, agree to all boxes.
  5. On the next screen, choose an installation location with enough space.
  6. On the next screen, click _Install_ and wait a while.

### Install Cable Drivers

If you are using Windows, your cable driver will have been installed during the installation process.  If you are using Linux, you must install them manually:

```
cd /tools/Xilinx/Vivado/2020.2/data/xicom/cable_drivers/lin64/install_script/install_drivers
sudo ./install_drivers
```

### Other Considerations
  * Before you can run any Vivado/Vitis tool, you will need to add the executables to your PATH.  This is done using a Xilinx-provided script:

        source /tools/Xilinx/Vivado/2020.2/settings64.sh

  * If you want that to always be run when you open a new shell, add it to your `~/.bashrc` file.  *Note:* While this is convenient, it can also cause issues.  The Xilinx tools come with their own versions of several others tools (ie. make, cmake), and you if add this to your *.bashrc* then the Xilinx versions of these programs will always be run instead of the version installed by your Linux package manager.
  * By default, Vivado creates log files in whatever directory it is run from.  To prevent these from cluttering up your filesystem, it is nice to redirect them to fixed locations (again, you may want to add this to your `~/.bashrc`):

         alias vivado="vivado -log /tmp/vivado.log -journal /tmp/vivado.jou"

