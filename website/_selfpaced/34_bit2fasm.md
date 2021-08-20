---
layout: page
toc: false
title: bit2fasm
slug: bit2fasm
type: fpga_opensource
order: 5
---

## Overview

"bit2fasm" is a tool within [Project X-Ray](https://byu-cpe.github.io/ComputingBootCamp/tutorials/xray/) that converts a bitstream (.bit file) into [FASM](https://byu-cpe.github.io/ComputingBootCamp/tutorials/fasm/) lines. 

This page provides details on how the `bit2fasm.py` script works within Project X-Ray. There are two primary sections of this description. The first, [Code](#code), describes the various files and functions used to perform the bit2fasm operations. The second, [Data Structures](#data-structures), describes the data structures used by the code. 

## Install

Follow the instructions for installing [Project X-Ray](https://byu-cpe.github.io/ComputingBootCamp/tutorials/xray/). 

## Code

### bit2fasm.py

The [bit2fasm.py](https://github.com/SymbiFlow/prjxray/blob/master/utils/bit2fasm.py) Python file contains the "main" function for the bit2fasm program. It isn't a very big file and most of the actual work is done by other files in the Project X-Ray repository.

To run the executable, the Project X-Ray Environment Variables (see below) need to be set as the code will use these variables to acccess the appropriate databases. 

The arguments for running this Python executable are summarized below:
```
usage: bit2fasm.py [-h] [--db-root DB_ROOT] [--bits-file BITS_FILE]
                  [--part PART] [--bitread BITREAD]
                  [--frame_range FRAME_RANGE] [--verbose] [--canonical]
                  bit_file
```

Here is an example of how to run the executable:

```
python bit2fasm.py <bitfile.bit>
```

### Functions

There are three crucial functions used within this file to achieve bit2fasm functionality. Each function is described below.

**main()**

This main function primarily manages arguments and uses the Python Argument Parser called argparse. The primary input is the Xilinx .bin bitstream.

**bit_to_bits()**

Once all the arguments are parsed, the `bit_to_bits` Python function is called. This function parses the Xilinx bitstream and generates a new text-based version of the bitstream. This function actually creates an intermediate file that gets deleted at the end of execution. If you want to see the file that is created, use the `--bitread` option in the command line:

```
python bit2fasm.py --bitread <bitread.txt> <bitfile.bit>
```

This function calls the executable `bitread` which is a C program used for parsing Xilinx bitfiles (see [bitread.cc](https://github.com/SymbiFlow/prjxray/blob/master/tools/bitread.cc)). The bitread executable is located in the `~prjxray/build/tools` directory. It calls this C program within Python using the Python subprocess library and the following options:

```
bitread <part yaml file> <frame range=None> -o <output bits file> -z -y <input Xilnx bitfile>
```

The '-z' option skips zero frames (or frames with all bits cleared) and the '-y' option uses the text "bit" format shown as an example below. Here is a sample from a "bits" file after this step:

```
bit_00420019_099_21
bit_0042001d_098_13
bit_0042001e_100_09
bit_00420020_099_16
```

### bits_to_fasm

After creating a 'bits' file, the 'bits_to_fasm' function is called. This function directs the main work of dissasembly. The function performs the following steps:
  1. It creates the [Database](#database) object
  2. It creates the [Grid](#grid) object (by calling db.grid)
  3. It creates [FasmDisassembler](#fasmdisassembler) object

After these objects are made, a [Bits File](#bits-file) is read and parsed using the `load_bitdata` function in the [bitstream.py](https://github.com/SymbiFlow/prjxray/blob/master/prjxray/bitstream.py) file. The result is a dictionary (called `bitdata`) between a frame_Address and two sets. The first set are the word columns that have any bits set in the bitstream and the second set are the bit indicies within the frame (not the word). The bit index references a specific bit within a frame and not within the word.

### More Functions

Next, the [find_features_in_bitstream](#find_features_in_bitstream) function is called in FasmDisassembler.

### find_features_in_bitstream

This is in the [FasmDisassembler](#fasmdisassembler) object.

The input to this function is a "bitdata" dictionary (see [bits_to_fasm](#bits_to_fasm)) that contains the bits we want to find features for. The key is a frame address and the two values are arrays: value[0] is a set of words and value[1] is a set of bits within the word. Value[i] forms a unique pair of word and bit indicating a specific bit within a frame address. The algorithm works as follows:

  * Iterate over all frames (keys) in the bitdata dictionary
    * Using the [SegmentMap](#segmentmap), iterate over all [BitsInfo](#bitsinfo) objects from the device that reference the given frame.
      * Iterate over the range of words in the given device BitsInfo object. If any of the words in the features bitdata[frame][0] fall within this range of the device info, continue. Otherwise continue iterating (i.e., the given BitsInfo object doesn't relate to any of the bits in the bitdata so skip).
        * Call [find_features_in_tile](#find_features_in_tile).Iterate over all fasm_line objects obtained from calling the function.


### find_features_in_tile

Input:
  * tile: Tile we are looking at
  * block_type: The block type we are looking at
  * bits: BitsInfo object from the SegmentTree that matched against the bitdata.
  * solved_bitdata
  * bitdata: This is the dictionary passed into the find_features_in_bitstream that contains all of the bits we seek to find
  * verbose=False

### match_bitdata

In the [tile_segbits.py](https://github.com/SymbiFlow/prjxray/blob/master/prjxray/tile_segbits.py) file.

### Database

The Database object is a container that houses information about the database files. It doesn't actually parse all of the data but rather combines all of the filenames used in the database into a single object so the data can be easily accessed later. This Python class is defined in the [db.py](https://github.com/SymbiFlow/prjxray/blob/master/prjxray/db.py) file.

There are many variables in the Database object but only a few of them are set in the constructor. The others are set on demand when member functions are called. The constructor iterates through all of the files in the corresponding Database directory and creates an object, organizing them. The following variables are set in the constructor:
  * db_root
  * part
  * tile_types (a dictionary between a text tile type in upper case and a [TileDbs](#tiledbs) object)
  * site_types (a dictionary between text site name and the corresponding filename)
  * required_features (a dictionary between the part name and a set of features)

The following variables are set as methods are called to access more information about the database:
  * tile_segbits: a dictionary with a key of the tilename and value of 

### TileDbs

A namedtuple (TileDbs) that encapsulates all of the database filenames associated with a specific tile type. It contains the following fields:
  * segbits: filename of segbits file
  * block_ram_segbits: filename of blockram segbits file
  * ppips: filename of ppips file
  * mask: filename of maskfile
  * tile_type: tile_type string (taken from the tile_type_<name>.json filename)

### Grid

A Python class object that represents the tilegrid for a given part. This Python class is defined in the [grid.py](https://github.com/SymbiFlow/prjxray/blob/master/prjxray/grid.py) file.

This class is created by first creating a Python json object from the corresponding tilegrid.json file (self.tilegrid). It manages a set of [GridInfo](#gridinfo) objects for the device.
  * tilegrid: json object
  * loc: a dictionary between a "grid_loc" object and a tile name (to go from coordinate to tile)
  * tileinfo: a dictionary where the key is the tile name and the value is GridInfo object 

### GridLoc

Defined in [grid_types.py](https://github.com/SymbiFlow/prjxray/blob/master/prjxray/grid_types.py) file. A named tuple with fields: 
  * **grid_x**
  * **grid_y**

### GridInfo

Defined in [grid_types.py](https://github.com/SymbiFlow/prjxray/blob/master/prjxray/grid_types.py) file. A named tuple with fields:
  * **bits** <!--A dictionary between a segment_type (block type) and a [Bits](#bits) object.->
  * **sites**
  * **prohibited_sites**
  * **tile_type**
  * **pin_functions**
  * **clock_region**

### Bits

Defined in [grid_types.py](https://github.com/SymbiFlow/prjxray/blob/master/prjxray/grid_types.py) file. A named tuple that stores the "bit" information within a tile .json using the following fields:
  * **base_address**
  * **frames**
  * **offset**
  * **words**
  * **alias**

### SegmentMap

Defined in [segment_map.py](https://github.com/SymbiFlow/prjxray/blob/master/prjxray/segment_map.py) file. A Python class that contains a Python "IntervalTree" object. The purpose of this class is to facilitate lookup of BitsInfo objects based on the base address.

The object is constructed by iterating over all of the tiles in the Grid object and creating a [BitsInfo](#bitsinfo) object for each tile/block_type pair. An Interval is added to the IntervalTree with the 'begin' being the base address, the 'end' is the base address + # frames (not #frames - 1). The data in the interval is the corresponding [BitsInfo](#bitsinfo) object.

### BitsInfo

Defined in [grid_types.py](https://github.com/SymbiFlow/prjxray/blob/master/prjxray/grid_types.py) file. A named tuple that is used as the data object within an interval of the [SegmentMap](#segmentmap) object. This object associates a block_type, tile, and [Bits](#bits) object together. The fields are:
  * **block_type**: String block type
  * **tile**: Tile name
  * **bits**: The [Bits](#bits) object associated with this block type in the tile

### FasmDisassembler

The FasmDisassembler object is key for the bitstream feature extraction. This Python class is defined in the [fasm_disassembler.py](https://github.com/SymbiFlow/prjxray/blob/master/prjxray/fasm_disassembler.py) file. The purpose of the FasmDisassembler constructor is to create a number of important objects used in the disassembly process. The following three objects are created in the constructor:

  * [Bitstream Database](#database)
  * [Grid](#grid)
  * [SegmentMap](#segmentmap)

### TileSegbits

This python class is defined in the file [tile_segbits.py](https://github.com/SymbiFlow/prjxray/blob/master/prjxray/tile_segbits.py). Objects of this class are created upon demand through the Grid.get_tile_segbits_at_tilename(tile_name) function. This object is owned by the 'Database' object (although accessed by the Grid object using the Database object).

Variables within the class:
  * segbits: A dictionary with key the name of the resource (CLBM_L.....) and the value is a set of [Bit](#bit) objects.
  * ppips
  * feature_addresses

### Bit

This is a named tuple defined in the [tile_segbits.py](https://github.com/SymbiFlow/prjxray/blob/master/prjxray/tile_segbits.py) file. The fields are:
  * word_column
  * word_bit
  * isset

They represent strings such as "29_14".


## Data Structures

This section summarizes the data structures and file formats used within the bit2fasm flow.

### Xilinx .bin Bitstream
This is the bitstream created by the Vivado tools and in the .bin format. It is binary, has a header, and is made up of command sequences. 

### Bits file
A textfile representation of the bitstream that is generated from the `bitread` executable using the '-y' and '-z' options. Here is a sample from a 'bits' file:

```
bit_00420019_099_21
bit_0042001d_098_13
bit_0042001e_100_09
bit_00420020_099_16
```

### tilegrid.json file

Devices of the same family share the same database directory but each device has its own unique "tilegrid.json" file. This file represents the grid of tiles used to make the unique part. The tile grid is represented in the .json format and is essentially a list of "tiles". Each tile is represented as follows:

  * **tile name:** A unique text string that represents a unique tile. The tile name has X & Y coordinates embedded within them. The coordiante system of these coordinates seems to be some logical representation and does not refer to actual physical locations (example: BRAM_INT_INTERFACE_L_X6Y2)
    * **tile type**: a string that indicates tile type. There should be a corresponding file named "tile_type_<type>.json" in the database directory.
    * **grid_x:** numerical grid x position (not the same coordinate system as the tile name)
    * **grid_y**: numerical grid y position
    * **pin_functions**
    * **prohibited_sites**
    * **sites**: contains a list of unique sites within the tile. Each site is specified by a key/value pair where "key" is the unique site name and the "value" is the site type.
    * **bits**: bitstream information (can be empty). Contains a list of named objects with corresponding bitstream info. Multiple named objects may exist.
      * **name**: A Block type name that has bits
        * **alias**
        * **baseaddr**: The base frame address in the bitstream of the object.
        * **frames**: The number of sequential frames in the current column that have bitstream information for this resource.
        * **offset**: The number of words in the frame in which bits for this resource starts.
        * **words**: The number of sequential words in the frame.
    * **clock_region**: String indicating which "clock region" the tile belongs to. This string is in the form "X<X loc>Y<Y loc>". Clock region
                     coordinate system.


### Project X-Ray Environment Variables

When opening a new terminal, the following command must be ran from the Project X-Ray directory to use Project X-Ray tools:

```
source settings/<part_famliy_name>.sh
```

After running the command above, the command `env` can be used to verify that the correct part is loaded into an environment variable. The command above sets several environment variables, which can all be seen (along with all other environment variables) by simply typing `env` in the terminal. To check one of the environment variables used by the tool, run `printenv XRAY_PART_YAML`, and a path to a part.yaml file should be printed.


## Follow-Up Activities:

If you performed the activities from the FASM module, you should now possess a bitstream and a FASM file for a 2-input AND gate (or design of your choice. Once again, the 2-input AND gate will be the design being referenced in this section, so adjust the instructions accordingly if your design differs.)

Before beginning, you should make sure the part you used matches the same part you're using in your environment variables (look inside the `settings/<part_famliy_name>.sh` script you ran, or run the command `printenv XRAY_PART`. It might not be important what part you're using, so the easiest route is to just match Vivado to whatever part is in the settings script).

### Change It Up

After finding the FASM lines corresponding to the logic that implemented the AND gate, go back and change up your design. Change the design to a 3-input AND gate, generate the bitstream and FASM file and compare the differences in logic to your original design. Do the same thing, but change your design instead to a 2-input OR gate and compare the differences once more to your two AND gate FASM files. 

### Spot the LUT 

Open up the Implemented Design feature in Vivado (for any of your designs) and look at the device GUI. Try to find the LUT that implements the logic in your design by looking at the Site/Slice location. Try to find one of the interconnects in the design as well. 

## Learn More

* Python ArgParse Documentation - <https://docs.python.org/3/library/argparse.html>
* JSON Documentation - <https://www.json.org/json-en.html>

