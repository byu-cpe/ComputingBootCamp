---
layout: page
toc: true
title: VS Code
slug: vscode
type: development
order: 3
---
## Overview 
VS Code is an editor that has risen in popularity in recent years. The 2021 stackoverflow developer survey reported that around 70% of respondants use VS code (see survey results [here](https://insights.stackoverflow.com/survey/2021#most-popular-technologies-new-collab-tools)). VS code is a versitile text editor with a vast array of extensions that allow easy coding in many different languages. VS code does not have any inbuilt compiling tools however it can easily interact with those that you have installed. VS Code can be configured to run python scripts and compile C code but requires the needed programs to be installed for it to do so (python or GCC or similar). With the proper use, VS code can be an efficient tool as you work on many projects. 


## Installation

Download .deb file from <https://code.visualstudio.com/>

Install (your file may be named differently):
    
    cd ~/Downloads
    sudo dpkg -i code_1.54.3-1615806378_amd64.deb

## Running 

You can open files from the command line using:
```
code <path_to_file>
```

Alternatively you can open entire directories in VS Code:
``` 
code <path_to_dir>
```

Alternatively you can open the program using the GUI and then choose a folder or file to open.

## Tutorial

On May 3, 2021 we had a VS Code Tutorial by Prof Goeders. The video is embedded below

<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/KetWeah5Z9A"> </iframe>

### Timestamps

[0:00](https://www.youtube.com/watch?v=KetWeah5Z9A&t=0s) Introduction<br>
[3:24](https://www.youtube.com/watch?v=KetWeah5Z9A&t=204s) Take a tour<br>
[5:12](https://www.youtube.com/watch?v=KetWeah5Z9A&t=312s) Opening files
  * File vs Folder vs Workspace
  * Reload workspace (Ctrl+R)
  * Open file (Ctrl+P)

[11:05](https://www.youtube.com/watch?v=KetWeah5Z9A&t=665s) Viewing files
  * Split views
  * File previews (Markdown)

[13:59](https://www.youtube.com/watch?v=KetWeah5Z9A&t=859s) Working with code
  * Syntax highlighting
  * Autocomplete
  * Auto parameters

[19:33](https://www.youtube.com/watch?v=KetWeah5Z9A&t=1173s) Sidebar<br>
[21:20](https://www.youtube.com/watch?v=KetWeah5Z9A&t=1280s) Terminals<br>
[22:22](https://www.youtube.com/watch?v=KetWeah5Z9A&t=1342s) Extensions<br>
[27:20](https://www.youtube.com/watch?v=KetWeah5Z9A&t=1640s) Remote access (SSH)<br>
[32:46](https://www.youtube.com/watch?v=KetWeah5Z9A&t=1966s) Settings
  * How to access JSON settings
  * User vs Workspace settings
  * Extension settings
  * Settings Sync

[40:45](https://www.youtube.com/watch?v=KetWeah5Z9A&t=2445s) Launch Configurations (Debugging)<br>
[46:51](https://www.youtube.com/watch?v=KetWeah5Z9A&t=2811s) Tasks<br>
[49:00](https://www.youtube.com/watch?v=KetWeah5Z9A&t=2940s) GitHub/Pull Request Integrations<br>
[51:22](https://www.youtube.com/watch?v=KetWeah5Z9A&t=3082s) Git Integrations<br>
[53:25](https://www.youtube.com/watch?v=KetWeah5Z9A&t=3205s) Package recommendations
 
## VS Code Tips
* Settings:
  * JSON

  * Word wrap
  * [python.analysis.extraPaths](https://github.com/byuccl/bfasst/blob/master/.vscode/settings.json)
  * [Include paths](https://github.com/byu-cpe/ecen427_student/blob/master/.vscode/c_cpp_properties.json)
* Settings sync
* Markdown preview
* Latex run and preview
* Run on save
* Package recommendations
### Setting up Debugger 
Properly configured VS code can run a debugger allowing you to step through and inspect your code. A brief explanation of the setup and use of the debugger is given below with a focus on C++ and Python. An extremely detailed explanation of all of the available features and settings can be found [here](https://code.visualstudio.com/docs/editor/debugging).

All launch configurations are stored in a file named launch.json in the .vscode folder. If your workspace does not yet have a launch.json file, create one by going to the debug tab and select creat a launch.json file. After a launch.json file has been created, you can add configurations either by manually typing them in or by selecting the add configuration button. This will allow you to choose from a number of preset configurations (based on your installed extensions) that you can then edit for your specific application. Note: many languages have both a launch and attach preset. In most cases, you will want launch as attach does not start an application it merely debugs an already running one. 

Settings that are common to most language configurations include the following
* `"name"`
    * This is the name that will be displayed in VS code for the configuration
* `"type"`
  * this denotes the language of the code.
* `"request"`
  * Either `"launch"` or `"attach`. Launch will start the program attach merely connects to an already running proccess
* `"program"`
  * The path to the script or executable
* `"cwd"`
  * The directory your code will be executed in.
* `"args"`
  * The arguments to be passed to your program

Two useful variables that can be used in the settings are `${file}` which holds the path to the currenly open file. And `${workspaceFolder}` which refers to the root folder of your workspace. 
#### C/C++
Below is a simple example configuration for C or C++.
```
{
    "name": "(gdb) Launch",
    "type": "cppdbg",
    "request": "launch",
    "program": "${workspaceFolder}/main",
    "args": [],
    "stopAtEntry": false,
    "cwd": "${workspaceFolder}",
    "MIMode": "gdb"
}
```
The two settings specific to C/C++ is `"type"` and `"MIMode"`. The type is set to `"cppdbg"` to indicate the language being used is either C or C++. `"MIMode"` is set to `"gdb"` to indicate that we want to debug using gdb. If you are using a Mac, you may need to change this to `"lldb"` as that is the debugger that is by default installed. 

Also notice that program points to a compiled executable, not to the source code. You must compile your C/C++ code before launching.

Additional C/C++ settings can be found [here](https://code.visualstudio.com/docs/cpp/launch-json-reference).

#### Python
Below is a simple example configuration for Python.
```
{
    "name": "Python: Current File",
    "type": "python",
    "request": "launch",
    "program": "${file}"
}
```
This example is quite simple. The program type of python is specified and program is indicated by `${file}`. This means that this configuration will run and debug whichever python file we currently have open. If that is desired `${file}` can be replaced with the path to a specific file. 

Additional information on Python-specific debugging can be found [here](https://code.visualstudio.com/docs/python/debugging).


### Formatting Code
VS Code provides the ability to format your code automatically. Depending on the language of your code a formatter may be already available for others you may need to install one. Once a formatter is installed it can be configured to format on save. Some languages and formatters also all formatting on paste or formatting when line is completed. You can manually format the code using the keystroke `Ctrl+Shift+I`. If you choose to use a formatter make sure your formatter and settings match those of the project you are working on.

#### Python
VS code does not by default have a python formatter. The recommended formatter to use is [Black](https://black.readthedocs.io/en/stable/). To install black simply run 
```
pip install black
```
Then, open your settings.json file. The settings you will need to add are:
```
    "python.formatting.provider": "black",
    "[python]": {"editor.formatOnSave": true}
```
The first setting specifies our chosen formatter. The second enables formatting on save for python files. 

To adjust the formatter's settings you may set `"python.formatting.blackArgs"`. For instance, the following example sets the max line length to 100.
```
"python.formatting.blackArgs": ["--line-length", "100"]
```
See [this page](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html), for more information on Black's settings.

#### C/C++
VS code uses clang-format to format C and C++ code by default. You can enable the formatter to format on save as well as to format a line whenever you type `;` using the following settings.
```
"C_Cpp.formatting":"clangFormat",
"[c]":{"editor.formatOnSave": true, editor.formatOnType": true},
"[cpp]":{"editor.formatOnSave": true}
```
The first line is not required unless the default formatter has been changed. 

The formatter settings can be changed from the default by placing a file named `.clang-format` in your project directory. You can read more about that [here](https://clang.llvm.org/docs/ClangFormatStyleOptions.html)

*Note:* VS Code assumes cpp files contain C++ code and C files contain C code. With h files, VS Code by default assumes they are C++ code and will apply cpp settings to them. You can specify the file to use C using [these steps.](https://code.visualstudio.com/docs/languages/overview#_changing-the-language-for-the-selected-file)

### Extension recommendations
There are a multitude of extensions for VS Code. Which to install will depend both on personal preference and the projects you are working on. Below is a list of some useful extensions. 
* [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools):
  * Provides basic support for C/C++
* [C/C++ Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools-extension-pack): 
    * Provides additional tools for C/C++ including C-make and Doxygen support.
* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  * Provides basic support for Python
* [Hex Editor](https://marketplace.visualstudio.com/items?itemName=ms-vscode.hexeditor):
  * Allows viewing of binary files in VS code.
* [Remote-SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
  * Allows VS Code to run on a remote machine
* [Debug Visualizer](https://marketplace.visualstudio.com/items?itemName=hediet.debug-visualizer)
  * Provides useful visualization for debugging
* [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
  * Allows management of Github pull requests and issues from VS Code. 
* [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
  * Allows easy integration with Docker

## Activities 
Bellow are several activities that might help you familiarize yourself with VS Code
### Configure the settings
Create a test project or open an existing one and setup VS Code's settings to fit. Try to setup the formatter and the debugger.

### Try the debugger
Try to debug a program in VS Code. Clone the Bootcamp repository and use the VS Code debugger to find the errors in the VS Code example untill you can get the expected output.


## Additional resource
VS Code has extensive tutorials and documentation. Below is a list of pages on key topics. Links to specific topics were included as part of the various tips. The full document can be found [here](https://code.visualstudio.com/docs)

<!---
## Faculty Brainstorming 
  To be added...   There is a lecture on this topic, we should schedule this to be just after that lecture.

##Possible topics
Some of these topics might deserve a full-blown text description.  

Others might just be a mention of some feature in the spirit of: "did you even know you can do X?  Go look it up, it will change your life...".    Maybe there could be a list of these and the student assignment is to choose and go figure out `n` of them and implement in your VS Code setup.   

- Installation - point to something
- Why you ONLY want it on your local machine - the ssh is too good to waste time otherwise and you will never keep the various versions in synch in terms of extensions and settings.
- The ssh remote capability for just editing and the like
- Debugging using the ssh remote.  Detail Python vs. C++ is there are significant differences.
- Any advantages of the local terminal instead of one on the remote machine?  Yes, big advantages, detail those.
- Extensions - how they work, how to install them, cool ones we know of they will not have  thought of...
- Writing your own keyboard macros.  Students likely don't need this, it is for me!  I have figured it out twice now and then forget how to do it by the next time I try next :-)

What else?
--->
