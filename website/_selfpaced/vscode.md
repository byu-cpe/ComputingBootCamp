---
layout: page
toc: true
title: VS Code
slug: vscode
type: development
order: 3
---



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

## Tutorial

On May 3, 2021 we had a VS Code Tutorial by Prof Goeders. The video is embedded below

<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/KetWeah5Z9A"> </iframe>

**Tutorial Topics**:
  * Take a tour: (3:24)
    * Opening Files (5:12)
      * File vs Folder vs Workspace
      * Reload workspace (Ctrl+R)
      * Open file (Ctrl+P)      
    * Viewing files (11:05)
      * Split views
      * File previews (markdown)
    * Working with code: (13:59)
      * Syntax highlighting 
      * Autocomplete
      * Auto parameters
    * Sidebar (19:33)
    * Terminal (and multiple terminals)  (21:20)
  * Extensions    (22:22)
  * Remote Access (SSH) (27:20)
  * Settings (32:46)
    * How to access JSON settings
    * User vs Workspace settings 
    * Extension settings     
    * Settings Sync
  * Launch Configurations (Debugging) (40:45)
  * Tasks (46:51)
  * Github / Pull Request Integrations (49:00)
  * Git Integrations (51:22)
  * Package recommendations (53:25)
 
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

### Formating Code
VS Code provides the ability to format your code automatically. Depending on the language of your code a formater may be already available for others you may need to install one. Once a formatter is installed it can be configured to format on save. Some languages and formaters also all formating on paste or formating when line is completed. You can manually format the code using the keystroke `Ctrl+Shift+I`. If you choose to use a formater make sure your formater and settings match those of the project you are working on.

#### Python
VS code does not by default have a python formater. The recommended formater to use is [Black](https://black.readthedocs.io/en/stable/). To install black simply run 
```
pip install black
```
Then, open your settings.json file. The settings you will need to add are:
```
    "python.formatting.provider": "black",
    "[python]": {"editor.formatOnSave": true}
```
The first setting specifies our chosen formatter. The second enables formating on save for python files. 

To adjust the formater's settings you may set `"python.formmating.blackArgs"`. For instance, the folowing example sets the max line length to 100.
```
"python.formatting.blackArgs": ["--line-length", "100"]
```
See [this page](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html), for more information on Black's settings.

#### C/C++
VS code uses clang-format to format C and C++ code by default. You can enable the formater to format on save as well as to format a line whenever you type `;` using the following settings.
```
"C_Cpp.formatting":"clangFormat",
"[c]":{"editor.formatOnSave": true, editor.formatOnType": true},
"[cpp]":{"editor.formatOnSave": true}
```
The first line is not required unless the default formater has been changed. 

The formater settings can be changed from the default by placing a file named `.clang-format` in your project directory. You can read more about that [here](https://clang.llvm.org/docs/ClangFormatStyleOptions.html)

*Note:* VS Code assumes cpp files contain C++ code and C files contain C code. With h files, VS Code by default assumes they are C++ code and will apply cpp settings to them. You can specify the file to use C using [these steps.](https://code.visualstudio.com/docs/languages/overview#_changing-the-language-for-the-selected-file)

### Extension recomendations
There are a multude of extensions for VS Code. Which to install will depend both on personal preference and the projects you are working on. Below is a list of some useful extensions. 
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
  * Provides usful visualization for debugging
* [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
  * Allows management of Github pull requests and issues from VS Code. 
* [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
  * Allows easy integration with Docker

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
