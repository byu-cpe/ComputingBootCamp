# Symbiflow Examples Jason Prescott

This summer I worked in the Immerse Program under the guidance of Professor Brent Nelson. During my months in the program I was able to learn serval new skills that have allowed me to be able to create a new project for the Symbiflow example repository, as well as create user friendly instructions to be able to help future supporters to be able to contribute to this project in the future. The Project I created was simple, but it is the stepping stone to understanding how the new projects need to be structured, as well as show how with more attention, any project can be converted to the necessary format to be created using the Symbiflow tool chain. I have created instructions that are found later in this document which I created with the help of faculty and fellow Immerse members as I researched the inner workings of the project. I realized that there were steps that are easily forgotten by experts in the field, and the lack of those simple steps led me to run into many errors as I learned how to work the Symbiflow tools. I now have instructions that have so far worked in every situation that I have been able to test in my short time, as well as target the new and inexperienced members of the Symbiflow community that are hoping to join in the project. With the instructions that I have formed, it will allow easier entrance to the project as well as encourage excitement from those who want to see where the project is heading.

I was able to create another example modeled after the previous examples that are found on the Symbiflow examples repository. I named this example up_counter.The project that was the core of the example up_counter was the project that I was able to build using the Symbiflow tool chain. This project was not a project I created myself, but was a project, created by a designer named Deepak, that I found on asic-world.com. I did need to alter the verilog project file slightly by adding the following lines to the project for it to function with the Symbiflow toolchain.

```
wire bufg;
BUFG bufgctrl(.I(clk), .O(bufg)); 
```

These lines created the needed clock net that was used in the .SDC file. Other than those lines the file was unchanged. This project is the stepping stone to creating more complex multi-file projects that will allow users to create the projects that they desire to test on the open source tools. I was unable to create the next project that I had planned, but with the instructions that I have formed, the next level projects can be easily created with only a little more time and effort. The files of the example that I was able to build successfully will be included later in the paper with the instructions to create future projects.

As I started to work with the Symbiflow examples I was able to create steps to set up the environment and the necessary tools that are easier to follow for those who are not familiar with the Symbiflow project. I made these steps with the help of Professor Nelson who was able to see where I was having issues. The steps are very similar to the ones found on the symbiflow example github repo, with some slight changes. The first change is that we added a new first step which is to download the symbiflow examples repo. This is an important step that is easily forgotten, but will prevent the rest of the steps from working. The following step was added so that all of the symbiflow files are in the same folder to help with organization of the tools and files. The rest of the steps are almost the same as shown in the repo. The last section shows the code that will need to be put in your .bashrc file if you wish to create the examples after closing the command prompt that you were working with. The options you have to create projects without re-creating the environment everytime is to add the necessary files into your .bashrc, which will put you into the correct environment when you open the command prompt, or you will need to create a alias which will activate the needed code before you will be able to create any more projects with the symbiflow tools.

Here are the new Symbiflow example instructions:

## Install and Create Env
```
git clone https://github.com/symbiflow/symbiflow-examples 
cd symbiflow-examples
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O conda_installer.sh
export INSTALL_DIR=$PWD/examples/xc7
bash conda_installer.sh -b -p $INSTALL_DIR/conda
source "$INSTALL_DIR/conda/etc/profile.d/conda.sh"
conda env create -f xc7/environment.yml
conda activate xc7
# The specific file in the command below will change as new versions are made (check the README.md of the repo)
wget -qO- https://storage.googleapis.com/symbiflow-arch-defs/artifacts/prod/foss-fpga-tools/symbiflow-arch-defs/continuous/install/66/20200914-111752/symbiflow-arch-defs-install-05d68df0.tar.xz | tar -xJ --one-top-level=$INSTALL_DIR/xc7/install

```

## Compile Examples
```
cd symbiflow-examples
export INSTALL_DIR=$PWD/examples/xc7
export PATH="$INSTALL_DIR/install/bin:$PATH"
source "$INSTALL_DIR/conda/etc/profile.d/conda.sh"
conda activate xc7 pushd examples/xc7/counter_test && TARGET="arty" make && popd
```

## Here is what I put into my .bashrc file:
```
cd symbiflow-examples 
export INSTALL_DIR=$PWD/examples/xc7 
source "$INSTALL_DIR/conda/etc/profile.d/conda.sh" 
export PATH="$INSTALL_DIR/install/bin:$PATH" 
conda activate xc7
```

Here are the common errors that I found as I created the Symbiflow examples:
```
xc7/counter_test/counter.v -d artix7 -p xc7a35tcpg236-1 
/bin/sh: 1: symbiflow_synth: not found 
Makefile:28: recipe for target 'build/top.eblif' failed make: *** [build/top.eblif] Error 127 
```
This error is found if you are not in the correct environment and try to create the examples. Another common error is that if you just run conda activate, it will tell you that the command is not found. You must first run these commands inside of the symbiflow-examples folder for conda activate to work correctly:
```
export INSTALL_DIR=$PWD/examples/xc7
export PATH="$INSTALL_DIR/install/bin:$PATH"
source "$INSTALL_DIR/conda/etc/profile.d/conda.sh" 
```
I was able to create a new example for the symbiflow example repo and I have created these steps to be able to create new examples.

1. The first step is to create your desired project in verilog files. The symbiflow tools can not support system verilog so all project files must be written in, or converted to, verilog. The verilog file in up_counter is called up_counter.v and had the following code: 
```
//----------------------------------------------------
// Design Name : up_counter 
// File Name : up_counter.v 
// Function : Up counter 
// Coder : Deepak 
//----------------------------------------------------
module up_counter ( out, // Output of the counter 
                    enable , // enable for counter 
                    clk , // clock Input 
                    reset // reset Input 
                  ); 
    //----------Output Ports--------------
    output [7:0] out; 

    //------------Input Ports--------------
    input enable, clk, reset; 

    //------------Internal Variables--------
    reg [7:0] out; 
    
    //-------------Code Starts Here-------

    wire bufg; 
    BUFG bufgctrl(.I(clk), .O(bufg));

    always @(posedge bufg) 
    if (reset) begin 
        out <= 8'b0 ; 
    end 
    else if (enable) begin 
        out <= out + 1; 
    end
endmodule 
```

2. The second step is to write the .PCF file. This file is the first half of the constraint file, which is the .XDC file for vivado projects. You must find a master .XDC file for the board you are working with, for that will be your reference for the .PCF file. In the following example of the format, what is in the { } are the variables or pins that you will need to add from the .XDC file and from the verilog files. The variables come from the verilog files of your project and the pins come from the .XDC file. There are two types of input and output variables. The first are the single input/output variables like buttons. The second are the variables with many inputs or output like leds and switches. Both are demonstrated in the example below.

The format for the .PCF file is as follows:
```
#clock constraint 
set_io {clock variable} {CLK pin} 
#input constraints for buttons, switches, etc 
set_io {input variable} {input pin} 
set_io {input variable[0]} {input pin} 
set_io {input variable[1]} {input pin} 
set_io {input variable[2]} {input pin} 
#output constraints for leds, 7 segment display, etc 
set_io {output variable} {output pin} 
set_io {output variable[0]} {output pin} 
set_io {output variable[1]} {output pin} 
set_io {output variable[2]} {output pin} 
```

Here is the .PCF file that I created for the up_coutner example named basys3.pcf:
```
# basys3 100 MHz CLK 
set_io clk W5

# enable correspond with btnC 
# reset corresponds with btnR 
set_io enable U18 set_io reset T17

# out[0:15] correspond with LD0-LD15 on the basys3 
set_io out[0] U16 
set_io out[1] E19 
set_io out[2] U19 
set_io out[3] V19 
set_io out[4] W18 
set_io out[5] U15 
set_io out[6] U14 
set_io out[7] V14
```

3. The 3rd step is creating the .SDC which is the second half of the .XDC file. I wasn’t able to test the .SDC files as well as the other files necessary for the symbiflow tool chain, but I was able to find a page in the symbiflow documentation that explains the .SDC files in detail. It is found at this website : https://symbiflow.readthedocs.io/en/latest/vtr-verilog-to-routing/doc/src/vpr/sdc_commands.html 

The .SDC file is mainly for creating the clock that the symbiflow tool chain will use during the generation of the project. What I found to make this file work properly is to add the following code to the top verilog file:
```
wire bufg; 
BUFG bufgctrl(.I(clk), .O(bufg)); 
```

And in the .SDC file you should add:
```
create_clock -period 10 bufg 
```

These lines of code work with single file projects without any problems, but I did not test them with multi file projects, but I believe that they should still work. The “wire bufg” portion can be changed to any variable name that you choose, but must be used in every place that uses the clk after the declaration in the verilog files. You will also need to change the variable name in the .SDC file.

The .SDC file in the up_counter was named counter.sdc and had the following code: 
```
create_clock -period 10 bufg 
```

4. The last step is to create the Makefile for the project. The easiest way to make the makefile is to use the makefile from an existing example that is similar to the one you are creating. You will need to change a few things but the majority of the makefile will not change. The “TOP:= {file.v }” should be changed to the name of your top verilog file. The reason for this is that while the tools are generating the intermediate files for the project, the important files will be named {file.v}.[filetype]. An example is “top.eblif”. The exception to this rule is when the tools are generating the .fasm. The .fasm file sometimes will be named after your top verilog file regardless of what you put in the “TOP:= {}”. This causes an error because the code will look for the name you specified but the tools generated the name of your verilog file. The easiest solution is to make the name you specified in the “TOP:=” section and the name of your top verilog file the same.

The next change you want to make is to the "VERILOG:=${current_dir}/{ file.v}" - this is where you put your verilog files. If you only have on file the format is:
```
VERILOG:=${current_dir}/{file.v}
```
If there are multiple verilog files the format is:
```
VERILOG := ${current_dir}/{file.v} \ 
    ${current_dir}/{file.v }\ 
    ${current_dir}/{file.v} \ 
    ${current_dir}/{file.v} 
```

The last two changes are to the “SDC:=” and the “PCF:=” which you will change to the names that you created for those files. These sections follow the same format as the “VERILOG:=”.

Here is the makefile that I used for the up_counter example:
```
mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST))) 
current_dir := $(patsubst %/,%,$(dir $(mkfile_path))) 
TOP:=up_counter VERILOG:=${current_dir}/up_counter.v 
DEVICE := xc7a50t_test 
BITSTREAM_DEVICE := artix7 
SDC:=${current_dir}/counter.sdc 
BUILDDIR:=build

ifeq ($(TARGET),arty_50) 
    PARTNAME := xc7a35tcsg324-1 
    PCF:=${current_dir}/arty.pcf 
else ifeq ($(TARGET),arty_100) 
    PARTNAME:= xc7a100tcsg324-1 
    PCF:=${current_dir}/arty.pcf 
    DEVICE:= xc7a100t_test 
else 
    PARTNAME:= xc7a35tcpg236-1 
    PCF:=${current_dir}/basys3.pcf 
endif

all: ${BUILDDIR}/${TOP}.bit

${BUILDDIR}:
    mkdir ${BUILDDIR}

${BUILDDIR}/${TOP}.eblif: | ${BUILDDIR} 
    cd ${BUILDDIR} && symbiflow_synth -t ${TOP} -v ${VERILOG} -d ${BITSTREAM_DEVICE} -p ${PARTNAME} 
    
${BUILDDIR}/${TOP}.net: ${BUILDDIR}/${TOP}.eblif 
    cd ${BUILDDIR} && symbiflow_pack -e ${TOP}.eblif -d ${DEVICE} -s ${SDC}

${BUILDDIR}/${TOP}.place: ${BUILDDIR}/${TOP}.net 
    cd ${BUILDDIR} && symbiflow_place -e ${TOP}.eblif -d ${DEVICE} -p ${PCF} -n ${TOP}.net -P ${PARTNAME} -s ${SDC} 2>&1 > /dev/null

${BUILDDIR}/${TOP}.route: ${BUILDDIR}/${TOP}.place 
    cd ${BUILDDIR} && symbiflow_route -e ${TOP}.eblif -d ${DEVICE} -s ${SDC} 2>&1 > /dev/null

${BUILDDIR}/${TOP}.fasm: ${BUILDDIR}/${TOP}.route 
    cd ${BUILDDIR} && symbiflow_write_fasm -e ${TOP}.eblif -d ${DEVICE}

${BUILDDIR}/${TOP}.bit: ${BUILDDIR}/${TOP}.fasm 
    cd ${BUILDDIR} && symbiflow_write_bitstream -d ${BITSTREAM_DEVICE} -f ${TOP}.fasm -p ${PARTNAME} -b ${TOP}.bit

clean:
    rm -rf ${BUILDDIR}
```
