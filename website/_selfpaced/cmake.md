---
layout: page
toc: true
title: CMake
slug: cmake
type: development
order: 5
---

# Introduction

In the last module, we talked about Make. Make and Makefiles provide a nice way to break the build process (or any complex generation process) into a list of dependencies and commands that are needed to generate them easily and efficiently. Make is a very useful tool for a variety of different problems, however manually coding a Makefile for large coding projects can be very tedious, time consuming, and brutal.

However, most C++/C projects tend to follow a common structure. For example, each .c file needed for an executable or library needs to be pre-processed, compiled, and assembled into binary object files (or .o files), then combinations of these files need to be linked together. To complete compilation and assembly of dependent .c files, the compiler needs access to the .h files for any included libraries; and, to complete linking, the linker needs access to the associated object files (or .o files) for those libraries as well.

CMake is a tool and syntax that enables you to specify the dependencies and properties for various targets (such as executables and libraries). CMake will then traverse through your folder structure and automatically generate a Makefile that will build all of the targets you specified by calling all of the combinations of gcc/g++/ld/ar commands needed to compile and link your code.

## Install

The version of *cmake* that is installed via *apt* is usually quite old.  There are [many ways](https://askubuntu.com/questions/355565/how-do-i-install-the-latest-version-of-cmake-from-the-command-line) to get a newer version of *cmake*, although the easiest is to grab it from the Python package manager (*pip*) where it is kept fairly up to date:

```
sudo apt install python3-pip
sudo pip3 install --upgrade cmake
```

# Lecture Tutorial

On May 7, 2021 we had a CMake Tutorial by Prof Mangelson. The video is embedded below:

<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/4PoLuU32nqw"> </iframe> 


All of the files used in the lecture tutorial can be found at: <https://github.com/byu-cpe/ComputingBootCamp/tree/main/cmake>

A rough outline of the discussion we had is included in the notes.txt file.

Try running through the examples we talked about in lecture. 





# Followup Activities

## Learn More CMake Syntax

* Watch the following video by Jason Turner for a quick introduction: <https://www.youtube.com/watch?v=HPMvU64RUTY>
* Read through the following page for an overview of the syntax: <https://llvm.org/docs/CMakePrimer.html>

{% include quizzes.html id=114 %}

{% include quizzes.html id=115 %}

## PUBLIC, PRIVATE,  INTERFACE

The PUBLIC, PRIVATE, and INTERFACE keywords are used to specify if a dependency, directory path, or property should be applied to the current target, its dependencies, or both.

Read more about this at: <https://leimao.github.io/blog/CMake-Public-Private-Interface/>

{% include quizzes.html id=116 %}

## STATIC and SHARED

Read more about the differences between static and shared libraries: <https://www.geeksforgeeks.org/difference-between-static-and-shared-libraries/>

{% include quizzes.html id=117 %}

## Essential CMake Functions

* project - <https://cmake.org/cmake/help/latest/command/project.html>
* add_library - <https://cmake.org/cmake/help/latest/command/add_library.html>
* add_executable - <https://cmake.org/cmake/help/latest/command/add_executable.html>
* target_include_directories - <https://cmake.org/cmake/help/latest/command/target_include_directories.html>
* target_link_libraries - <https://cmake.org/cmake/help/latest/command/target_link_libraries.html>
* target_link_directories - <https://cmake.org/cmake/help/latest/command/target_link_directories.html>
* target_compile_features - <https://cmake.org/cmake/help/latest/command/target_compile_features.html>

The official documentation for all built-in cmake functions can be found at: <https://cmake.org/cmake/help/v3.20/>

{% include quizzes.html id=118 %}

## Create Your Own Example

Now that you have seen an example code structure, try creating a mini-project of your own.
Be sure to include at least a library and executable program.

Try switching the library from STATIC to SHARED and vice versa.
Maybe create an executable that uses one of each. 

Be sure to make sure you check to make sure your executable runs correctly.

* Make your example a little bit more complicated by developing a dependency chain that includes:
** exe1 (an executable that depends on and calls a function from lib1)
** lib1 (a shared library where the function called by exe1 calls a function from lib2)
** lib2 (a shared library that includes the function needed by lib1)

To do this you will need to play around with and understand the PUBLIC and PRIVATE keywords. 

* Play around with changing these libraries from SHARED to STATIC

* Play around with introducing dependencies between libraries that are or are not needed by targets further up the chain.

## Certify Your Skills
<a href="https://badgr.com/public/badges/dHgXDlBtTCa1Re-LwGo5pw"><img src="https://media.badgr.com/uploads/badges/060b773b-bd5c-48b0-82e3-68af87eabf0f.png" alt="CMake Badge" width="250"/></a>

For those who believe they have mastered CMake, we present the CMake badge! This badge can be viewed in its entirety on Badgr.com here: [CMake Badge](https://badgr.com/public/badges/dHgXDlBtTCa1Re-LwGo5pw). The CMake badge can be used to prove your CMake files knowledge to potential employers, educational institutions, or anyone else! To earn it, you'll have to complete the CMake test and use your knowledge to write CMake files for varying situations. Attempt the CMake test and earn the CMake badge with the button below!

<div class="collapsible" onclick="location.href='https://github.com/BYUComputingBootCampTests/cmakeTest'">
    <p class="activity-label h3-clone">EARN THE CMAKE BADGE</p>
    <p class="dropdown-arrow h3-clone">&#9654;</p>
</div>

Good luck to those who attempt the test, and if you pass, congratulations! You are now certified in CMake by the BYU Computing Boot Camp.

# Advanced (But Essential) Topics

## Learn about Modern CMake

Early CMake primarily worked by working with setting global variables for include trajectory lists, linked libraries, and other dependencies. This can cause many problems.

Modern CMake is targets based. Instead of directly changing variables (which was the old way to do things), instead we should deal with targets and properties. Modern CMake is the object oriented version of the older cmake methods.


You should always be using Modern CMake techniques and methods.

Read about these items at the following links:
* <https://gist.github.com/mbinna/c61dbb39bca0e4fb7d1f73b0d66a4fd1>
* <https://cliutils.gitlab.io/modern-cmake/>


## Accessing External Projects

Often you need to combine many small repositories or projects into a single large one. 

The best way to accomplish this is via FetchContent and the MakeAvailable function if possible.
Read more about this here:
* <https://cmake.org/cmake/help/latest/module/FetchContent.html>


## Exporting, and Installing

Enabling others to use your library is essential. For large projects especially, installing your files from many sub-projects to a single unified folder can be very helpful.

Exporting your targets is essential for supporting Modern CMake practices.

More information can be found at: <https://pabloariasal.github.io/2018/02/19/its-time-to-do-cmake-right/>

## Accessing System Installed Libs

There may also be situations where you need to access libraries on your local machine that have not been setup as CMake targets.

This can be done by using either find_packageFindModule file that searches for the file. To be compliant with Modern CMake that find module file needs
to create an INTERFACE target that supports access to those resources.

More information about FindModule can be found at: <https://hsf-training.github.io/hsf-training-cmake-webpage/09-findingpackages/index.html>

More information about how to write your own Modern CMake FindModule can be found at: <https://pabloariasal.github.io/2018/02/19/its-time-to-do-cmake-right/>


## Integrating Testing into CMake

We will be talking more about unit testing in a later module, however, cmake can also be used to handle unit testing.

More information can be found at the following link: <https://cliutils.gitlab.io/modern-cmake/chapters/testing.html>

## pods2

There are also many sets of cmake utilities/resources that wrap
CMake functions into groups of commonly used functions or structures
that can simplify specific projects.

One that is used and maintained by the FRoSt Lab at BYU is called pods2 and
can be accessed at:

<https://bitbucket.org/frostlab/pods2/src/master/>

This project demonstrates many of the advanced topics described in the followup activities above.

# Excellent Resources

* <https://cmake.org/>
* <https://cmake.org/cmake/help/v3.20/>
* <https://internalpointers.com/post/modern-cmake-beginner-introduction>
* <https://pabloariasal.github.io/2018/02/19/its-time-to-do-cmake-right/>
* <https://cliutils.gitlab.io/modern-cmake/>
* <https://hsf-training.github.io/hsf-training-cmake-webpage/>
* <https://gist.github.com/mbinna/c61dbb39bca0e4fb7d1f73b0d66a4fd1>