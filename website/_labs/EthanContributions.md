*This page is a place where Ethan Rogers will upload contributions before a better place is found for them.*
# SymbiFlow
*SymbiFlow contains many repos that are all used to help with fpga development - found at https://github.com/SymbiFlow*
## prjxray
*can be found at https://github.com/SymbiFlow/prjxray.git*

## fasm2bels
*can be found at https://github.com/SymbiFlow/symbiflow-xc-fasm2bels.git*


## PRJXRAY NOTES:

### X-Ray ARTIX7 Database html page
file:///home/erogers/workspaces/prjxray/htmlgen/html/artix7/index.html  
The above link contains the TILEGRID of an Artix7 xc7a100tfgg676-1 part

### tilegrid.json - 
Contains the tilegrid specific to a PART.  
Tiles in this file can be found in the X-Ray ARTIX7 Database html page

### tile_type_BRAM_L.json (or others of similar form)  
Found in the prjxray/database/artix7 directory  
Specific to Artix7  

### Misc.  
If you want to use FASM2BELS, you will need Python3.7 or greater.

### Setting up a virtualenv for Python3.7  
Run the following command in the directory you would like your virtual environment to live.  
`python3.7 -m venv venv3.7 --without-pip`  
This will create the virtual environment without pip. If you remove the `--without-pip` argument, you may run into issues.  
  
To install pip in your new virtual environment, activate the environment with `source activate` within it's bin directory.  
Once the environment is activated, run:  
`curl https://bootstrap.pypa.io/get-pip.py | python`  
This will install pip, and you should be good to go!

# Building the Connections database (Symbiflow)  
`python3 -mfasm2bels --connection_database=/home/erogers/workspaces/symbiflow-xc-fasm2bels/fasm2bels/database/connection_database.db --db_root=/home/erogers/workspaces/prjxray/database/artix7 --part=xc7a35tcpg236-1 --fasm_file=/home/erogers/workspaces/fasm/examples/many.fasm --verilog_file test_v.v`

### Combine cd and ls into one command: cs
Place the following at the end of your ~/.bashrc file:  
`cs() { if [ $# -eq 0 ]; then ls; else cd $1 && ls; fi }`

