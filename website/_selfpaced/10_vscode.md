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
  * Format on save
  * Word wrap
  * [python.analysis.extraPaths](https://github.com/byuccl/bfasst/blob/master/.vscode/settings.json)
  * [Include paths](https://github.com/byu-cpe/ecen427_student/blob/master/.vscode/c_cpp_properties.json)
* Settings sync
* Markdown preview
* Latex run and preview
* Run on save
* Package recommendations

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
