---
layout: page
toc: true
title: Linux Setup & Tutorials
slug: linux
type: development
order: 0
---


## Installing Linux

You may be asked to wipe your computer and install a clean version of Linux.  Please do not wipe your lab computer without your advisor's permission as old students may still be using your computer.

To install Ubuntu on your machine:
  1. Download Ubuntu 20.04 LTS from <https://ubuntu.com/download/desktop>
  1. Create a bootable USB: <https://ubuntu.com/tutorials/create-a-usb-stick-on-windows>
  1. Install using the USB: <https://ubuntu.com/tutorials/install-ubuntu-desktop>

## Lecture Video

On April 27, 2022 Dr. Wirthlin gave a brief overview of Linux. The video is embedded below.

<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/Zjoc77AC8IA"> </iframe>


## Learn the Command Line

Our work will be nearly 100% Linux and so you will want to invest significant time into becoming proficient with Linux.  It is a skill worth much and so you will be benefiting yourself by doing so.

A note: you may have grown up using computers via a GUI.  Linux is different - there may only be two uses for using the built-in Linux GUI:

1. The menu on the left is useful for holding programs you can click to run (Firefox, New Terminal, ...).
1. The icons in the extreme upper right of the window are useful for setting system configurations (so you don't have to learn how to do everything from the command line).

OK, so we exaggerate, but you get the point...

<!-- ### The Linux Command Shell - _bash_
Beyond that you will spend the majority of your time typing things in the command shell.  The default is called _bash_.   -->
<!-- 
Everything in Linux can be (and usually is) run by shell scripts and commands so learn them.  There are hundreds, start with these at a command prompt:

    man (as in "man man" - show me the manual page for "man" command)
    apropos (as in "apropos file" - tell me all the commands that do things with files) -->


### Linux Tutorial 
**<ins>You must to read through and complete all steps of this tutorial</ins>**: <https://ryanstutorials.net/linuxtutorial>.  Even if you are already familiar with Linux and the command line, please read through the different topics and bring yourself up to speed on any you aren't familiar with.

{% include quizzes.html id=6 %}

### Linux Resources (please add to this as you find good stuff)
Here are some Linux tutorials that may be helpful:

* <https://learning.oreilly.com/library/view/ubuntu-linux-unleashed/9780136685395/> A good, full book on Linux - with your academic credentials you may have free access to it (for BYU students that is the case)
* <https://tldp.org/LDP/abs/html/index.html> Advanced Bash Scripting Guide
* <https://www.grymoire.com/Unix/> Tutorials on awk, sed, grep, make and find
* <https://danielmiessler.com/study/vim/> Opinionated tutorial on vim
* <https://stackoverflow.com/q/1218390/1220118#1220118> Making vim make sense
* <https://blog.sanctum.geek.nz/unix-as-ide-introduction/> How to make Linux tools work together

## Setting Up Your Environment

### Update your Packages

After installation you should apply any pending updates to the packages installed on your computer.  First run this to query the package mangers and get a list of current package versions:
```
sudo apt update
```

Then update any out of date packages:
```
sudo apt upgrade
```

### Install an Editor

In many tutorials you will be asked to edit files.  It is good to be familiar with a command-line editor like Vim, nano, or Emacs in order to make quick edits without needing a GUI, but if you prefer to always use a GUI for editing files, that's fine.  

There are some instructions on installing and running VS Code [here]({% link _modules/vscode.md %}).


## Other Things to Learn and Set Up

### SSH

SSH provides you with remote command-line access to another computer.  You will likely to need to connect to other computers during the course of your research.  You can connect to other machines using either `ssh <IP_address>` or `ssh <computer_network_name>`.

Try it out by connecting to the CAEDM SSH server:
```
ssh ssh.et.byu.edu
```

By default it will try and connect using the same username that your are logged in with on your current machine.  If you need to change username (for example, suppose your CAEDM username was *cosmo*), you can do this:
```
ssh cosmo@ssh.et.byu.edu
```

### scp
Copy files to and from a remote machine as in:

    # Copy file1 from my machine to the Downloads directory on another machine
    scp file1 student@192.168.52.23:Downloads

    # Copy the .bashrc file from remote machine to /tmp on my machine
    scp username@hostname:.bashrc /tmp

This is how you move files between machines.

{% include quizzes.html id=7 %}

### SSH Keys
Instead of having to authenticate with a password each time you connect to a remote machine, you can set up an SSH key to do automatic authentication.  [This tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1804) explains how to set this up in a variety of ways.

You will need to add your SSh Key to you GitHub account. This will allow you to use you account with authentication and reconfigure local repositories. [This page](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) should walk you through the instructions on adding this to you account. 

A few of notes __before__ following the tutorial:
  * If your computer doesn't have ''ssh-copy-id'' installed, you will need to follow the instructions below that
  * Although it is less secure, it is nicer if you do not specify a passphrase for the key.  Presumably your computer is protected by password, which makes not having a passphrase less of an issue.
  * You probably don't want to follow Step 4 of the tutorial

Before proceeding, make sure you can ssh into `ssh.et.byu.edu` without being prompted for a password.

### SSH Config

You can create an SSH Config file in order to save SSH preferences.  This file is located at `~/.ssh/config`.  Each entry in this file lists a remote machine that you can connect to by alias.

For example, to connect to the CAEDM SSH server by only running `ssh caedm` you would add an entry to the file like this:
```
Host caedm
    Hostname ssh.et.byu.edu
    User cosmo
```

You can remotely connect to an individual machine by tunneling through an SSH server on the same network as the machine. To accomplish this, use SSH to connect to the SSH server, then use SSH again within the same session to connect to the remote machine.

This can be automated by adding `ProxyJump` to your Config file entry for the machine, and optionally adding `IdentityFile` to allow for passwordless key authentication, like this (appended below the above CAEDM example):
```
Host myDesktop
    Hostname 10.2.111.111
    User cosmo
    ProxyJump caedm
    IdentityFile ~/.ssh/privateKeyName
```

{% include quizzes.html id=8 %}

<!-- # Faculty Notes
- Writing shell scripts (especially if they take parameters)
- Really understanding and manipulating permissions.  It is true the GUI can do it (with about 9 clicks) but when when knowledgeable people start talking about them as in 'permission should be 755' we don't want them to lost.
- Things like `find . -name \*.sv -exec cp {} /tmp \;`  (OK, so that may be a bit obtuse but I use it multiple times per week).  But, even things like `chgrp fpga *.sv` are useful
(This should all be covered in the tutorial now)

What else?
-  -->
