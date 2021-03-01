---
layout: page
toc: true
title: Customize Your VM
lab: 1
type: setup

---

# Do This First
These are useful steps to immediately do with your new Linux VM.
* RapidSmith and RapidSmith2 have been written in Java. In order to use either one of theses libraries, we need to download the Java jdk and the Java jre. The following terminal command will install both on the provided Linux VM
  * ``sudo apt install default-jdk``


* Set up your coding environment. We recommend that you use VS Code, however we are not requiring a specific environment to be used. If you choose to use something other then VS Code, you will likely be on your own to get everything working. If you decided to use VS Code, there are many extensions that would enhance the coding experience. For example, with java it is highly recommendation that you download the java extension pack from the extension list. This will install several extensions that will make it easier to code in java in VS code.
  * Depending on the project, you might need to tell VS Code where library files are located on your machine. At this point, you can skip setting up external libraries until you are ready to install/setup the libraries. Just be aware that further work is likely needed before working on your projects.

After finishing setting up Linux VM, it might be useful to create a backup of it. If you are not careful, it is very easy to damage Linux with carefree use of sudo. A backup of the VM will allow quick and easy recovery to a state where everything is installed and ready to use.

# Things you could/should do later to customize it:

## 1. Learn to use the Linux command line.  
Vivado usually does not install any icons on the
Desktop (it is a Vivado bug that seems to come and go) 
and so you will be running it from the command line as in:``vivado`` or ``vivado -mode tcl``.

## 2. Increase Memory and Processors
You will definitely want to increase memory and processors, based on the
host's capabilities.  For a 16GB Macbook Pro, I give it 8GB of RAM
and 4 processor cores.  

## 3. Hard Code Your Machine's IP Address
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

## 4. Put your Linux Machine in Your Local Hosts File
If you do #3, then give a name to refer to your machine that your local
PC can use to refer to when using it.  

If on a Mac or other Unix-like machine add an entry in /etc/hosts with the IP address and your VM name:
  * ``sudo vi /etc/hosts`` will let you edit it (but you have to know some vi)

You can search the web for how to do it on your particular Windows installation.

## 5. Install an IDE
You may want to install an IDE.  But, there is a reason we did not -
VS Code has a wonderful remote capability where you can just have VS
Code on your local PC and always remote in to edit, execute, debug on
the VM.  

You can open a terminal right on the remote machine from within
a locally running VSCode.  By running VS Code locally you are in your familiar
PC environment, simplifying many things (like mappings for alt,
command, option, control, ...).  However, feel free to install an IDE
on the VM.  Either way, we recommend VS Code.

## 6. Set Up SSH Keys So You Don't Have to Always Log In When Accessing a Remote Machine
You may want to set up ssh keys so you don't have to log in to the
VM every time you want to open a shell on it from your PC and you
don't have to specify a password when using ssh to log in.

To learn how, follow [these instructions](https://github.com/byu-cpe/BYU-Computing-Tutorials/wiki/SShKeys).  Note that for what you are doing here, the "remote machine" is your VM and the "local machine" is your PC.  However, you can always reverse the roles if you want to initiate communications from your VM back to your PC.

# More Advanced Things You Might Need to Do

## Increasing Disk Space
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

# Upgrading Vivado

Your VM’s have the Xilinx WebPack on them which is a chopped down (but quite useful version).   But, you may need to upgrade depending on what you are doing.  You do this by going into Vivado and in Help there is an upgrade devices or something link.  Fire that up.  It will start the installer.

The version you want is probably still 2017.2? but you don’t want WebPack you want the “real one”.  It is NOT Vivado Lab (that is just the download tool).  Also, you do not need SystemGenerator (which is the one just below the one you want).  

When done, you have to set the license for it.  All you do is add this to your .bashrc file:


Then, restart your terminal for it to take effect and Vivado should be happy.
