---
layout: page
toc: true
title: RapidWright
slug: rapidwright
type: fpga_opensource
order: 1
---


These are useful steps to immediately do with your new Linux VM.
* RapidWright is written in Java. In order to use this library, we need to download the Java jdk and the Java jre. The following terminal command will install both on the provided Linux VM
  * ``sudo apt install openjdk-11-jre``

### Setup Capnp & RapidWright/interchange
These instructions have been tested on the following versions:<br>
Ubuntu 20.04<br>
RapidWright/interchange commit: 81366d2  <br>
CapnProto-C++: 0.9.1  <br>
CapnProto-Java commit: 2f7ce18 <br>
CapnProto-Python version: 1.1.0<br>
Java: openjdk-11-jre (it is assumed that this is installed)<br>

#### Dependencies:
* CapnProto <br>
First install CapnProto. The base installation instructions are located [here](https://capnproto.org/install.html).
They are copied below for convenience. They can be executed in the /tmp directory.

From Release Tarball:

You may download and install the release version of Cap’n Proto like so:
```
curl -O https://capnproto.org/capnproto-c++-0.9.1.tar.gz
tar zxf capnproto-c++-0.9.1.tar.gz
cd capnproto-c++-0.9.1
./configure
make -j6 check
sudo make install
```
This will install capnp, the Cap’n Proto command-line tool. It will also install libcapnp,
libcapnpc, and libkj in /usr/local/lib and headers in /usr/local/include/capnp and /usr/local/include/kj.

* CapnProto-Java <br>
Next, install the CapnProto-Java extenstion. These instructions are based on the github ci that YosysHQ uses to build interchange, found [here](https://github.com/YosysHQ/nextpnr/blob/master/.github/ci/build_interchange.sh#L16)

```
git clone https://github.com/capnproto/capnproto-java.git
pushd capnproto-java
make -j`nproc`
sudo make install
popd
```

* CapnProto-Python <br>
In your environment of choice run:
```
pip3 install pycapnp
```

#### Install RapidWright/interchange
Most of the following instructions come from the README.md for the RapidWright/interchange project located [here](https://github.com/Xilinx/RapidWright/tree/interchange/interchange).
These commands are best ran somewhere in your home directory.

* Easiest way to Setup a RapidWright Repo Locally:
```
wget http://www.rapidwright.io/docs/_downloads/rapidwright-installer.jar
java -jar rapidwright-installer.jar -t
source rapidwright.sh
cd RapidWright
```
More details here:
http://www.rapidwright.io/docs/Automatic_Install.html#automatic-install

* Finish setting up interchange
```
cd interchange && make && cd ..
make
```

RapidWright has python wrappers. In your environment run:
```
pip3 install rapidwright
```

### Additional Resources
Instructions on how to use rapidwright in python are [here](https://github.com/Xilinx/RapidWright/blob/master/python/README.md).

Symbiflow has a project for loading capnp-interchange files into python and interacting with them. This can be found [here](https://github.com/SymbiFlow/python-fpga-interchange).

RapidWright javadoc is [here](https://www.rapidwright.io/javadoc/index.html), the python functional calls should be identical to the java calls.
