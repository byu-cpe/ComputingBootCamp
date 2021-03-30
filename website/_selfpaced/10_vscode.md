---
layout: page
toc: true
title: VS Code
slug: vscode
type: development
order: 1
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

We will be having a lecture on this topic, and will post the video here afterwards.

**Tutorial Topics**:
  * Take a tour:
    * File vs Folder vs Workspace
    * Sidebar
    * F1, Ctrl+P
    * Split views
    * File previews (markdown)
    * Terminal (and multiple terminals)
  * Syntax highlighting 
  * Extensions    
  * Settings 
    * How to access JSON settings
    * User vs Workspace settings
  * Git Integrations
  * Remote Access (SSH)
  * Launch Configurations (Debugging)
  * Other niceties: 
    * Package recommendations
    * Github / Pull Request Integrations
  


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
