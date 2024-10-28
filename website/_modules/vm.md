---
layout: page
toc: true
title: Virtual Machine Setup
slug: vm_setup
type: archive
order: 1
---

This pages describes how you can download and run a provided virtual machine image, or create your own virtual machine image.

## Getting and Running a Linux Virtual Machine

The system we will develop on is a Linux installation on a VMWare Virtual machine.  This is a self-contained Linux system which can be run "inside" another operating system (typically Windows or Mac).   We use this because some of the tools we work with have specific requirements as to the Linux they will run on. 

1. CAEDM has links to how to get free 1-year licenses to VMWare for students.  We will run our virtual machine in VMWare.  Search for it, find it, and install VMWare on your local machine.  If you are on a Mac there is likely only one option (VMWare Fusion).  For Windows, get "VMWare Workstation Pro" and the platform to choose is "Windows" (since you want to run the VMWare software on Windows).
1. The VM we will run can be found: [here](https://byu.box.com/s/5sx0v7fgsjenyzryd4cvf2sdgrgpog8c).  There is a directory there called: Student_Ubuntu16.04.6_Xilinx-2017.2.  On the right, click Download->Folder.
1. It downloads it as a ZIP file, unzip it.
1. Then, open VMWare and "Open Virtual Machine" it, selecting the file with the .ovf extension.  It will ask where to put it - your home directory is a recommended place.
1. Log in with "student", password "fpga".
1. See net section for how the virtual machine was originally created/configured. 
1. For things to do to customize your VM, see section below.

## Creating Your Own VM
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

* Install Xilinx Vivado
  * First increase CPU's and memory in the VM (see below)
  * Follow [Instructions]({% link _modules/installing_vivado.md %})


## VM Customization
<!-- * Set up your coding environment. We recommend that you use VS Code, however we are not requiring a specific environment to be used. If you choose to use something other then VS Code, you will likely be on your own to get everything working. If you decided to use VS Code, there are many extensions that would enhance the coding experience. For example, with java it is highly recommendation that you download the java extension pack from the extension list. This will install several extensions that will make it easier to code in java in VS code.
  * Depending on the project, you might need to tell VS Code where library files are located on your machine. At this point, you can skip setting up external libraries until you are ready to install/setup the libraries. Just be aware that further work is likely needed before working on your projects. -->

After finishing setting up Linux VM, it might be useful to create a backup of it. If you are not careful, it is very easy to damage Linux with carefree use of sudo. A backup of the VM will allow quick and easy recovery to a state where everything is installed and ready to use.

### 1. Increase Memory and Processors
You will definitely want to increase memory and processors, based on the host's capabilities.  
For a 16GB Macbook Pro, I give it 8GB of RAM and 4 processor cores.  

### 2. Hard Code Your Machine's IP Address
You might or might not want to hard code your IP address so you always get the
same one.  To do so, click upper right gear icon, select System
Settings, Select Network. It will tell you the address you have, you
probably want to keep it since VMWare is choosing the subnet parts.
To have it be static, click Options then IPv4 Settings, then Manual,
then Add.  A typical address might be 192.168.52.130 (use whatever
your host gave it initially).  Fill that in with a mask of
255.255.255.0 and a gateway of 192.168.52.1 (usually the same as your machine's address
but with a 1 on the right end.  Sometimes it is a 2).  Set the DNS to the
gateway address.  NOTE: your address might not have the 52 in it -
depends on your system, but that is common.  Just use what
it gave you.  You can find out what it gave you with:

    ip addr
or

    hostname -I

### 3. Put your Linux Machine in Your Local Hosts File
If you do #3, then give a name to refer to your machine that your local
PC can use to refer to when using it.  

If on a Mac or other Unix-like machine add an entry in /etc/hosts with the IP address and your VM name:
  * ``sudo vi /etc/hosts`` will let you edit it (but you have to know some vi)

You can search the web for how to do it on your particular Windows installation.

### 4. Install an IDE
You may want to install an IDE.  But, there is a reason we did not -
VS Code has a wonderful remote capability where you can just have VS
Code on your local PC and always remote in to edit, execute, debug on
the VM.  

You can open a terminal right on the remote machine from within
a locally running VSCode.  By running VS Code locally you are in your familiar
PC environment, simplifying many things (like mappings for alt,
command, option, control, ...).  However, feel free to install an IDE
on the VM.  Either way, we recommend VS Code.


## More Advanced Things You Might Need to Do

### Increasing Disk Space
If you run out of disk space, no fear, you can resize the partition without erasing the disk.  Here are some instructions:

First, must increase disk size in VMWare settings for VM.  Go into Settings in VMWare for the VM (shut it down first) and increase the disk size.

Then, must tell Linux about it.  [Here are great instructions here for that second step](https://askubuntu.com/questions/116351/increase-partition-size-on-which-ubuntu-is-installed/116367).

Contents of above:

1. Run sudo fdisk /dev/sda

2. use p to list the partitions. Make note of the start cylinder of /dev/sda1

3. use d to delete first the swap partition (2) and then the /dev/sda1
partition. This is very scary but is actually harmless as the data is
not written to the disk until you write the changes to the disk. 

4. use n to create a new primary partition.

5. Make sure its start cylinder is exactly the same as the old
/dev/sda1 used to have. For the end cylinder agree with the default
choice, which is to make the partition to span the whole disk.

6. use a to toggle the bootable flag on the new /dev/sda1

7. review your changes, make a deep breath and use w to write the new
partition table to disk. You'll get a message telling that the kernel
couldn't re-read the partition table because the device is busy, but
that's ok.

8. Reboot with sudo reboot. When the system boots, you'll have a
smaller filesystem living inside a larger partition. 

9. The next magic command is resize2fs. Run sudo resize2fs /dev/sda1 -
this form will default to making the filesystem to take all available
space on the partition. 

10. Finally, sometimes startup and shutdown will take 90 seconds.  The reason is outlined [here](https://askubuntu.com/questions/639559/very-slow-boot-with-ubuntu-15-04).  Follow these instructions to remove
the /etc/fstab entry for the swap partition and then reboot.

That's it, we've just resized a partition on which Ubuntu is installed, without booting from an external drive.

### Upgrading Vivado

Your VM’s have the Xilinx WebPack on them which is a chopped down (but quite useful version).   But, you may need to upgrade depending on what you are doing.  You do this by going into Vivado and in Help there is an upgrade devices or something link.  Fire that up.  It will start the installer.

The version you want is probably still 2017.2? but you don’t want WebPack you want the “real one”.  It is NOT Vivado Lab (that is just the download tool).  Also, you do not need SystemGenerator (which is the one just below the one you want).  

