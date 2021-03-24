---
layout: page
toc: true
title: Create a VM
lab: 1
type: setup
order: 2
---

# Machine Creation Script
* Use ubuntu-xx.xx.xx-desktop-amd64.iso - get from Ubuntu website (do a search) - the xx.xx.xx are version numbers.  You may want 16.04, 18.04, 20.04, or some other version.  You will note they all end in ".04" - these are the LTS or long term support versions of Ubuntu Linux.

* Create new machine using VMWare, specifying above file when asked.  Specify whatever you would like for 
  * Username: student
  * Password: fpga

* Customize settings (can be changed in VM settings later):
  * 2GB RAM
  * 1 CPU
  * 60 GB disk (harder to change later but can be done)
    * When all is said and done, this VM takes up just about 20GB but you need nearly 60GB for the install files.

* Wait until the install finishes being created and log into it.  Every below are things you now do inside the Linux virtual machine.  You do it from a terminal (command prompt).  To get one started, right-click in middle of screen and select "New terminal" or similar choice.  A command window will appear.

NOTE: you prefix a lot of commands below with the word 'sudo' - this means run the following command as an administrator.  BE CAREFUL and only use it when you have to - you can totally trash your installation by doing the wrong thing with sudo.

* Give your machine a name
  * ``sudo hostname StudentFPGA``

* Update system software installer catalog
  * ``sudo apt update``

* When you first create a VM it immediately goes out and looks for
certain updates.  So, you may have to wait a few minutes until you
can do this.  You will get errors until the coast is clear.  The following 
will basically upgrade all the software in your VM.  Doing so is completely optional. 
It will take 10-20 minutes.  You can always do it later.
  * ``sudo apt upgrade``

* Install the VM tools (Ubuntu prefers these to what VMWare provides).  
Depending on the ubuntu system you are working with these may or may not already 
be installed.  Doing it even if they are installed won't hurt.
  * ``sudo apt install open-vm-tools open-vm-tools-desktop``

* Reboot the machine (I do it just to make sure everything I just installed is running
the needed daemons, etc.
  * ``sudo shutdown -r now``

Moving on, we will install a few more things you will need:
* SSH
  * ``sudo apt install openssh-server``
  * ``sudo systemctl status ssh``
  * ``sudo ufw allow ssh``

* git
  * ``sudo apt install git -y``

* emacs (optional) - this is a text editor that some people use.  There are other programs built in on Linux you will likely prefer (it is here because I like it).  The programs 'vi' and 'nano' are two common built-in ones.  Either of them will be fine.
  * ``sudo apt install emacs -y``

* Xilinx VIvado
  * Increase CPU's and memory in the VM first (see below)...  

Instructions:
  * Get -> xilinx.com -> support -> downloads/licensing -> Vivado Archive -> xxxx.x -> Vivado HLx xxxx.x WebPACK and Editions - Linux Self Extracting Web Installer (xxxx.x will depend on the version you want)
  * ``cd Downloads``
  * ``chmod 755 Xilinx...  (... means hit the TAB key to let command completion finish it)``
  * ``./Xilinx...``

  * Choose Webpack (top option)
  * Unselect Ultrascale and Ulstrascale+ devices
  * Select DocNav
  * Put it in /home/student/Xilinx_xxxx.x
  * Takes a while to install

Regardless of which method you use, then:
* Add to end of the .bashrc file in your home directory (using a text editor).  Remember
to change the xxxx.xx to be your Vivado version:
  * ``# Set environment to run Xilinx tools.  Remove if you don't want/need it.``
  * ``source ~/Xilinx_xxxx.x/Vivado/xxxx.x/settings64.sh``
  * ``# Keep .log and .jou files from cluttering up the entire filesystem``
  * ``alias vivado="vivado -log /tmp/vivado.log -journal /tmp/vivado.jou"``

* When done, install cable drivers
  * Refer to https://www.xilinx.com/support/documentation/sw_manuals/xilinx2018_3/ug973-vivado-release-notes-install-license.pdf
  * Commands below are broken into 2 separate cd commands so it will fit on the screen for this wiki...
  * ``cd ~/Xilinx_xxxx.x/Vivado/xxxx.x``
  * ``cd data/xicom/cable_drivers/lin64/install_script/install_drivers/``
  * ``sudo ./install_drivers``

