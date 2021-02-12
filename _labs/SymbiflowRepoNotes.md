# Working with Symbiflow Repo

## Prjxray
* The Prjxray home page now says specifically that you need Xilinx 2017.2 to run.  Don't bother with anything newer - it has been verified to not work with them.

* Follow the setup instructions provided on the Prjxray page - there is a fairly long procedure required.

* Installing Prjxray on Ubuntu 16.04 goes without a hitch when following the instructions.   Ubuntu 16.04 has Python 3.5 installed natively.

* Installing on Ubuntu 18.04, which has Python 3.6 had problems.  
  * Everything worked just fine up until it hit  Step 5 of the prjxray install instructions where you get a pyjson5 install error.  
  * If you follow the instructions to build pyjson5, it complains about a missing cython Python module.  
  * When you do "pip3 install cython" it installs it for 3.5.2, not 3.6.
  * One idea from Easquel, visiting student from China (hasn't been tried yet): 
    * _sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1_
  * SOLUTIONS are being solicited so Ubuntu 18.04 can be used...
  * One easy solution to this problem would be to download miniconda and use a conda environment. (hasn't been tried yet)
    * Ex: `conda create --name prjxray-env python=3.5`