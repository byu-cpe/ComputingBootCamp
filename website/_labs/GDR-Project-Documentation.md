# Size of Java Objects

**Shallow size** of an object is the amount of memory allocated to store the object itself, not taking into account the referenced objects. Shallow size of a regular (non-array) object depends on the number and types of its fields. Shallow size of an array depends on the array length and the type of its elements (objects, primitive types). Shallow size of a set of objects represents the sum of shallow sizes of all objects in the set.

**Retained size** of an object is its shallow size plus the shallow sizes of the objects that are accessible, directly or indirectly, only from this object. In other words, the retained size represents the amount of memory that will be freed by the garbage collector when this object is collected.

# Memory

## Part Used xc7a100tcsg324

The first three columns are from measuring process before and after loading the device. The other three columns are potential other ways of measuring the memory use of loading the device.

To get the value for the first and second column, process memory use was taken from the system monitor. The best way to implement this is to have a program what for user input before loading the device and then after to allow the user to locate the process. The easiest way to find the process is to short the processes list in the System Monitor by ID. To get the ID/PID of the java process, use jps. This will list all the java processes and what their ID/PID is. The third column is the difference between the second and first columns.

To get the memory usage from the program for the fourth column, we can get memory data from the runtime environment. To get the runtime object, use Runtime.getRuntime(). With the runtime object, it has function calls totalMemory() and freeMemory(). The difference between the return value of totalMemory and freeMemory is the memory that is being used. One thing to note, the JVM might decide to adjust how much memory it is using between the two calls. The steps to get data for the "from program" column is

1. Run garbage collection
2. Get the used memory from subtracting the totalMemory from freeMemory gotten from the Runtime object.
3. Load the device
4. Run garbage collection
5. Get the used memory from subtracting the totalMemory from freeMemory gotten from the Runtime object.
6. Subtract the used memory after loading the device from the used memory before loading the device

To get the retained memory for the fifth column, create a heap dump after the device is loaded with

* jmap -dump:live,format=b,file=/path/to/dump/file [pid]

To read the heap dump file, use Eclipse Memory Analyzer (MAT). The following directions uses version 1.10. To open a heap dump go to File > Open heap dump and navigate to where the heap dump is saved. Once the heap dump is open in MAT, choose to create a histogram from an arbitrary set of objects. Next select calculate the retained size. This will determine what the retained memory is for objects in the heap dump.

Sixth Column: To get the memory that is retained by the fields of an object, right click the object in the histogram view and select list objects > with outgoing references. Add up all the retained values that correspond to the objects fields.

All measured in MiB
| Process Before | Process After | Δ Process | From Program | Retained | Field Retained|
| --- | --- | --- | --- | --- | --- |
| 8.5 | 301.7 | 293.2 | 94.0 | 93.4 | 20.3 |
| 8.3 | 325.7 | 317.4 | 94.0 | 93.4 | 20.3 |
| 8.3 | 315.3 | 307.5 | 94.0 | 93.4 | 20.3 |
| 8.3 | 317.8 | 309.5 | 94.0 | 93.4 | 20.3 |
| 8.3 | 296.9 | 309.5 | 94.0 | 93.4 | 20.3 |

Since there is a large difference between the third column and the fourth/fifth column, it requires more effort to determine which is the accurate represent the amount of memory used by loading a Device file. One tool that can be used is visualVM and can be installed on Ubuntu with 

* sudo apt install visualvm

To start visualVM, type visualvm in the terminal. It is useful to install the startup profiler. 
```diff
- Need to go back and redo the process, had to something to get the plugins to apper but can't remember the process right now
```
VisualVM will list running java applications on the right with the name of the class that main is running in and its PID. Select the applicate you want to look at and then open the monitor.

Based on visualVM, the monitor is showing the used heap is ~100MB after the device is loaded and GC have taken place. This supports the conclusion that just measuring the difference in process memory usage from a system monitor does not provide an accurate view on the memory that objects use in a java program is actively using at any given time.

Using the runtime environment to estimate memory usage appears to be sufficient. However, when it is difficult to isolate desired object from surrounding objects, it would be beneficial to create a wrapper object for the target object and use a heap analyzer like MAT or visualVM and get the retained memory. However, since retained memory is a sum of shallow memories of what can be uniquely reached from a given object (in other words, the only way to get to them is through the given object), care must be taken to make sure all unwanted references to internal objects are removed.

(Time measurements taken on Windows 10, Ryzen 5 3600, 16GB 3600MHz Timing 16-19-19-39, WDS500G2B0C )

* Loading xc7a15tcpg236-3 1000 times took 288473 ms (avg: 288.473000)
* Loading xc7a100tcsg324-3 1000 times took 442011 ms (avg: 442.011000)
* Loading xc7a200tsbg484-3 1000 times took 859623 ms (avg: 859.623000)

# RapidSmith2 Notes

Tile.getWires() only return wires that originate or end in that tile, or in other words wires that are can be found with Connection.getSinkWire() or Connection.getSourceWire().
Wire.getConnections() will only return connections if the wire is connected to a pin (PIP, site pin, etc.) meaning that it does not return any connections that exists because it crosses unto another tile.

Takes 93 MiB to call getWires() on each tile.

## Comparing references

The following tables contain the results from comparing fields from objects of the same type. To compare the references, the == operator was use. If true was return, then the references point to the same object and is labeled as same in the table, else the references point to different objects and labeled as different.

### Comparing site references

Note: At this time, unsure if java is comparing references of Integer or the int it wraps

Unless otherwise noted, the following comparisons are made on the bottom site of the respective tile. This corresponds to the first element in the array of sites of the tile the site is located in (Site[] site field in the tile object).


#### Checking two tiles of the same tile type in the same column

Tiles: CLBLL_R_X21Y107, CLBLL_R_X21Y106

Comparing references in {Site SLICE_X32Y107} to {Site SLICE_X32Y106}
|Field Name|Field Type|Same|Dif|
|--|--|--|--|
|name|String||x|
|index|int||x|
|tile|Tile||x|
|instanceX|Integer|x||
|instanceY|Integer||x|
|bondedType|BondedType|x||
|template|SiteTemplate|x||
|possibleTypes|SiteType[]|x||
|externalWires|Map<SiteType, Map<String, Integer>>|x||
|externalWireToPinMap|Map<SiteType, Map<Integer, SitePinTemplate>>|x||

#### Checking two tiles of the same tile type in the same row

Tiles: CLBLL_R_X21Y107, CLBLL_R_X23Y107

Comparing references in {Site SLICE_X32Y107} to {Site SLICE_X36Y107}
|Field Name|Field Type|Same|Dif|
|--|--|--|--|
|name|String||x|
|index|int||x|
|tile|Tile||x|
|instanceX|Integer||x|
|instanceY|Integer|x||
|bondedType|BondedType|x||
|template|SiteTemplate|x||
|possibleTypes|SiteType[]|x||
|externalWires|Map<SiteType, Map<String, Integer>>|x||
|externalWireToPinMap|Map<SiteType, Map<Integer, SitePinTemplate>>|x||

#### Checking tiles with similar function on different side of a switch box tile

Tiles: CLBLL_R_X21Y107, CLBLM_L_X22Y107

Comparing references in {Site SLICE_X32Y107} to {Site SLICE_X34Y107}
|Field Name|Field Type|Same|Dif|
|--|--|--|--|
|name|String||x|
|index|int||x|
|tile|Tile||x|
|instanceX|Integer||x|
|instanceY|Integer|x||
|bondedType|BondedType|x||
|template|SiteTemplate||x|
|possibleTypes|SiteType[]||x|
|externalWires|Map<SiteType, Map<String, Integer>>||x|
|externalWireToPinMap|Map<SiteType, Map<Integer, SitePinTemplate>>||x|

#### Checking sites on same CLBLL_R tile

Comparing references in {Site SLICE_X32Y107} to {Site SLICE_X33Y107}
|Field Name|Field Type|Same|Dif|
|--|--|--|--|
|name|String||x|
|index|int||x|
|tile|Tile|x||
|instanceX|Integer||x|
|instanceY|Integer|x||
|bondedType|BondedType|x||
|template|SiteTemplate|x||
|possibleTypes|SiteType[]|x||
|externalWires|Map<SiteType, Map<String, Integer>>||x|
|externalWireToPinMap|Map<SiteType, Map<Integer, SitePinTemplate>>||x|

### Comparing references in tiles

#### Comparing references of tiles of the same type

Comparing references in CLBLL_R_X21Y107 to CLBLL_R_X21Y106
|Field Name|Field Type|Same|Dif|
|--|--|--|--|
|dev|Device|x||
|name|String||x|
|type|TileType|x||
|row|int||x|
|column|int||x|
|tileYCoordinate|int||x|
|tileXCoordinate|int||x|
|sites|Site[]||x|
|Individual Sites|Site||x|
|wireConnections|WireHashMap|x||
|reverseWireConnections|WireHashMap|x||
|wireSites|Map<Integer, Integer>|x||

#### Comparing references of tiles of similar function 
Comparing references in CLBLL_R_X21Y107 to CLBLM_L_X22Y107
|Field Name|Field Type|Same|Dif|
|--|--|--|--|
|dev|Device|x||
|name|String||x|
|type|TileType||x|
|row|int||x|
|column|int||x|
|tileYCoordinate|int||x|
|tileXCoordinate|int||x|
|sites|Site[]||x|
|Individual Sites|Site||x|
|wireConnections|WireHashMap||x|
|reverseWireConnections|WireHashMap||x|
|wireSites|Map<Integer, Integer>||x|

## Looking at shared objects

Using xc7a100tcsg324-3 as reference

Total tiles 30,932

INT_R/INT_L: 10,350 tiles

CLB: 7,925 tiles

Procedure: Using a map where the key is the object that being shared and the value being a set of objects that contain the key. Iterate through all interested holding objects and place them in the correct set.

### [wireConnections](https://github.com/byuccl/RapidSmith2/blob/master/src/main/java/edu/byu/ece/rapidSmith/device/Tile.java) (WireHashMap)

* Where can this object be found? Only found in Tile objects
* How often is this object reused? A majority are used only once, however a majority of tiles use the top five shared wireConnections. The following graphs show how the sharing of wireConnections. The first graph is where 1 to 13 tiles point to the same wireConnection object and the second graph for wireConnections that is pointed to by at least 14 tiles. This means that the farther to the right, the more shared a wireConnections is and the left the more unique the wireConnections is.  
* 5079 unique wireConnections
* Largest memory size ~190KiB (Used in PCIE_BOT_X104Y167)
* Smallest memory size 216B (Used in HCLK_CLB_X23Y182)


![alt text](./GoogleDeviceRepFigures/SharingOfwireConnections_Tile_per_wireConnections_1_to_13.png)
![alt text](./GoogleDeviceRepFigures/SharingOfwireConnections_Tile_per_wireConnections_14_to_max.png)

tiles per wireConnections: stats by tile type
||INT_R/INT_L|CLB|
|---|---|---|
|Mean|2.1513|660.4167|
|SD|2.0017|906.0772|
|Min|1|12|
|Max|15|2304|
|Median|1|79|
|25th Percentile|1|15|
|75th Percentile|3|1632|
|Unique wireConnections|4811|12|

For the most part, tiles that contain switch boxes (INT_R*/INT_L*) have unique wireConnections. From analyzing the CLB tiles that share wireConnections, it appears that the general rule is as long as it is not the top of a column of CLB, it references the same wireConnection that CLB type is referencing (CLBLL_L, CLBLL_R, CLBLM_L, etc. are considered different types of CLBs). Each unique wireConntions that are used by CLBs have a unique number of CLBs referencing that wireConnections.

![alt text](./GoogleDeviceRepFigures/SharingOfWireConnections_INT_Tile_per_group.png)

12492

#### What is a WireHashMap

A custom hash map implementation. It maps integers to arraies of WireConnection objects. According to documentation found the code, WireHashMaps are ment to only be used internally by RapidSmith and the user is not to use them directly. There are muliple public facing functions that uses wireConnections to gather information to perform their tasks.

### reverseWireConnections (WireHashMap)

* Where can this object be found? Only found in Tile objects
* Where is the object used? In the TileWire class.
* What is this object used for? Find driving connections
* 7472 unique reverseWireConnections
* Largest memory size ~183KiB (Used in PCIE_BOT_X104Y167)
* Smallest memory size 216B (Used in HCLK_CLB_X23Y182)

tiles per reverseWireConnections: stats by tile type

||INT_R/INT_L|CLB|
|---|---|---|
|Mean|1.4716|660.4167|
|SD|0.6144|906.0772|
|Min|1|12|
|Max|4|2304|
|Median|1|79|
|25th Percentile|1|15|
|75th Percentile|2|1632|

### wireSites (Map<Integer, Integer>)

* Where can this object be found? Only found in Tile objects
* 12009 Tiles do not have a wireSites (field is null)
* 404 unique wireSites (including null)
* Used to know which site in a tile a wire is connected to, which would explane why some tiles have this field be equal to null.
* Largest 124416 Bytes/2249 entries (PCIE_BOT_X104Y167)
* Smallest 4912 Bytes/2 Entries (INT_L_X6Y10)

While most wireSites are used uniquely, 12009 tiles does not have wireSites defined (value set as null) and 3 wireSites are used by at least 3148 tiles totaling 18,221. This 58.9% of tiles uses one of 3 wireSites and 38.8% of tiles has wireSites set as null;

Mean: 76.5644

SD: 834.3086

Min: 1

Max: 12009

Median: 1

25th Percentile: 1

75th Percentile: 1

## Sites

### externalWires (Map<SiteType, Map<String, Integer>>)

* Used internally by sites as part of creating cite pins. 

* Method for determining the largest and the smallest: Since externalWires is a map whoes value is also a map, the largest externalWires object is assumed to be the one which the sum of the map size and the value map sizes is the greatest. The same methodology was used to find the smallest. 
* Largest: 276600 Bytes (PCIE_X0Y0)
* Smallest 384 Bytes (K9)


Mean: 28.9858

SD: 416.4914

Min: 1

Max: 10350

Median: 1

25th Percentile: 1

75th Percentile: 1

Total Sites: 28551

Number of entries: 985

## Trend

The general trend appears that majority of objects (both Java and RapidSmith) that could be shared are only referenced by one RapidSmith object, however there is a handful of objects that is referenced by many RapidSmith objects.

### template (SiteTemplate)

Mean: 648.8864
SD: 2322.3519
Min: 1
Max: 11100
Median: 16
25th Percentile: 2
75th Percentile: 135
Total Sites: 28551
Number of entries: 44
