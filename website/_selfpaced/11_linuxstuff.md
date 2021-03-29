---
layout: page
toc: true
title: Linux stuff
slug: linux
lab: 1
type: development
order: 2
---

Our work will be nearly 100% Linux and so you will want to invest significant time into becoming proficient with Linux.  It is a skill worth much and so you will be benefiting yourself by doing so.

A note: you may have grown up using computers via a GUI.  Linux is different - there may only be two uses for using the built-in Linux GUI:

1. The menu on the left is useful for holding programs you can click to run (Firefox, New Terminal, ...).
1. The icons in the extreme upper right of the window are useful for setting system configurations (so you don't have to learn how to do everything from the command line).

OK, so we exaggerate, but you get the point...

## The Linux Command Shell - _bash_
Beyond that you will spend the majority of your time typing things in the command shell.  The default is called _bash_.  

Everything in Linux can be (and usually is) run by shell scripts and commands so learn them.  There are hundreds, start with these at a command prompt:

    man (as in "man man" - show me the manual page for "man" command)
    apropos (as in "apropos file" - tell me all the commands that do things with files)

## Linux Links (please add to this as you find good stuff)
Here are some Linux tutorials that may be helpful:
* https://ryanstutorials.net/linuxtutorial/
* https://tldp.org/LDP/abs/html/index.html Advanced Bash Scripting Guide
* https://www.grymoire.com/Unix/ Tutorials on awk, sed, grep, make and find
* https://danielmiessler.com/study/vim/ Opinionated tutorial on vim
* https://stackoverflow.com/q/1218390/1220118#1220118 Making vim make sense
* https://blog.sanctum.geek.nz/unix-as-ide-introduction/ How to make Linux tools work together

## ssh and Related Commands
One of the best ways to communicate with a Linux machine (physical or virtual) is a set of command line programs that are all related.  Here is a quick rundown of the 2 most common ones:

### ssh
Open a "shell" or command line on a remote machine as in:

    ssh 192.168.52.23  # Specify machine by IP address
    ssh bluebell # Specify machine by a name

This is how you "log in" to a remote machine.

### scp
Copy files to and from a remote machine as in:

    # Copy file1 from my machine to the Downloads directory on another machine
    scp file1 student@192.168.52.23:Downloads

    # Copy the .bashrc file from remote machine to /tmp on my machine
    scp username@hostname:.bashrc /tmp

This is how you move files between machines.

The instructions at the bottom of [Create a VM]({% link _selfpaced/02_createvm.md %}) (item 6) can show you how to set it up so that your local machine is trusted by your Linux machine and so you don't have to specify your password every time.  And, if your username on your local machine is the same as the remote machine, you don't have to specify a username either and can just do:  "scp files 192.168.52.23:Downloads".

# Possible Topics to Add
Students will need to be forced to not use the GUI for everything.  Are we ready to do so?  Some topics that likely will require this might/probably include are listed below. However, I am so clueless about what the FileExplorer can do that maybe it can do all these :-(

- Writing shell scripts (especially if they take parameters)
- Really understanding and manipulating permissions.  It is true the GUI can do it (with about 9 clicks) but when when knowledgeable people start talking about them as in 'permission should be 755' we don't want them to lost.
- Things like `find . -name \*.sv -exec cp {} /tmp \;`  (OK, so that may be a bit obtuse but I use it multiple times per week).  But, even things like `chgrp fpga *.sv` are useful

What else?
- 