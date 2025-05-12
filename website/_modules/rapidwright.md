---
layout: page
toc: true
title: RapidWright
slug: rapidwright
type: fpga_opensource
order: 1
---

### Background

**RapidWright** is a (mostly) open-source Java tool that provides you with a programming interface to Vivado designs. RapidWright contains its own Java classes to represent Xilinx FPGA devices, netlists, and how a netlist is implemented on the FPGA device. RapidWright interacts with Vivado through Xilinx `.dcp` (Design Checkpoint) and `.edf` (Electronic Design Interchange Format) files. You can create designs in Vivado, export them to a checkpoint and import them into RapidWright for analysis or modifications. The reverse process is also possible.

Although **RapidWright** is written in Java (available at [Xilinx/RapidWright](https://github.com/Xilinx/RapidWright)), it is possible to access the Java classes and methods directly from Python using the **JPype** tool. Setting up this environment takes only a few minutes, and instructions are provided [here](https://www.rapidwright.io/docs/Install_RapidWright_as_a_Python_PIP_Package.html).

### Starter Code

Here’s a basic Python script that opens a design and prints the number of cells and nets:

```
import jpype
import jpype.imports
from jpype.types import *

jpype.startJVM(classpath=["rapidwright-2021.2.1-standalone-lin64.jar"])

from com.xilinx.rapidwright.design import Design

def main():
    d = Design.readCheckpoint("design.dcp", "design.edf")

    print("Number of Cells:", len(d.getCells()))
    print("Number of Nets:", len(d.getNets()))


if __name__ == "__main__":
    main()
```

For this code to work, you will need to download `rapidwright-2021.2.1-standalone-lin64.jar` from the [RapidWright Releases Page](https://github.com/Xilinx/RapidWright/releases). You will also need to provide a `design.dcp` and `design.edf` file. These can be obtained from Vivado by running the following commands:

```
write_checkpoint <filename>.dcp
write_edif <filename>.edf 
```

You should place all these files (including the `rapidwright-2021.2.1-standalone-lin64.jar` file) into your project directory along with your python script. The output of the script should look something like this:

```
==============================================================================
==                         Reading DCP: design.dcp                          ==
==============================================================================
Loading device from file xc7a200tsbg484-1
 XML Parse & Device Load:     0.475s
              EDIF Parse:     0.448s
        Read XDEF Header:     0.014s
        Read XDEF Caches:     0.023s
     Read XDEF Placement:     0.295s
INFO: Building uncommon Wire->Node cache...
      This might take a few seconds for large devices on the first call.  
      It is generally triggered when getting the Node from an uncommon Wire object.  
      To avoid printing this message, set Device.QUIET_MESSAGE=true or set the ENVIRONMENT variable RW_QUIET_MESSAGE=1.
INFO: Finished building uncommon Wire->Node cache
       Read XDEF Routing:     1.325s
------------------------------------------------------------------------------
         [No GC] *Total*:     2.581s
Number of Cells: 10185
Number of Nets: 11829
```

### Documentation

The documentation for the various RapidWright classes can be found at https://www.rapidwright.io/javadoc/.

Here are a few useful classes:
* [Device](https://www.rapidwright.io/javadoc/com/xilinx/rapidwright/device/Device.html)
* [Design](https://www.rapidwright.io/javadoc/com/xilinx/rapidwright/design/Design.html)
* [Net](https://www.rapidwright.io/javadoc/com/xilinx/rapidwright/design/Net.html)
* [PIP](https://www.rapidwright.io/javadoc/com/xilinx/rapidwright/device/PIP.html)
