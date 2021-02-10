# The BYU Computing BootCamp

# Bootcamp Planning for 2021

### Published Units (in SelfPaced directory)
These are self-paced learning activities on the wiki.  Typically, they have the students read about topic, install the tool, and then complete a series of mini-projects to actually use the topic's tool and do some useful things with it.

Last year we gave them a schedule to follow and adjusted it as some things took longer/shorter than we thought.  I took a guess at grouping them into weeks for this year.

#### Week 1
- Getting The Pre-Canned Linux Virtual Machine
    - Creating Your Own Virtual Machine Instructions
- Learning Linux - Reference Materials
- Customizing Your Linux VM

#### Week 2
- Vivado Tcl: Command Line Scripting Using the Tcl Language
    - Using `vivado -mode tcl` for command line usage (non-project mode)
    - Using Tcl to control Vivado operation and synthesis/implementation phases
    - Writing Tcl programs to analyze/manipulate designs

#### Week 3
- Git, Github, Github Best Practices
- RapidWright Bootcamp
    - RapidWright Interchange Format

#### Week 4
- Symbiflow Bootcamp
    - Prjxray
    - FASM, fasm2bits, ...
    - Fasm2Bels

#### Week 5
- Symbiflow-VTR Bootcamp

### Group Talk Schedule
These are talks presented by faculty/students (mostly faculty) at our weekly meetings.  Last year we met 2x/week during May, then the Immerse talks started up on Wednesdays and so we switched to 1x/week until mid-July.

| Date | Talk Topic(s) |
| --- | ---  |
| Mon May 3  | Welcome |
|            | Linux VM () 
| Wed May 5  | VS Code ()
| Mon May 10 | Python 
| Wed May 12 | C++ programming helps ()
|            | `make` and `cmake` () 
| Mon May 17 | GIT and Github () 
| Wed May 19 | RapidWright and Interchange (?) 
| Mon May 24 | Prjxray & FASM ()
|            | fasm2bels, fpga-tool-perf, symbiflow-examples ()
| Wed May 26 | Start Immerse talks 
| Mon May 31 | HOLIDAY
| Mon Jun 7  | VTR and Symbiflow-VTR () 
| Mon Jun 9  | LaTeX ()
|            | ReadTheDocs ()
| Mon Jun 16 | Docker ()
|            | Travis-CI ()


### More Details on the Above Bootcamp Talks
- Talk on Linux VM's
    - Obtaining/creating
    - Configuring/modifying
        - Increasing memory/processors in VMWare
        - Hard code IP address, /etc/hosts file
        - Using package managers
        - SSH keys
        - Increasing disk size
- Talk on VS Code
    - Basic usage, extensions
    - Buit-in help
    - Configuration file
    - Ssh:  remote use on other machines
    - Debugging python: setup and usage
- Talk on git
    - Git basics
    - Use of github: direct clone vs. forks
    - Contributing to SW projects using PR's or forks
- Talk on Python: 
    - Virtual environments in general, conda in particular
        - System python vs. user python
        - Activating/deactivating
        - Preventing base frm starting up on login
        - The requirements.txt file
    - Scripts vs. stand-alone programs
    - Python path
    - Python pathlib module
    - Modules and the __init__.py file
    - Python argparse module
- Talk on C++ programming helps
- Talk on cmake and make
- Talk on prjxray and FASM
    - Fuzzers
    - The database and libraries to access
    - FASM
    - fasm2bels, fpga-tool-perf, symbiflow-examples
- Talk on VTR
    - Base VTR
    - Symbiflow-vtr
- Talk on LaTeX
- Talk on ReadTheDocs
- Talk on 'Travis CI'
- Talk on Docker

---
## Other Things
Group 1 are the things discussed above.

### Group 2: Things That Are Documented, But Only Pointed To (not covered in talks)
- Networking in a Linux VM
- SSH Keys
- SystemVerilog Testbenches - An Alternative to Tcl

### Group 3: Things Mentioned as of Interest for Future Inclusion in Group 1 or 2
- gradle
- maven
- pandoc
- sphinx
