---
layout: page
toc: true
title: LCM
slug: lcm
type: robotics
order: 0
---


# Lightweight Communications and Marshalling (LCM)

## Overview - What is LCM?

As stated on the main page of the [LCM documentation](https://lcm-proj.github.io/), Lightweight Communications and Marshalling, or LCM, "is a set of libraries and tools for message passing and data marshalling, targeted at real-time systems where high-bandwidth and low latency are critical. It provides a publish/subscribe message passing model and automatic marshalling/unmarshalling code generation with bindings for applications in a variety of programming languages."

In other words, LCM is a tool that allows us to send and receive messages between the components of our robotic systems.

Alternate tools that serve this same, or a similar, purpose exist, such as the [Robot Operating System (ROS)](https://www.ros.org/), or [ZeroMQ](https://zeromq.org/). Each approach has it's own advantages and drawbacks. We have chosen to use LCM because it is lightweight, or has very little overhead, and is relatively simple to implement and use.

## Lecture

For the recording of our discussion about LCM, see the video below:

<iframe width="800" height="600" allow="fullscreen"
src="https://www.youtube.com/embed/xTEgV79aVLY">
</iframe>

## Download

The FRoSt Lab has forked and modified the source code of LCM, allowing us to correct a few old methods used in their installation. 
In particular this has allowed us to more reliably install LCM with python. Please clone the master branch of the repository found at <https://bitbucket.org/frostlab/lcm/src/master/>. If you are uncertain where to put the repo, generally I just clone it into my home directory.

Alternate methods for downloading LCM exist, but those will not be covered in this guide.

## Building and Installing LCM

The full build instructions for LCM can be found at <https://lcm-proj.github.io/build_instructions.html>. 

Given that the aforementioned guide assumes the use of Linux/Ubuntu, simplified instructions for that platform are provided here, first with the prerequisites and then the actual instructions.

### Prerequisites 

There are three required packages that must be installed, if they are not already, before building LCM.

They are:
* build-essential
* libglib2.0-dev
* cmake (version 3.1 or higher)
* default-jdk (not required, but permits use of useful tools later on)

To install all of the above:
- Run ```sudo apt update ``` to update your package list
- Run ```sudo apt install build-essential libglib2.0-dev cmake default-jdk``` to install all of the dependencies
    - If you already have some of the dependencies installed, running the above command will just skip installing the ones you already have on your system

Some optional prerequisites for LCM can be found on the build instructions webpage, but they are not necessary for basic LCM operations and compatibility with the C and C++ programming languages. Should you encounter any problems using LCM with another language, please refer to the [full build instructions](https://lcm-proj.github.io/build_instructions.html) to find those optional prerequisites.

#### Notes on CMake

There are multiple ways to install CMake, with each method providing slightly different versions. For our purposes installing through apt, as is done above, should be sufficient. However, installing it through apt usually does not get you access to the newest version of CMake, so if for some reason you need a newer version, the full list of installation methods are:
* Through apt, the system package manager (```sudo apt install cmake```)
* Through pip, the python package manager (```pip install cmake ```)
* Through cloning the source code for CMake (Visit <https://gitlab.kitware.com/cmake/cmake> and follow the instructions in their README file)

As previously mentioned, apt should be new enough, but pip grants a newer version than apt, and cloning the source code will provide you with the newest possible version of CMake. For more information on CMake, see the [CMake page](https://byu-cpe.github.io/ComputingBootCamp/tutorials/cmake/) on the BYU Computing BootCamp website.

### Building LCM

On Ubuntu, the steps to build LCM are as follows:
* Navigate to the lcm directory within a terminal
* Run ```mkdir build``` 
* Run ```cd build``` 
* Run ```cmake ..``` 
* Run ```make``` 
* Run ```sudo make install``` 

The FRoSt Lab fork of LCM has also added a command to build the python portion of LCM:
- Run ```make python-install```
    - Did you get an error after running the above?
        - Note that this will not work if your system only has python 2. If you get an error that mentions ```No module named 'setuptools'```, then use [conda](https://byu-cpe.github.io/ComputingBootCamp/tutorials/conda/) and [python3](https://byu-cpe.github.io/ComputingBootCamp/tutorials/pythonIntro/). If conda is not already activated by default then run  ```conda config --set auto_activate_base true```, restart your terminal, remove the build folder from LCM and all of it's contents, and start over with the build steps. This time when you get to the python-install step it should run successfully.
        - Alternatively, if you receive an error message mentioning not having permissions to edit specific file locations, run the command with sudo privileges.

Note that for each python environment that you would like to have LCM installed on, you will need to repeat all of the above steps. If you have already installed it once, then in your base lcm folder remove the build folder with ```rm -rf build``` to recursively delete everything inside and including the build folder. Then you can start on the first step of building LCM above and run through all of the steps again, ensuring that your python environment of choice is active.

Now you should have LCM built and installed on your system!

### LCM Python Package

If you will be using LCM with python, while you can still follow the instructions above and install it for python after installing it to your system, alternatively you can install it for your python environment with: 

```pip install lcm``` 

The site for the pip version can be found at <https://pypi.org/project/lcm/>.

## Using LCM

At this point you should have LCM installed on your system. 
To now learn about how to use LCM, feel free to refer to their tutorials, which are found at <https://lcm-proj.github.io/tutorial_general.html>.

Some of the same material will be covered in the sections that follow in this tutorial, but we hope to make things slightly clearer and easier to follow.
Additional material will also be provided here that is not easily found in their tutorials.
Lastly, it is worth noting that all of the material here is focused on using LCM with C++.
The steps for different languages are very similar, but the syntax may vary, so please refer to the LCM documentation and their tutorials for usage with other languages.

### Defining Messages

Message definitions are language independent for LCM, but are crucial for being able to subsequently publish and receive those messages using other programming languages.

The first step to define new messages and types is to create a file with the .lcm file extension.
Inside of our new file we must then define a package name, so the first line of the file should be ```package [your package name here];```, noting that the semicolon is necessary at the end of the line.

Following the package definition is where you can then define any messages that you choose.
All messages should be of the format:
```
struct [message name]
{
    [type1] [variable1];
    [type2] [variable2];
    ...
    [typeN] [variableN];
}
```

Where the message names and variable names can be of your specification, while the types must be one of a preset list of accepted types by LCM. 
Those type specifications can be found at <https://lcm-proj.github.io/type_specification.html>.

For my example I am going to be setting up two messages, one that contains information about an item (the name, cost, and whether or not that item is in stock), and another message that is used to provide a report of a list of items, including information like the time stamp, number of items in the status report, and then the list of all of those items.

To do this I created the following file:
```
// Comments are identical to the c++ format, so any line preceded by // is a comment
// The filename that I chose for this file is example_def.lcm

package example_pkg;

struct item
{
    string name;
    int16_t cost;
    boolean stocked;
}

struct status
{
    int64_t timestamp;
    int16_t item_count;
    item items[item_count];
}
```

So in this file I have created a package with the name of example_pkg, in which I have defined two message types: item and status. 
The first message contains all of the fields that I will need to store the data for one item, while the second one contains an array of item types as a means of storing a status report.

At this point, I now need to generate the code that will allow my c++ program (which we have not yet written) to use these message definitions.

LCM provides many different terminal commands, most of which will be covered later, but we do need one of them in order to generate the code to allow my messages to be used in a c++ program. 
In a terminal that is in the directory of your .lcm file, run: 

```lcm-gen -x [filename].lcm```

This will generate code from your .lcm file in c++ that defines your messages and allows them to be included and used in your program.
The -x parameter is what specifies that the code should be generated for c++. 
An important note is that if you have some of your messages using other messages defined in the same package (as is the case in the example file provided above), you will need to use a slightly modified command:

```lcm-gen -x --cpp-include .. [filename].lcm```

This will allow for your messages to include one another properly. A number of other parameters can be used for other languages, all of which can be found at <https://lcm-proj.github.io/tut_lcmgen.html>.

The lcm-gen command should now have created a folder that uses the package name specified in your .lcm file, and inside of that folder you should see one or more .hpp files (one .hpp file will be generated for each message you defined).
So after running lcm-gen I now have a folder called 'example_pkg' with two files inside, namely, 'item.hpp' and 'status.hpp'.

We now have defined our messages and are ready to move on to the next step, incorporating those messages in a program that will publish data using them.

### Sending Messages

In order to send a message, we first need to fill it with some kind of useful information. This is now where the programming language of your choice comes in. For each language the process is ever so slightly different, but the principles remain the same. We need to: 
* Include the message definitions
* Create an object of that type in our code
* Fill it with the desired information
* Publish it over the network using built in functions from LCM.

Following is the file that I created for publishing simple messages that use the item and status types that I defined in the previous section.
````
#include <lcm/lcm-cpp.hpp>
#include "example_pkg/item.hpp"
#include "example_pkg/status.hpp"
#include <iostream>
#include <chrono>

// Creates an item object and fills it with the provided data.
// Returns the item object
example_pkg::item newItem(std::string name, int16_t cost, bool stocked)
{
    example_pkg::item item;
    item.name = name;
    item.cost = cost;
    item.stocked = stocked;
    return item;
}

// Simple program to publish hardcoded message data using LCM
// If the program is called without any command-line arguments it will publish a single item message
// If anything is present as a command-line argument, a status message with five items will be published instead
int main(int argc, char** argv)
{
    // Create LCM object and check that it was created successfully
    lcm::LCM lcm;
    if (!lcm.good())
    {
        std::cout << "LCM initialization failed" << std::endl;
        return 1;
    }
    // If no command line arguments are provided, run the program with a single item message,
    if (argc <= 1)
    {
        example_pkg::item msg;
        msg = newItem("Milk", 5, true);
        // Specifies the channel name for the message and publishes it
        lcm.publish("INDIVIDUAL", &msg);
    }
    // However, if any arguments are provided then run it with a hardcoded status message.
    else
    {
        std::string names[5] = {"Milk", "Cheese", "Ground Beef", "Salt", "Pepper"};
        int16_t costs[5] = {5, 30, 6, 1, 2};
        bool is_stocked[5] = {true, true, false, true, false};
        example_pkg::status msg;
        msg.timestamp = std::chrono::system_clock::now().time_since_epoch().count();
        msg.item_count = 5;
        for (int i = 0; i < 5; i++)
        {
            msg.items.push_back(newItem(names[i], costs[i], is_stocked[i]));
        }
        // Specifies the channel name for the message and publishes it
        lcm.publish("REPORT", &msg);
    }
    return 0;
}
```

In the file I have:
- Included the main LCM package
- Included any defined LCM message types that will be used
- Included any other standard libraries that I'm using
- Created a helper function to easily fill in the data fields of an item message type
- Created a main function that:
- Initializes LCM
** Checks whether or not command line arguments were provided
** Initializes and stores information in either a single item message, or in a status message that contains five item messages
** Calls the publish function to transmit the desired message over the network, using a specified channel
** Terminates after publishing the message

Overall the process is really quite simple, but given the complete control that we have over the message definitions, it's also quite powerful.
As we'll soon cover, I can now have other scripts listening for the messages that are getting published, and then processing that data in any way that is desired. 

One side note when dealing with arrays in LCM with c++, those arrays are vector types.
When filling the array, make sure that you fill it completely, otherwise when calling the publish function your program will result in a segmentation fault.
On the other hand, if you overfill the array (eg. if the message specifies an array of five elements, but you put six elements into that vector) then it will publish only the first elements up to the expected size of the array and ignore any extra elements of that vector.

Ultimately, you can have any number of scripts running simultaneously and publishing on either the same, or different, channels.

### Receiving Messages

Receiving messages isn't quite as straightforward as sending them. 
Once again, you'll need a file that includes the base LCM library, as well as any messages that will be used in the script.

The file that I created for my example is below
```
#include <lcm/lcm-cpp.hpp>
#include "example_pkg/item.hpp"
#include "example_pkg/status.hpp"
#include <iostream>

// Class for handling LCM messages
class Handler 
{
    public:
        ~Handler() {}
        // Function for handling of Item message types
        // It simply prints out the message
        void handleItemMessage(const lcm::ReceiveBuffer* rbuf,
                const std::string& chan, 
                const example_pkg::item* msg)
        {
            printf("Received message on channel %s:\n", chan.c_str());
            printItem(msg);
        }
        // Function for handling of Status message types
        // The full status message will be printed, including each item
        void handleStatusMessage(const lcm::ReceiveBuffer* rbuf,
                const std::string& chan, 
                const example_pkg::status* msg)
        {
            std::cout << "Received message on channel " << chan << ":" << std::endl;
            std::cout << "-------------------------------------------------------------" << std::endl;
            std::cout << "Begin Status" << std::endl;
            std::cout << "-------------------------------------------------------------" << std::endl;
            std::cout << "Timestampe: " << msg->timestamp << std::endl;
            std::cout << "Number of items: " << msg->item_count << std::endl;
            for (int i = 0; i < msg->item_count; i++)
            {
                printItem(&msg->items[i]);
            }
            std::cout << "-------------------------------------------------------------" << std::endl;
            std::cout << "End Status" << std::endl;
            std::cout << "-------------------------------------------------------------" << std::endl;
        }
        // Helper function for printing Item message types
        void printItem(const example_pkg::item* msg)
        {
            std::cout << "=== Item ===" << std::endl;
            std::cout << "\t Name: " << msg->name << std::endl;
            std::cout << "\t Cost: " << msg->cost << std::endl;
            std::cout << "\t Stocked: " << bool(msg->stocked) << std::endl;
        }

};

// Runs an infinite loop that waits for any messages to be received on the two channels 
// "INDIVIDUAL" and "REPORT", with appropriate handling performed whenever a message is
// received on either of those two channels
int main(int argc, char** argv)
{
    // Initialize LCM and verify that it was successful
    lcm::LCM lcm;
    if(!lcm.good())
        return 1;
    // Initialize handler object and subscribe to the desired channels
    Handler handlerObject;
    lcm.subscribe("INDIVIDUAL", &Handler::handleItemMessage, &handlerObject);
    lcm.subscribe("REPORT", &Handler::handleStatusMessage, &handlerObject);
    // Handle any incoming messages on the subscribed channels, and run in an
    // infinite loop
    while(0 == lcm.handle());
    return 0;
}
```

In the above you'll see that the main function is pretty simple. 
We initialize an LCM object, subscribe to the appropriate channels (knowing the channel name is necessary to receive the messages properly), and then have an infinite loop that will handle the processing of any received messages per the definitions found in the Handler class.

The handler class is where things get a bit more structured and slightly more difficult to follow. 
In order to subscribe to a channel a handler class must also exist that defines the function(s) that should be called whenever a message is received. 
The simplest format for a handler class would be
```
class Handler
{
    public:
        ~Handler() {}
        void handleMsg(const lcm::ReceiveBuffer* rbuf, const std::string& chan, const [pkg]::[msg]* msg)
        {
            // Insert whatever code you would then like to use to process the message here
        }
}
```

In the code above, the parameters of the handler function must be kept as is, with the exception of inserting your package and message name in the [pkg] and [msg] fields. 

You are welcome to include as many handler functions as you would like, with each one handling a different type of message, or even messages from a different package. 
The one thing to bear in mind is that if you perform a lot of processing in those handler functions and you are receiving that message at a very high rate, you may end up skipping messages that are being published.
With that consideration, it's generally a good idea to keep the handler function fairly simple, maybe even just copying the message over into a queue and then processing of that queue can be performed by another function, allowing your handler to return to wait for new messages.

Another important note, the LCM::handle() function is a blocking function, it will wait until a message is received and the program will not execute any following lines of code until that function has returned, which it will only do once a message and been received and processed. 
In other words, if you call the handle() function and aren't sending any messages on the channel that you've subscribed to, your program could hang indefinitely, doing nothing.
An alternative to the handle() function is the handleTimeout() function, which has one parameter, the number of milliseconds that can pass before the function will timeout, which can be used to prevent the function from indefinitely blocking your code. 
Another alternative is to introduce threading into your script and have one thread dedicated to listening for LCM messages, and the other thread executing the rest of your code, though this does introduce some additional complexity for the programmer.

For the documentation on the LCM class functions, like handle() and handleTimeout(), please visit <https://lcm-proj.github.io/classlcm_1_1LCM.html#aac221c0fa80ede30a2383fba612f972e>.

Lastly, just as in the publishing section, you can have as many scripts running as you would like that interact with the same channels.

In a more solid example of the above statement, our AUV will be recording information from a set of stereo cameras. 
That camera data could then be published onto the channel "STEREO_CAM".
Then for localization of the vehicle the Xavier could subscribe to the "STEREO_CAM" channel and process the information gathered from those cameras to see how the vehicle has moved.
Another script might be running that is also subscribed to the "STEREO_CAM" channel, but all it does is display the images so that a human operator can see what the vehicle is seeing.
Both of those processes are able to access the "STEREO_CAM" channel data and process it independently, and therefore simultaneously, allowing for very versatile systems.
Just to complicate matters more, we will have two sets of stereo cameras, one on the front and the other on the back of the vehicle.
Both sets of cameras could be publishing their data on the "STEREO_CAM" channel and everything that is subscribed to that channel would receive images from the front and back of the vehicle.
Ultimately it wouldn't be a good idea to have both of those camera sets using the same channel, but it serves to describe what you can do with LCM.

### CMake and LCM

For the example code that I have provided in the previous sections, I used the following CMake file to generate the executables for both the publishing and receiving scripts:
```
# Always must specify the minimum version of CMake that is required, in this case I used version 3.16, so I specified 3.16
cmake_minimum_required(VERSION 3.16)

project(pub) # moved to be above package loader and linking libraries

# Find and include LCM
find_package(lcm REQUIRED)
include( ${LCM_USE_FILE} )

# Create project and executable for publishing script
# project(pub) # moved to above
add_executable(pub example_pub.cpp)
target_link_libraries(pub lcm)

# Create project and executable for receiving script
# project(rec) # 2 projects needn't be included in the same CMakelist
add_executable(rec example_rec.cpp)
target_link_libraries(rec lcm)
```

The CMakeLists.txt file show above was in my base directory with my .lcm file, from there I:
* Created a build folder and moved into it with ```mkdir build && cd build```
* Ran CMake to generate the makefile with ```cmake ..``` (The .. is because for the cmake command I want it to use the CMakeLists.txt found in the directory below my build folder)
* Generated my executables with ```make```

If you are using the FRoSt Lab's lcm_messages repository and want to include it in another project that uses the pods structure, you can do so by including in the base CMakeLists.txt file:
```
# LCM Messages
FetchContent_Declare(
  lcm_messages
  GIT_REPOSITORY git@bitbucket.org:frostlab/lcm_messages.git
  GIT_TAG origin/master
  UPDATE_DISCONNECTED true
  )
FetchContent_MakeAvailable(lcm_messages)
```

If you need to use a branch other than master, you can swap out the GIT_TAG field from "origin/master" to be "origin/[branch name]".

### Tools and Terminal Commands

#### Base Terminal Commands

LCM provides a number of useful and/or necessary commands available from the terminal.

The commands that we will be using the most are:
* lcm-gen
* lcm-logger
* lcm-logplayer
* lcm-logplayer-gui
* lcm-spy

The first three are all terminal based commands, and the last two provide user interfaces.
However, in order to use the last two you must have installed default-jdk in part of the prerequisites, as those user interfaces rely on Java and will only be available to you if LCM was able to find Java during the installation process. 
If you did not have default-jdk installed and aren't able to use lcm-logplayer-gui and lcm-spy, please return to the 'Building and Installing LCM' section of this page.

##### lcm-gen

This command will generate source code for the message types that you have defined in a .lcm file type. 
See <https://lcm-proj.github.io/tut_lcmgen.html> for a description on how to use it and the flags required for each output language. 
The code generated from this command will be output into a folder with the name of the package specified in the .lcm file, with individual files for each message definition inside of that folder.

##### lcm-logger

This command allows for LCM messages to be logged to a logfile.
When run without any additional flags or options set it will log any LCM messages on any channel in the network, and output them to an automatically generated logfile, the name of which will be output in the terminal.

Additional flags or options can be provided to set the logfile to record messages on specific channels, and to output to a user-defined logfile destination and name, rather than an automatically generated one.

To view the options and learn more about them, run ```lcm-logger -h``` in a terminal.

##### lcm-logplayer

This command allows you to play back a log. 
Logs record the message and contents, channel the message was sent on, as well as the time that the message was sent at.
In playing back a log you are able to then receive those messages as if it was happening in real-time.

If you are on a system that supports graphical output, it is recommended that instead of lcm-logplayer you use lcm-logplayer-gui, but the headless command is still very useful for system that do not provide graphical output.

This feature is incredible useful and will be one that we use a lot. 
For example, we have the wheelchair that is equipped with LiDAR and cameras. 
A user could manually drive the wheelchair through an environment with all of the sensors running, and logging all of the data sent and received through LCM.
Then as the autonomous control systems of the wheelchair are being developed, we could play back those data logs and see how the control system handles the input data in real time to verify that it works as expected. 
Using the logged data and playback features we can then develop systems and test them before applying them onto the vehicle, minimizing the risk of unexpected behavior, especially behaviors that could lead to damage to the hardware.

##### lcm-logplayer-gui

This provides access to a GUI that allows for greater control of the playback of a logfile, when compared to the lcm-logplayer command. 
Specific channels can be isolated, playback speed can be easily controlled, and the progress of the logfile can be viewed.

As previously mentioned, this command requires the use of java and a graphical output, so if one or both of those are unavailable for some reason, you can use the lcm-logplayer command instead.

##### lcm-spy

This command provides a GUI that can be used to visualize all desired messages and channels in real time.
Some of the useful information provided is the channel, message type, number of messages received, frequency at which messages are received, and then additional information like the current values of message fields.
Additionally, the messages can be clicked on to view more detailed information, and the individual fields can also be clicked on to view a plot of those values over time. 

The interactive features (clicking on messages and fields) can only be used once proper setup for your message types has been performed. When run without any setup, lcm-spy will listen to any message and channel, similar to lcm-logger, but with greater feedback to the user than lcm-logger, but without any of the interactive features.

In order to setup your message types to use the interactive features, you will need to:

# Generate the java form of your messages
# Have a terminal open in the directory that contains your .lcm file you used to generate the messages
# Run ```javac -cp /usr/local/shar/java/lcm.jar [your package name]/*.java``` to create .class files for each of your java messages
# Run ```jar cf [your package name].jar [your package name]/*.class``` to create a .jar file from your .class files
# Then run ```export CLASSPATH=[your package name].jar && lcm-spy``` to run lcm-spy using your .jar file to allow it to process messages that are any of your message types

==== Additional Terminal Commands ====

Additional terminal commands are available, but you will likely never need to use them. 
However, if you are curious, or for some reason do need them, they are:
* lcm-example
* lcm-logfilter
* lcm-sink
* lcm-source
* lcm-tester

=== Communicating between computer systems ===

By default, the UDP Broadcasts that LCM uses to publish messages will be configured to only be viewable on a local machine.
In other words, if you have two computers, one of them running a script that publishes a message, the other running a script that receives a message, and the two systems are connected via a wired local area network, the two systems will not receive any LCM broadcasts, so the receiving system will not do anything whenever the publishing system broadcasts a message.

In order to resolve this, we can modify the configurations of the UDP broadcasts, allowing them to to be sent "over the wire".
More information on this can be found at https://lcm-proj.github.io/multicast_setup.html, but here we'll cover the basics.

==== TTL Configuration ====

The ttl is time-to-live, and controls how far in the network the signal can go.

If you want to allow LCM to communicate across a local network, run 
```
export LCM_DEFAULT_URL=udpm://239.255.76.67:7667?ttl=1
```
on all systems that are connected to each other and will be using that network to publish and receive LCM messages.
The ttl variable is what we are updating, the default for this is 0, which restricts communication to a single device. 
A value of 1 then allows for communication over a local network, and a value of 2 should allow communication through a router (this has not yet been tested by me, but the value of 1 has been tested and confirmed to work as advertised).

The above will only configure LCM for that particular terminal session. 
To enable it by default, add the above command to the .bashrc file, located in your home directory.
This will ensure that LCM is configured to broadcast on the local network from startup of the device and in any terminal that is opened.

Alternatively, some of the above can be done in the LCM scripts, rather than from the Ubuntu system environment.
At this time I have not yet experimented with how to do that, but doing so requires the use of 
```lcm::LCM lcm = lcm_create(); ``` 
(with the appropriate parameters passed in for your use case) instead of just 
```lcm::LCM lcm; ```
in your code. 
The documentation for the lcm_create() function can be found at https://lcm-proj.github.io/group__LcmC__lcm__t.html#gaf29963ef43edadf45296d5ad82c18d4b.

==== Network Routing ====

If you still are unable to communicate between devices, you may need to configure routes between them.
This can be done by running the command
```
sudo route add -net 224.0.0.0 netmask 240.0.0.0 dev [interface]
```
where [interface] is the appropriate connection for the local network for that device.

===== Identifying The Network =====

In order to identify the connection, the easiest way is to disable all wi-fi connections for all devices that are connected together, and ensure that they are not connected to any wired internet connections as well.
Then run 
```
arp -a
```
and you should get an output that is something along the lines of
```
DEVICE-NAME (IP-ADDRESS) at HARDWARE-ADDRESS [CONNECTION-TYPE] on INTERFACE
```
In the above, everything in all caps is a field wherein you'll find some form of text or numeric data.
The field that you care about is INTERFACE. 
Whatever is output there is what you should put into the [interface] field of the earlier command for adding a route.
You will need to do this for all systems connected to the local network, after which you should then be able to send and receive LCM messages across devices!

=== Using LCM on a local machine with no network connections ===

If you will be using LCM on a machine that has no network connections, be them wired or wireless, then you need to enable multicast on your computer, or else you will not be able to use any scripts that contain LCM functionality in them.

The commands for a Linux system are:
``` sudo ifconfig lo multicast ```
and
``` sudo route add -net 224.0.0.0 netmask 240.0.0.0 dev lo ```

After which you should be able to run any LCM scripts as you normally would, noting that only scripts running on that computer will be communicating with one another.

=== Adding LCM messages to the FRoSt Lab Repo ===

In our lab we have a single repository for storing all of our LCM message definitions. 
Then, using CMake and the Pods2 structure, those LCM messages can be easily included and generated within any other repository that needs to use them. 

The repository for all of our LCM message definitions can be found at https://bitbucket.org/frostlab/lcm_messages/src/master/

If you will need to add any new message types to the repository, please follow these steps:
# Clone the master branch of the repository
# Create and switch to a new branch
#* ```git checkout -b [name of your new branch] ```
# Push and set the upstream for your new branch
#* ```git push --set-upstream origin [name of your new branch] ```
# Add a new .lcm file in the lcmtypes folder with a descriptive name (generally the name of the file should be closely tied to the other repository that the message will be used in)
# Define any messages that you need to in the new .lcm file, ensuring that the package definition is ```package lcm_messages;``` in any of the new .lcm files you add
# Verify that your new LCM messages are properly generated
## Open a terminal to the base directory of the lcm_messages repo
## Run ```make ```
## Correct any errors, if they exist and repeat until you have verified that your messages are correctly defined
# Add, commit, and push your changes (while still within your new branch)
# Test that the other repo that uses the messages is able to do so
#* Instructions on including the lcm_messages repo in other repos are found in the README of the lcm_messages repo, just change the GIT_TAG field from origin/master to origin/[your branch name]
# If all works as intended and you have finished testing your new message(s), merge your branch into the master one
## Run ```git checkout master ``` to switch back to the master branch
## Run ```git merge [your branch name] ``` to merge your branch into the master branch (This will bring all of the changes that you made in your branch into the master branch)
# Delete your branch
#* To delete the branch from your computer run ```git branch -d [your branch name] ```
#* To delete the branch from bitbucket run ```git branch -d [remote name] [your branch name] ``` (usually the remote name is origin, though this may be different in certain cases)
# Update the GIT_TAG field in the CMakeLists.txt file of the repo that is using your new message to be origin/master so that it pulls from the master branch instead of your, now deleted, branch, and also then rebuild that project to reflect those changes

And that's it!

One great benefit of our lcm_messages repository is that lcm-spy is setup to be configured for all of the messages therein by simply calling "make spy" from a terminal that is in the base directory of the lcm_message repository. 
Then you can call lcm-spy and take advantage of all of the great tools available from there.

=== Advanced Topics ===
==== LCM uses Multicast ====

By default, LCM uses multicast to broadcast messages over a UDP server. 

Initially, messages will only be broadcast locally but they can be configured to be broadcast on an entire subnet, or even through a router. 
In order to learn more about what configurations are available and how to use them, please visit https://lcm-proj.github.io/multicast_setup.html

==== LCM Tunneling ====

Tunneling is a feature wherein select messages can be transmitted directly from one network port to another, instead of relying on the typical multicast method.
In other words, one device, or component of the system, can send messages directly to another component of the system without broadcasting those messages to the entire system.

Tunneling is implemented in libbot2, the general code for which can be found at https://github.com/libbot2/libbot2, and the tunneling-specific code can be found at https://github.com/libbot2/libbot2/tree/master/bot2-lcm-utils/src/tunnel.

As we have yet to use tunneling, the coverage in this guide is limited, but when we begin to use it in the future this guide will be updated with better descriptions of how and when we use it.

== Try It Out For Yourself ==

In this exercise you should use both python and c++.
If you need additional resources beyond what is included in the above tutorial, the link to the tutorial found on LCM's site for C++ is https://lcm-proj.github.io/tut_cpp.html and for Python is https://lcm-proj.github.io/tut_python.html.
If you just want to explore more of the documentation on LCM's site, their homepage is https://lcm-proj.github.io/index.html.
Their documentation can be a bit lacking, or difficult to navigate, depending on what you are looking for help with, but it does provide information beyond what is covered in the tutorial on this page. 
So if what you are looking for isn't found here, you may find it there.

Now to try things out for yourself
# Fork the [https://bitbucket.org/frostlab/lcm_messages/src/master/ lcm_messages repo from our lab]
#* This is different from cloning. Instructions on how to fork from a BitBucket repository can be found at https://support.atlassian.com/bitbucket-cloud/docs/fork-a-repository/
# Create a new branch in your forked repo and switch to operating within that branch
# Add a new message type, remembering that the package name should be lcm_messages, then generate the files for both python and c++
#* While you can make the message definition(s) as simple or complicated as you would like, I would highly recommend including arrays, especially at least one multi-dimensional array
# Create a script to publish your message, one in c++ and another in python
# Create a script to receive and process your message, one in c++ and another in python
# Verify on your local system that you are able to publish and receive, both from c++ and python, and from c++ to python, and so on
# Prepare lcm-spy and then use it to visualize the messages as you publish them real-time (I would recommend not having a single static value being published each time, as if the values are changing the output on lcm-spy will be much more interesting)

Part 2
# Connect your computer to another computer via an Ethernet cable
# Setup the computers to communicate with one another
# Publish the messages using one computer and verify that they can be received on the other computer

Once you are done feel free to experiment more with your forked version of the lcm_messages repository, or simply delete it from your computer. 
We ask that you fork the repository so that no changes are made to the actual repository during the time that you spend learning more about how to use LCM.
In the future, if you ever need to add a message to the repo for a lab-related project, you will instead follow the steps provided in the respective section of the above tutorial.

= LCM On Windows =
So you want to be brave and work with LCM on Windows? (Unfortunately it's nowhere as easy as on Linux)

Please refer to: [[File:Building.LCM.pdf]] if you would like to see where the inspiration for this guide came from.

The following instructions are a modified version of the ones found in the link above.
These steps are more up-to-date and tested more recently than those found on the pdf linked above.

'''Verified Windows Versions'''
These installation instructions have been tested and verified on:
* Windows 7 (Please see [[RoboticsTrack:LCM#Notes For Windows 7 (IVER Backseat) | Notes For Windows 7]] )
* Windows 10
* Windows 11

## Setup and Installation

* '''Install Java JDK 8'''
** Download and Install Java JDK 8 using jdk-8u311-windows-x64.exe found in the folder at [https://byu.box.com/s/ckc9ehi0we9ifz4vj2hum7dcz4lijyf2 https://byu.box.com/s/ckc9ehi0we9ifz4vj2hum7dcz4lijyf2]
** Add a new environment variable called 'JAVA_HOME' with a value of ```C:\Program Files\Java\jdk1.8.0_311```
** Also add ```
C:\Program Files\Java\jdk1.8.0_311\jre\bin
C:\Program Files\Java\jdk1.8.0_311\jre\bin\server
C:\Program Files\Java\jdk1.8.0_311\bin``` to the PATH environment variable
*** '''''Sidenote:''''' If you encounter any errors with java when trying to build LCM later on with CMake, try uninstalling and reinstalling Java.
* '''Install Python'''
** Miniconda is recommended, and can be found at [https://docs.conda.io/en/latest/miniconda.html https://docs.conda.io/en/latest/miniconda.html]
** Add the location of your python executable to PATH, which should be ```%USERPROFILE%\miniconda3```
** Open miniconda (search for it in the windows search bar and run the anaconda prompt)
*** Run ```pip install --upgrade pip```
*** Run ```pip install pyjnius```
* '''Install GLIB'''
** Download and install MSYS2 from [https://www.msys2.org/ https://www.msys2.org/]
** Run MSYS2 and within the console that opens up run ```pacman -S mingw-w64-x86_64-gtk3``` and in the prompt press 'y' to install gtk3 which will include GLIB 2.0
** Add ```
C:\msys64\mingw64\lib
C:\msys64\mingw64\bin``` to the path variable
* '''Install CMake'''
** Download and run the windows installer from [https://cmake.org/download/ https://cmake.org/download/]
** While it is not necessary to add CMake to the path, you can check to have it added to path for the current user if you would like access to CMake from the command prompt (We will be using the GUI later, hence no need for it to be added to the PATH variable)
* '''Install Visual Studio C++'''
** Install the community edition (it's the free one) from [https://visualstudio.microsoft.com/vs/features/cplusplus/ https://visualstudio.microsoft.com/vs/features/cplusplus/]
*** '''''Sidenote:''''' If you encounter a problem where CMake cannot find a C/C++ compiler, your installation is incomplete. Open up the Visual Studio Installer, click on 'Modify Installation' and then navigate to the C++ tools, which should already be selected. Deselect and then reselect them, and then install the additional files that will then be included (for some reason, the installation may occasionally be incomplete, leaving out some critical parts of the packages necessary for everything to run properly)
* '''Download LCM'''
** Download (you could clone it if you'd like, but downloading might be easier) the master branch of LCM from [https://github.com/lcm-proj/lcm https://github.com/lcm-proj/lcm] (At the time of writing we have tested it using commit 91ce7a2ae46ad05f8a232f5fe32a06cccbead1c2)
** Extract the contents of the zip folder, if you downloaded it instead of cloning it
* '''Configure LCM using the CMake GUI'''
** Run the CMake GUI
** Set 'Where is the source code' to where you extracted the LCM folder (for example: C:/Users/[yourusername]/Downloads/lcm-master)
** Set 'Where to build the binaries' to the same path as above, with the addition of '/build' so that it will create a new folder named build, where the binaries will be placed
** Click 'Configure' and select 'yes' when prompted to create the build folder, as it shouldn't yet exist, ensure that the generator matches the Visual Studio version that you installed previously (eg. Visual Studio 17 2022), leave the selection of 'Use default native compilers', then click 'Finish' 
** After the configuration has completed, check the 'Advanced' box and find LCM_ENABLE_TESTS and deselect it
** Ensure that LCM_ENABLE_PYTHON is selected, and that python was found and the PYTHON variables have been all set to reference the miniconda installation, for example: 
```
PYTHON_EXECUTABLE          C:/Users/kalin/miniconda3/python.exe
PYTHON_INCLUDE_DIR         C:/Users/kalin/miniconda3/include
PYTHON_LIBRARY             C:/Users/kalin/miniconda3/libs/python39.lib
``` 
Note that your python library may be a different version from python39.
** Click 'Configure' once again and ensure that the configuration is successful once more, and if so then click 'Generate'
* '''Build LCM in Visual Studio'''
** Navigate to the build folder for LCM, where you generated the binaries, and open up lcm.sln in Visual Studio
** In the top, for the solution configuration, change it from Debug to Release, and then in the Build tab at the top select 'Build Solution'
* '''Install LCM using Visual Studio'''
** Open Visual Studio as an administrator, and then open up lcm.sln
** In the solution explorer panel on the right hand side, locate INSTALL, right click it, hover over 'Project Only' and select 'Build Only INSTALL'
* '''Add LCM to PATH'''
** Add ```C:\Program Files (x86)\lcm\bin``` (This allows access to LCM commands in the command prompt)
* Test your installation (see [https://lcm-proj.github.io/tutorial_general.html https://lcm-proj.github.io/tutorial_general.html] for a list of available LCM tutorials with scripts that you can easily use to test if everything is working)

### Notes For Windows 7 (IVER Backseat)
* When installing python, the last version of python that supports Windows 7 is Python 3.8, so rather than downloading the latest miniconda release, download the last version that shipped with Python 3.8 from [https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Windows-x86_64.exe](https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Windows-x86_64.exe).

## Additional Steps For C++ in Visual Studio
* Create a new project
* In the Project tab, select select your project's properties (it should be the very last item in the drop-down menu)
* In Configuration Properties, select VC++ Directories
** add ```C:\Program Files (x86)\lcm\include;``` to the end of the Include Directories field
** add ```;C:\Program Files (x86)\lcm\lib;``` to the end of the Library Directories field
* In Linker, select Input
** add ```;lcm.lib;lcm-static.lib``` to the end of the Additional Dependencies field
* Now switch from Debug to Release and perform the same changes as above
* Then in the Project drop-down menu select Export Template, select the project you have just modified, and create a new template based on that project. 
* Now you can create new projects using that template that will all be ready to go with LCM readily available through #include <lcm/lcm-cpp.hpp>

## Additional Steps For Python
Ensure that you always use the base conda python environment, as that is what you have now installed lcm to. If you try to run a script that uses lcm with another python environment or version, it most likely will not work. 
While you can install lcm multiple times, using different python environments, I highly recommend that you don't, as that will take a lot of time and is likely very unnecessary. Ultimately it'll be much easier on Linux where you can just create a new python environment and pip install lcm. On Windows it's much more involved, so just use the base conda environment, which is where this guide will have the python package installed for.

Initially python will not be able to find the lcm package, in order to fix that please do the following:
* Add LCM Python package to Environment Variables
** Check your environment variables, if one called PYTHONPATH exists, then edit it, otherwise create a new variable called 'PYTHONPATH' and add the following to the value field ```C:\Program Files (x86)\lcm\lib\site-packages ```
