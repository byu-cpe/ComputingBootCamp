# Instructions for acquiring and working with RapidSmith2

1. Learn git so you feel comfortable with it.   [Here is a link to our GIT reference wiki page](https://github.com/byuccl/GoogleDeviceRep/wiki/Git#git-reference-materials).
1. Download RapidSmith2 from https://github.com/byuccl/RapidSmith2
1. Configure it for your work environment (Intellij, Eclipse, VS Code, gradle, command line).  See below for more instructions.
1. Work your way through the documents and the tutorials in them.
1. Checkpoint review: what has been done/learned, identify next set of experiments.

# Install Steps for RapidSmith2
* You don't have to install TINCR first, you can do it later...

1. Get a copy of RapidSmith2 using: `git clone https://github.com/byuccl/RapidSmith2`
1. Set an environment variable in your .bashrc file to point to it:  
`export RAPIDSMITH_PATH=~/RapidSmith2`  
You do this by editing the .bashrc file in your home directory and adding the above command to the bottom.  It (the .bashrc file) will then get executed every time you log in and start up a terminal.  Kill your terminal and re-start to have it take effect.  Or do: `source ~/.bashrc` in your open terminal.

### Method #1: If You Intend to Run RapidSmith2 from VS Code

This is the highly recommended way.

1. Start VS Code.
1. Make sure you have installed the 'Java Extension Pack' into your VS Code setup.
1. Open up `src/main/java/edu/byu/ece/rapidSmith/examples/DesignAnalyzer.java`.
1. From the VS Code menu, select `Run->Run Without Debugging` and you should get the following message:  
`Usage: DesignAnalyzer tincrCheckpointName`  
meaning you forgot to provide the needed command line parameter.  This indicates everything is set up for it to run.  (NOTE: you may get a build failed message about other items in the repo not compiling, you may click 'Proceed' to ignore those.)
1. Now try `CreateDesignExample.java` and `DeviceAnalyzer.java`.  They should run and produce output since they needs no command line parameters.
1. Go back to `DesignAnalyzer.java` and edit the usage error message in some way and re-run and verify that your changes are reflected.  In this case, VS Code has compiled RapidSmith and placed the .class files into `$RAPIDSMITH_PATH/bin/main` and is running them from there.  

We know that Java requires a CLASSPATH so how is this all working without your creating one?  RapidSmith2 comes with its own gradle build files.  VS Code sees those gradle files and, from them, derives the needed dependencies on external JAR files.  It also decides it will put all its compiled source files (the .class files) into `$RAPIDSMITH_PATH/bin/main` - go look for them and you will see them.  Thus, running with VS Code  is quite seamless.

How to get rid of all the other error messages when you build?   Parts of RapidSmith2 rely on some .jar files in `$RAPIDSMITH_PATH/jars`. You need to add them to VS Code (search below for _referencedLibraries_).  This will remove some but there are some files within RapidSmith2 that have compilation errors.  With other IDE's like Eclipse and others you would get an initial compile error and after that the IDE would ignore those (since we are not trying to run them).  VS Code seems to be quite insistent on reminding you regularly, which makes it essentiall impossible to see if your program has compiled correctly (if your program fails to compile it will print a message, which might be easily missed among the torrent of output, and then execute the old .class file - that can be very confusing).  To fix this, you can do the following: (1) in the Explorer (left side), red marks directories with files with compilation errors in them and red also marks files with compilation errors in them.  Right-click the files that show compilation errors and select Delete.  Then, try to run again and new ones will turn red (files that depended on those you just deleted).  Repeat this until there are no more compilation errors.  Why is this OK?  Remember, this is all based on git and so if needed you can always retrieve the deleted files.  And, since those files you deleted wouldn't compile, they must not be needed for what we are doing...

_And, here is a trick for running programs that generate output.  The terminal window within VS Code can get filled with tons of output.  When scrolling up it can be hard to figure out where the previous run's output stops and the new run's output starts.  Also, each time yu do things, new terminals start inside the old ones.  If you exit the terminal window completely (type `exit` or `CTRL-D`) repeatedly, it will terminate them all and a new clean one will appear when you run again.  Now, when you run your program you know that the only thing in the terminal window is the output from that program's run.  And, if youdon't want to run again, you can always open up a new terminal with CTRL-` (control backquote)._

### Method #2: If You Also Want to Run From the Command Line

While this method is not recommended, it is instructive to do to actually learn about CLASSPATHs and how java runs.  So work your way through it.

You can use the compiled files that VS Code creates but you will need to get the required dependencies.  And, you will need a CLASSPATH to point to them all.
1. Now from the command line (inside RapidSmith2) run:  
`java edu.byu.ece.rapidSmith.examples.DesignAnalyzer`  
You should get a 'class not found error' since java doesn't know where to find the .class file for that.
1. Now, execute the following:  
`export CLASSPATH="$RAPIDSMITH_PATH/bin/main"`  
This will put the .class files on to CLASSPATH. 
1. Redo the above command in #1.  You should now get a different error message.  The DesignAnalyzer.class file was found but it needs a jdom library which is not found.
1. Go to https://byu.box.com/s/1cvhqnwjtivvmpfv64okwazc2yw8uhou and download that file.  It should be called `RS2.jar`.  Put it into your `$RAPIDSMITH_PATH/jars` directory.
1. Now execute the following to tell java to also look in that file:  
`export CLASSPATH="$RAPIDSMITH_PATH/bin/main:$RAPIDSMITH_PATH/jars/RS2.jar"`.  
Now, when you run as above in #1 you should get the Usage error, meaning the program ran but you didn't provide the needed input parameters.
1. If you choose to run this way you will be relying on VS Code to compile the programs and put the results in `bin`.
1. At this point, go back and add the above `export` command to the bottom of your .bashrc file in your home directory.  This will cause that command to be executed every time you log in.
1. Finally, if  you choose to write your own programs, you will want to put `.` at the start of your classpath by dding the following to the bottom of your .bashrc file:  
``export CLASSPATH=.:$CLASSPATH``  
(or modify the original statement in the .bashrc to include . as well).  
You can then write them anywhere and compile them, and if they are in the current directory they will run.

### Method #3: If You Just Want to Run the Pre-Compiled RapidSmith2 Code
This is the recommended method if yo have no plans to do any editing of the RapidSmith2 code.

Finally, what about if you have no plans on editing the RapidSmith2 code but just want to run RapidSmith2 as it came from github?  You can execute `./gradlew build` and it will build the entire thing (takes about 5 minutes, be patient - it will stick at 78% done for 3+ minutes).  

This will build the project and deposit a bunch of things in the `build/install/RapidSmith2` directory.  One of those is a big .jar file.  If you put that on your path (instead of the $RAPIDSMITH_PATH/bin/main and instead of the $RAPIDSMITH_PATH/jars/RS2.jar) that is all you need to run. 

One last thing before we continue, why the RS2.jar file at the link above that you had to download?  RapidSmith2 was really created with 2 execution models in mind (our first method above).  One is to use an IDE like Eclipse or VS Code for if you wanted to modify and recompile the RapidSmith2 code.  The other is to use gradle to build a finished JAR that you just point to (our third method).  

What about the second method where you edit the RapidSmith2 source code and compile using VS Code but want to run the executables from the command line?  There really is not a good reason to do so - if you are editing the code then run from within your IDE.  If you are not editing then let gradle build the big JAR file for you.    If you use the second method you need to tell java where both the .class files are as well as where all the external .jar files are for execution.  

The RS2.jar file from above contains all the external .jar files (that both gradle and VS Code know how to automagically fetch for you).  The RS2.jar file was created by hand to simply contain all of the jar files from `build/install/RapidSmith2/lib`.  Alternatively, you could have put all the .jar files there onto your CLASSPATH.

If you want to see all that is in the RS2.jar file, execute: `jar tf RS2.jar` and see what comes out...  It is essentially the contents of all the .jar files from `build/install/RapidSmith2/lib`.  

At this point, wander around the RapidSmith2 code base.  Some things to do include:

1. Look at all the packages for design, device, examples, ...
1. Go in and look at all the programs in the `examples` directory.  
1. Some of them (at least 2) can be run without supplying any Vivado designs.  Some require a Vivado design.  Run the ones you can without a Vivado design.
1. Look at the outputs provided by the ones you can run.  What are they generating?

# Installing Tincr
* RapidSmith2 uses another tool called Tincr to interact with Vivado. Tincr is able to output designs that have been synthesized up to the point where they have been placed and routed on a FPGA. Also, tincr is able to take files generated by RapidSmith2 and import them into vivado. Tincr can be found [here](https://github.com/byuccl/tincr)

* There are some steps required to be able to use Tincr.  Look in `$TINCR_PATH/README.md` for instructions (also found on the github page for Tincr).  One step is to create an environment variable call TINCR_PATH and set it equal to the path for the root directory of Tincr. This should be an absolute path (starting from the root directory). To create an environment variable edit ~/.bashrc and add this to the bottom:
``export TINCR_PATH=where-ever-you-put-Tincr``

* Another thing the `README.md` file will tell you is to copy the `$TINCR_PATH/install/pkgIndex.tcl` file to your Vivado installation.  Do that.

* You can check that Tincr is installed correctly. Start Vivado in Tcl mode and you type `package require tincr`.  If it is installed, Vivado will print out '0.0', which is the Tincr package version number.

# Continuing On with RapidSmith2
* You can tell tell VS Code what .jar files to add to its internal classpath if you don't have a gradle build setup for your project (while we do have a gradle build setup, it is useful to know how to do this for cases where you don't).  Edit the `settings.json` file (you can get to it by opening up the VS Code Command pallete and searching for 'open settings').  You may already have an entry there for `java.project.referencedLibraries`. If so, add the .jar files to its entry.  If not, right before the final right curly brace add ``"java.project.referencedLibraries": [path_to_jars]``. 

* A very common way for code to be documented in java is with javadoc strings that can be used to produce documentation that is viewable in a internet browser. RapidSmith2 is documented with javadoc strings, however the project files does not have the javadoc documentation. This means we need to generate it ourselves. To generate them, have a terminal navigated to the root of the RapidSmith2 and then run 
`` javadoc -d ./javadocs -sourcepath src/main/java -subpackages edu.byu.ece.rapidSmith ``.
It will throw multiple warnings, but it will still generate the javadocs. To change where the javadocs are saved, simply changed the argument after the -d flag. To open the javadocs, open javadocs/index.html in a browser (choose `File->Open File` in a browser and it will open it).  If you have never worked with documentation like this before, it will list all the packages in RapidSmith2.  

* What if you want to write a program using VS Code but you want all the RapidSmith2 source code available to look at or modify with print statements as you go?  Here is a suggestion: go into the `src/main/java` directory and create your own directory and put your files there.  Your program will be embedded in the RapidSmith2 repository and you won't have to do anything else to interact with the RapidSmith2 source code.  Here is an example inside `src/main/java/bootcamp`:  
```
package bootcamp;

import java.io.IOException;
import org.jdom2.JDOMException;
import edu.byu.ece.rapidSmith.examples.DeviceAnalyzer;

public class test {

    public static void main(String[] args) throws IOException, JDOMException {
        DeviceAnalyzer.main(null);
    }
    
}
```   
It doesn't do much other than call DeviceAnalyzer but it shows how to write your own program that interacts with the RapidSmith2 code base.

# Generating designs for RapidSmith2
Go into the `exampleVivadoDesigns` directory.  There, you will find a number of sub-directories containing sample designs.  The design itself lives in a subdirectory with its top level module's name. 

In that directory there is also a `compile.tcl` file.  Look through its contents - it ought to look familiar - the Tcl command to compile files you learned about back in the Tcl bootcamp activity was based on it.  But, it has some significant differences.  Carefully look through it to see.  The main difference is it expects the source files for design `someDesign` to reside in a directory of that name (you run the script from outside the directory).  And, when it runs it generates not only a Vivado checkpoint(a .dcp file) but also a RapidSmith2 checkpoint (a .rscp file).   If you run one of them you can then run some of the example programs that require a checkpoint on it.  

Note that at the top of the file there is `package require tincr` - that is required to load the Tincr library so that you can generate a RapidSmith2 checkpoint from your Vivado design.

For example, start Vivado in -tcl mode, source `compile.tcl`, and compile the `add` design by calling `compile add`.  Then run DesignAnalyzer and pass it the name of the .rscp that is generated.  You should be able to compare what is in the .sv files with what the program prints out.  

To run this, you will have to figure out how to tell VS Code how to provide a command line parameter when you execute the program (search the web).  In VS Code, click the debugging icon on the left side of the screen (a triangle with a little bug on it).  At the top of that will be a drop down bo with all the run configurations VS Code has created for the programs in this directory.  Choose the Debug Launch for `DesignAnalyzer`, then hit the settings gear icon next to it.  It will open up the `launch.json` file for this run configuration.  You can add an args entry for that run configuration like this:   
```
{
            "type": "java",
            "name": "Debug (Launch)-DesignAnalyzer<RapidSmith2>",
            "request": "launch",
            "mainClass": "edu.byu.ece.rapidSmith.examples.DesignAnalyzer",
            "projectName": "RapidSmith2",
            "args": ["/home/nelson/RapidSmith2/exampleVivadoDesigns/add.rscp"]
        },
```   
Then, when you hit run next to the drop down box it will run `DesignAnalyzer` with the provided argument.

Note that `compile.tcl` as distributed does not place or route the design, it just synthesizes it.  So, when you run `DesignAnalyzer` it will say that nothing is placed or routed.  Go into `compile.tcl` and uncomment the place and route commands and re-run and see what you get.  The add design is so simple that it is hard to even find any real cells in it besides input and output cells and buffers.  Search for `LUT3` to find one of the LUTs in the design.

Now try out a few more and see what you can learn.  They are already compiled - count16 is a good one but its output is very long.  And, the terminal in VS Code (where the output is displayed) is limited to 1000 lines of history.  You can change the setting `terminal.integrated.scrollback` in VS Code to be longer (look on the web for instructions on how to set VS Code settings - you open up the settings window with a multi-key combination and search for scrollback.  This is CMD, on a Mac, not sure what you use for Windows or Linux.  Also, see above (search for `exit`) on how to get a clean terminal to avoid cluttered output.

After running count16, make your own 2-bit counter (it lives in it own directory and has strict rules on the name of the directory must match the name of the top level module in your design for `compile.tcl` to work).  Something this small should produce output that is quite readable.

_Another reason to run VS Code on your own machine and use it to SSH into the VM - the hotkey combinations for most/many of the things you want to do in VS Code don't work when you run VS Code inside the Linux VM - they have been remapped.  Painful, and it will come back and bite you often until you just bite the bullet and start running VS Code on your own machine (where the key mappings for ALT and the like are known) and SSH into the VM_.

# Some Mini-Projects
* Open up the `javadocs` that you generated above.  Choose a package - try `edu.byu.ece.rapidSmith.design.subsite` (this contains much of the good stuff about RapidSmith2 designs)).  You will see entries for all the packages inside it (select `Cell`).  Look through the methods in this class.  Find `getBEL()`?  What does it do?  Look for other interesting methods such as: `getInputPins()`, `getName()`, `getPin()`, `getType()`, `getProperties()`, etc.  What do they all do?  Next look at `edu.byu.ecerapidSmith.design.subsite.CellDesign`.  What method call would you use to get a list of all the cells in a given design?  How would I add a new cell to a design?

* Now, go in and read through the program `edu.byu.ece.rapidSmith.examples.DesignAnalyzer`.  Do you see how it opens a design and iterates across all the dells in the design?  What does the `prettyPrintCell()` routine do?  It is bit complex in that while it prints out everything about a cell, there are `if` statements in it to handle 'normal' cells, macro cells, and macro internal cells.  Once you get through all that logic, you should be able to see that it basically  prints out the characteristics of the cell including its name, placement location (if placed), etc.  It then prints out all the cell's pins - look at the different pin characteristics it prints (name, direction, net connected to that pin, etc).  

* Similarly, the program also prints out everything about the nets in the design (name, pins on cells it is connected to, etc).  It also prints out the `RouteTree` associated with the net - this is how a routed net is represented.  You will remember from your Tcl experiments that a routed net in Vivado has PIPs associated with it.  However, in RapidSmith2, that is abstracted away into a `RouteTree` data structure which is a tree where the root of the tree is the cell pin that drives the net and the structure of the tree shows the the structure of the net's route (each element in the `RouteTree` is one of the wires making up the routed net.  You could say it is the opposite of how Vivado represents it - from the PIPs in Vivado's representation you can infer the various wire segments in the routed net.  But here, from the wire segments in the `RouteTree` you can infer what the PIPs were.

* Now, modify the DesignAnalyzer program to print out some additional information regarding the design, its cells, and nets or change the way the existing information is printed out.  Then, run the modified program.

* Similarly, look through the `DeviceAnalyzer` program.  It is much less extensive than `DesignAnalyzer`, printing out a few things about two of the tiles in the design.  Can you modify it to be similar to the Tcl program you wrote earlier that printed out information about a device, a switchbox, etc?  Run your resulting program.

* You will note that `DeviceAnalyzer` is hard-wired to print out information about a specific part.  Can you change it so that the name of the device to analyze is passed in as a command line parameter to its `main()` routine?  Then, look through the `RapidSmith2/devices` directory to see what 2 other devices you could try to run the program on (they candidate devices are files with a .dat extension).

* Look at `CreateDesignExample` - it shows how to create a new design from scratch and then print out information about it. 

* The `ImportExportExample` program reads an .rscp and outputs a .tcp.  See below for a discussion of what these checkpoints are.  And, remember that up above you learned how to generate a .rscp of a design using the `compile.tcl` program.  Now, run `ImportExportExample` on one of the designs you compiled in Vivado this way.  Find and example the .tcp it generated.  See below for a discussion of the differences of .rscp and .tcp checkpoints.

* In `ImportExportExample` note the routine called `importExportDesign()`.  It imports the design, manipulates the design, and exports it back out.   Can you insert some code between these two steps in the program to change the design in some way?  Maybe modify the contents of a LUT?  Maybe unplace some or all of the cells (set the BEL they are mapped to as null).  Then, when you import the resulting design back into Vivado can you see the difference in the design in the Vivado GUI or with Tcl?

The point of this exercise is to learn what you can and cannot do with RapidSmith2 so be creative and just dig in and play around.  This is a very open-ended activity.

Some things to do while you do this:

1. Read whatever documentation they provide
   * There is a docs directory in RapidSmith2 with a PDF RapidSmith2 document in it.
   * There are instructions above on how to generate all the javadocs documentation on the API calls and how to learn about the RapidSmith2 API using it.
1. Wander around and read through the source code
1. Experiment (just play around with it).  In this case, maybe you come up with a simple thing you want to do with it and then you read up and figure out what to do.

And that is what this exercise is all about.  

## A Note About RapidSmith vs. Tincr Checkpoints
Due to how Vivado is structured, it was necessary to use different checkpoint formats for exporting data from Vivado vs. importing data back into Vivado.

When you run the `compile.tcl` program from `exampleVivadoDesigns` above, it creates a .rscp file.  That is a "RapidSmith Checkpoint" - meaning it contains all the data regarding your design that is needed by RapidSmith2 to be able to do something with the design.

When RapidSmith2 is ready to send the design back to Vivado, it creates what we call a "Tincr Checkpoint".  It contains the information needed for Vivado to be able to import the design back in.  RapidSmith2 can read .rscp checkpoints _only_ and can write _.tcp_ checkpoints only. 

At this point it would be good to look through the .rscp generated above when you compiled the add program.  Figure out what the pieces are and what they represent.  Now, run the ImportExportExample program on that and look through the .tcp generated.  Figure out what the pieces are and what they represent.  The definitive paper on these formats and how information in RapidSmith2 is exhanged with Vivado are the "Vivado Design Interface" paper below and the thesis by Thomas Townsend.

# Explanation and Papers
Once RapidSmith had been in use for some time, Xilinx discontinued the ISE tool set and so the XDL language went away.  Since RapidSmith was based on XDL, there was a need for a replacement tool.  

RapidSmith2 was the follow-on.  It took a number of grad students a number of years to pull it together (it was a MUCH large undertaking than RapidSmith was).  Here are some papers on the constituent pieces of what now akes up RapidSmith2 (be sure to use the CAEDM VPN before you try to access these links so you can get to the PDF's of the papers):

* [Tincr — A custom CAD tool framework for Vivado](https://doi.org/10.1109/ReConFig.2014.7032560)
* [Vivado design interface: An export/import capability for Vivado FPGA designs](https://doi.org/10.23919/FPL.2017.8056809)
* [Thomas Townsend's MS Thesis on the Vivado Design Interface](https://scholarsarchive.byu.edu/etd/6492/)
* [RapidSmith 2: A Framework for BEL-level CAD Exploration on Xilinx FPGAs](https://doi.org/10.1145/2684746.2689085)
* [Maverick: A Stand-Alone CAD Flow for Partially Reconfigurable FPGA Modules](https://doi.org/10.1109/FCCM.2019.00012)

Finally, here is an invited talk survey article from not too long ago that gives an overview of our efforts with RapidSmith and RS2 and Maverick as well as what other groups have done:
* [Third Party CAD Tools for FPGA Design - A Survey of the Current Landscape](https://doi.org/10.1007/978-3-030-17227-5_25)



----------------------------------
Initially created by Brent Nelson, April 2020.