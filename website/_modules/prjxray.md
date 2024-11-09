---
layout: page
toc: true
title: Project X-Ray
slug: xray
type: fpga_opensource
order: 3
---

## Overview

[Project X-Ray](https://github.com/SymbiFlow/prjxray) is a project that documents the [Xilinx 7-Series](https://www.xilinx.com/support/documentation/selection-guides/7-series-product-selection-guide.pdf) bitstream.

It is being created by [SymbiFlow](https://symbiflow.github.io/), which aims to create a completely open-source [toolchain](https://en.wikipedia.org/wiki/Toolchain) for FPGAs from various vendors (currently Xilinx and Lattice). In order to create this toolchain, the bitstream needs to be generated after completing implementation. Xilinx does not have documentation open to the public on how their bitstreams are generated, so Project X-Ray aims to fill this gap.

Essentially, Project X-Ray can build databases that map the elements (LUTs, interconnects, muxes, ports, etc.) for an FPGA part to their corresponding bits in the bitstream.

There are many cases where such databases can be useful. As a hypothetical example, if an FPGA part undergoes radiation testing and certain bits flip and break the design, we will want to know why. By using these Project X-Ray database(s) associated with the part in question, we can determine where the broken bits are based on their connections to areas inside the FPGA. Once identified, whatever has broken the design (i.e. whether the broken bit was affecting a PIP, LUT, etc.) can be repaired.

Like a pair of X-Ray Vision Goggles, Project X-Ray is providing the way for the closest examination of bitstreams than ever before. 

## Install

Follow the [Project X-Ray Quickstart Guide](https://github.com/SymbiFlow/prjxray#quickstart-guide) on their GitHub repository to install Project X-Ray. The guide was written for Ubuntu 16.04, but is also known to work on Ubuntu 18.04 and 20.04. Other versions of Ubuntu are not guaranteed to work.

**Please note:** You must have **Vivado 2017.2** installed for Project X-Ray to work. Other versions of Vivado will not work. This version of Vivado may not work with newer versions of Ubuntu (but for now, it does work with Ubuntu 20.04 with no issues). Click [here](https://byu-cpe.github.io/ComputingBootCamp/tutorials/install_vivado/) for instructions on installing Vivado. 

Here are some extra tips for each of the install steps that might be helpful:

* Step 1: Project X-Ray sometimes needs to use Vivado, so it needs to know where you have it installed on your system. By default, it is installed in the `/opt/` directory, but it may be in some other place on your system. Double check where you have it installed, and then you should add the export command from this step to your [.bashrc file](https://www.journaldev.com/41479/bashrc-file-in-linux) so you don't have to type this in each time you start a terminal.

`export XRAY_VIVADO_SETTINGS="/opt/Xilinx/Vivado/2017.2/settings64.sh"`

* Step 4: When running `make`, it will look for a file called `Makefile`. For Project X-Ray, this will be in the `prjxray` directory on the top level, so make sure you are there by running `cd ~/prjxray`.

* Step 5: Go with Option 1.  This will create a self-contained Python virtual environment that will not interfere with your system setup.

* Step 8: Choose Option 1. It is possible that your system may not even have the resources (not enough RAM) to recreate the entire database.

* Step 9: Complete this step exactly as written. This runs a single "fuzzer". If it works, (the last line before your terminal returns reads `touch run.ok`), your system is set up correctly. Since you downloaded the database in Step 8, you don't actually have to run any of the fuzzers to start using the Project X-Ray tools.

One of the installation steps for Project X-Ray had you create a Python virtual environment (the 'make env' step). You may not know about them - they are an important _containerization_ technology.  Once you create a Python virtual environment and activate it, everything you install with `pip` will be placed into that environment and will not affect the rest of your running system.  It is a nice way to get precisely the Python environment you need for a project without messing with the contents of your initial Linux installation.

The key steps are Step 5 and Step 6. Once you create the environment ("env"), you need to activate it any time you are working on the project using the step:

    source settings/artix7.sh

Remember, the `artix7.sh` file is actually located in the prjxray directory you created when you did a "git clone".  So, you will probably want something like this in your .bashrc file:

    alias xray='source ~/prjxray/settings/artix7.sh'

After adding the alias to your .bashrc file, kill your terminal and open a new one. If you have set it up correctly, after changing to your prjxray directory, type `xray` (or the alias keyword you chose) into the terminal to activate your virtual environment. You will know it is activated when the command prompt for your Linux bash shell has "(env)" preceding it like this:

    (env) nelson@ubuntu:~$ 

To deactivate your virtual environment, type `deactivate` into the terminal and "(env)" will disappear, returning your terminal to normal.

To learn more about Python virtual environments, click [here](https://byu-cpe.github.io/ComputingBootCamp/tutorials/pythonEnvs/).

## Lecture

On June 2, 2021, we had a lecture from Professor Nelson about Project X-Ray and [FASM](https://byu-cpe.github.io/ComputingBootCamp/tutorials/fasm/). The video is embedded below.

<iframe width="800" height="600"
src="https://www.youtube.com/embed/6HGN8pQn_jA">
</iframe>

### Timestamps

[0:00](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=0s) Overview of open source software<br>
[4:22](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=262s) Open source FPGA tools<br>
[11:54](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=714s) VTR<br>
[14:20](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=860s) Project IceStorm<br>
[14:47](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=887s) SymbiFlow<br>
[16:45](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=1005s) Introduction to Project X-Ray<br>
[18:45](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=1125s) Nextpnr<br>
[19:47](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=1187s) A look inside Project X-Ray<br>
[23:02](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=1382s) part.json<br>
[24:14](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=1454s) tilegrid.json<br>
[28:19](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=1699s) segbits file<br>
[34:10](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=2050s) Discussion of the uses of Project X-Ray<br>
[38:07](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=2287s) fasm<br>
[44:42](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=2682s) Example fasm output<br>
[50:15](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=3015s) Discussion on fasm uses and benefits<br>
[52:44](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=3164s) Fuzzers<br>
[55:30](https://www.youtube.com/watch?v=6HGN8pQn_jA&t=3330s) Contributing to open source projects

## Follow-Up Activities

Project X-Ray includes many tools, which is where you'll find out more about its capabilities. See the [FASM](https://byu-cpe.github.io/ComputingBootCamp/tutorials/fasm/), [bit2fasm](https://byu-cpe.github.io/ComputingBootCamp/tutorials/bit2fasm/), and [fasm2bels](https://byu-cpe.github.io/ComputingBootCamp/tutorials/fasm2bels/) modules to learn more. 

Below are some activities associated with the fuzzers.

### Recreate the Database (Optional)

**Only complete this step if your advisor has asked you to.**

For this activity, return to your Project X-Ray folder and recreate the database (running all the fuzzers). According to the SymbiFlow website, [Fuzzers](https://f4pga.readthedocs.io/projects/prjxray/en/latest/db_dev_process/fuzzers/index.html) are "a set of tests which generate a design, feed it to Vivado, and look at the resulting bitstream to make some conclusion. This is how the contents of the database are generated."

Recreating the database (running all the fuzzers) will require performing Step 8, Option 2 in the Quickstart Guide.  This will take a very long time; begin the process right away. While this process is running, you are suggested to investigate the links at the bottom of this page to learn more about Project X-Ray and its documentation. Check on the process periodically to make sure it is still working and hasn't crashed. While the fuzzers are running, there are a number of things you can also do to learn about the Project X-Ray system:

  * The output stream will provide an indication on where you are in the build process. The following line demonstrates what you may see. The key here is the text "005-tilegrid" which indicates that the process is currently operating on fuzzer "005-tilegrid" 2020-05-14T17:10:01 - xc7a50tfgg484-1/005-tilegrid  - 1h02m: make---make---sh---make---sh---bash---vivado.sh---vivado---loader---vivado---2*[{vivado}].

  * When a fuzzer has finished, you can enter its directory to browse information about the results. The fuzzers run in sequential order (using the first three digits of the fuzzer name) so it is easy to know which fuzzers have already completed running. If the build process is currently on `005-tilegrid` then the fuzzers `000-init-db` and `001-part-yaml` have been completed.


The following information is helpful to review in each fuzzer directory:

  * The file <!---`run.xc7a50tfgg484-1.ok`-->`run.ok` is an empty file that indicates that the fuzzer has successfully completed running. If this file does not exist then the fuzzer has not finished running. 

  * Each fuzzer directory has a sub-directory named `logs_xc7a50tfgg484-1` that contains the output logs of the fuzzer run. The file `stdout.<date>.log` contains the output to standard out and the file `stderr.<date>.log` contains the output to standard error. It is useful to browse through these files to understand what is involved to run each fuzzer. You can also view the real-time output generated by a fuzzer by running the `tail -f` unix command to follow the file.

  * It is useful to browse a bit in each fuzzer directory to see what types of files are there. Fuzzers often have a Makefile, Verilog files, Vivado .tcl files, a READEME.md Markdown file, and Python scripts.
 
### Run Three Fuzzers by Hand

In your `~/prjxray/fuzzers` folder, there are over 60+ fuzzers to choose from. They are numbered sequentially from 000 to 101, but there are obvious gaps between Fuzzers and their numbers.

If you were instructed to recreate the entire Database in the optional activity above, you ran all the fuzzers at once by typing:
    
    cd fuzzers
    make -j$(nproc)

To run individual fuzzers, we will modify the make command. 

For this activity, run three different fuzzers from the fuzzers directory. The first fuzzer will be `fuzzers/010-clb-ltinit`. The other two fuzzers can be any two of your choice, so have fun with it!

The purpose of the [clb-lutinit Fuzzer](https://f4pga.readthedocs.io/projects/prjxray/en/latest/db_dev_process/fuzzers/clb-lutinit.html) is to determine where in the bitfile the LUT initialize constants are found. Review the fuzzer documentation (there is not much for this one!), change into the fuzzer's directory,  and run it by adding `run` to the end of the make command. Review the console output while the fuzzer is running.

    make -j$(nproc) run

After the fuzzer has been run successfully (**"touch run.ok" is the last line before your terminal returns and "run.ok" exists and is empty**), go back to the fuzzer directory and review the following files:
   
   File      |    Purpose
------------ | -------------
   top.v     | Verilog file to use for running fuzzer. Try to figure out what this circuit is doing.
generate.tcl | Vivado .tcl file for generating the bitfile

**Repeat this same process with two more fuzzers of your choice; research the fuzzer's documentation by name on the SymbiFlow website, run it successfully, and examine the contents of the resulting top.v and generate.tcl files.**

## Learn More

* SymbiFlow Website - <https://symbiflow.github.io/>
* Toolchain Wikipedia - <https://en.wikipedia.org/wiki/Toolchain>
* Project X-Ray GitHub Repository - <https://github.com/SymbiFlow/prjxray>
* Project X-Ray BRAM Patch Github Repository - <https://github.com/SymbiFlow/prjxray-bram-patch>
* Project X-Ray Database: XC7 Series - <https://github.com/SymbiFlow/prjxray-db>
* "Read the Docs" Project X-Ray Documentation (PDF Version) - <https://readthedocs.org/projects/prjxray/downloads/pdf/latest/>
* Project X-Ray Documentation - <https://f4pga.readthedocs.io/projects/prjxray/en/latest/>
    * (Pay particular attention to the first three sections of "Xilinx 7-Series Architecture": Overview, Configuration, and Bitstream Format)
* Project X-Ray Fuzzers Documentation -<https://f4pga.readthedocs.io/projects/prjxray/en/latest/db_dev_process/fuzzers/index.html>

