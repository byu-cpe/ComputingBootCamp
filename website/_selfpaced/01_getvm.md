---
layout: page
toc: true
title: Get a VM
lab: 1
type: setup
order: 1
---

# Getting and Running a Linux Virtual Machine

The system we will develop on is a Linux installation on a VMWare Virtual machine.  This is a self-contained Linux system which can be run "inside" another operating system (typically Windows or Mac).   We use this because some of the tools we work with have specific requirements as to the Linux they will run on. 

1. CAEDM has links to how to get free 1-year licenses to VMWare for students.  We will run our virtual machine in VMWare.  Search for it, find it, and install VMWare on your local machine.  If you are on a Mac there is likley only one option (VMWare Fusion).  For Windows, get "VMWare Workstation Pro" and the platform to choose is "Windows" (since you want to run the VMWare software on Windows).
1. The VM we will run can be found: [here](https://byu.box.com/s/5sx0v7fgsjenyzryd4cvf2sdgrgpog8c).  There is a directory there called: Student_Ubuntu16.04.6_Xilinx-2017.2.  On the right, click Download->Folder.
1. It downloads it as a ZIP file, unzip it.
1. Then, open VMWare and "Open Virtual Machine" it, selecting the file with the .ovf extension.  It will ask where to put it - your home directory is a recommended place.
1. Log in with "student", password "fpga".
1. See [Create a VM]({% link _selfpaced/02_createvm.md %})  for how the virtual machine was originally created/configured. 
1. For things to do to customize your VM, see [Customize Your VM]({% link _selfpaced/03_customizevm.md %}).

