---
layout: page
toc: true
title: Setup Linux
lab: 1
type: setup
order: 3
---


## Clean Install of Linux

Add description/pointer to tutorial on doing a clean install of Linux on a machine.

* You should install Ubuntu 18.04 LTS or Ubuntu 20.04 LTS (do we care which one?)


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

### SSH Keys
Instead of having to authenticate with a password each time connecting to the PYNQ, you can set up an SSH key to do automatic authentication.  [This tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1804) explains how to set this up in a variety of ways.

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