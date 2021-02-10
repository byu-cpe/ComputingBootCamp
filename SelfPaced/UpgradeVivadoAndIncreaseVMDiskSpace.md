# Upgrading Vivado

Your VM’s have the Xilinx WebPack on them which is a chopped down (but quite useful version).   But, you may need to upgrade depending on what you are doing.

You do this by going into Vivado and in Help there is an upgrade devices or something link.  FIre that up.  It will start the installer.

The version you want is probably still 2017.2? but you don’t want WebPack you want the “real one”, but I cannot remember the name.  It is NOT Vivado Lab (that is just the download tool).  Also, you do not need SystemGenerator (which is the one just below the one you want).  

When done, you have to set the license for it.  All you do is add this to your .bashrc file:

```
    export XILINXD_LICENSE_FILE=2100@ece-xilinx.byu.edu
```

Then, restart your terminal for it to take effect and Vivado should be happy.

# Upgrading VM Disk Space
One more thing, you may not have enough disk space on your VM.  Options include: 
1. Create a new VM with larger disk.
2. [Enlarge your existing VM’s disk space](https://askubuntu.com/questions/116351/increase-partition-size-on-which-ubuntu-is-installed/116367)

Option 2 is quicker and not that bad - if you do it I would go to at least 120GB to be safe.  Also, with 2. the instructions are not entirely clear but: a) You shut down the VM, b) Enlarge the disk space in VMWare in the settings for the VM, c) Follow the instructions in the webpage, d) Reboot as directed (maybe multiple times).
