---
layout: page
toc: true
title: Make (and Makefiles)
slug: make
type: development
order: 4
---

## Overview

[make](https://www.gnu.org/software/make/manual/make.html) is a powerful tool that helps you organize and issue collections of shell commands.  It is commonly used to:
  * Determine which parts of a program need to be compiled, and issue shell commands to compile these programs.  While C/C++ is the most commonly compiled language, *make* can be used to compile any language that uses a command-line interface for compiling.
  * More broadly, *make* can be used for any task where files are created or modified via shell commands and need to be updated when other files change.
  * Even more broadly, *make* is often used as a shorthand for issuing multiple shell commands in a single statement.

## Installation

From a Linux terminal, run:

```
sudo apt install make
```

<details>
  <summary> Wondering what this does? </summary>
  <ul>
    <li><em>sudo</em> - This command elevates the privileges of the next command to superuser level, allowing you to install <em>make</em> system-wide.</li>
    <li><em>apt</em> - This command runs the command-line interface of the APT (advanced package tool), which handles the installation of <em>make</em>.</li>
    <li><em>install</em> - This is an <em>apt</em>-specific command that installs the packages named as inputs.</li>
    <li><em>make</em> - The name of the package to install.</li>
  </ul>
</details>

## Lecture Video
On May 5, 2021, we had a Make Tutorial by Prof Goeders. The video is embedded below:

<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/4ITu7eJBdDY"> </iframe>

### Timestamps

[0:00](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=0s) Introduction to Make<br>
[1:01](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=61s) Creating a recipe<br>
[2:54](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=174s) Running makefiles and recipes<br>
[4:09](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=249s) Common uses of Make<br>
[5:15](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=315s) Using Make to create other files<br>
[8:20](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=500s) A simple C program<br>
[9:28](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=568s) Compiling C with Make<br>
[10:25](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=625s) Adding dependencies<br>
[12:35](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=755s) make clean<br>
[12:53](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=773s) Importance of recipe names<br>
[15:01](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=901s) Adding variables<br>
[16:40](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=1000s) Chaining recipes<br>
[24:47](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=1487s) Importance of recipe order<br>
[25:17](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=1517s) Comments on suppressing output<br>
[25:50](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=1550s) Comments on calling other makefiles<br>
[26:28](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=1588s) Built-in variables<br>
[30:06](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=1806s) Simplifying through pattern matching<br>
[32:01](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=1921s) Demonstration of verbose option<br>
[34:35](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=2075s) Making your makefiles more generic and reusable<br>
[40:54](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=2454s) Creating overridable variables<br>
[43:55](https://www.youtube.com/watch?v=4ITu7eJBdDY&t=2635s) Creating a default, catch-all rule

## Example

The lecture video presents a simple C program that implements an interactive calculator and then discusses how to use *make* to compile it.  The lecture walks through how a Makefile works, starting with a very simple example and building up to a more complex generic makefile.  

<!-- The code is the split calculator code from the compiler lecture, so it makes sense to position this lecture after that one. -->

The files used in the lecture video can be found here: <https://github.com/byu-cpe/ComputingBootCamp/tree/main/make>

The lectures starts by creating a very simple *Makefile*, which is copied from `makefiles/mk1`.  It then walks through the steps of modifying this *Makefile* to the one in `makefiles/mk2`, then `makefiles/mk3`, and so on.  

<!-- Last time I showed them mk6 first, and showed how cryptic it was, and then talked about how we will walk through the steps to understanding this. -->

The various stages of makefile development shown in the lecture are (time stamps in parentheses):
* mk1 ([10:13](https://www.youtube.com/embed/4ITu7eJBdDY?start=613)): The simplest makefile where we discuss makefile "recipes" (targets).  Build and clean only.
{% include quizzes.html id=12 %}
* mk2 ([15:01](https://www.youtube.com/embed/4ITu7eJBdDY?start=901)): Variables
* mk3 ([16:36](https://www.youtube.com/embed/4ITu7eJBdDY?start=996)): We split up the compilation/linker steps, and introduce chained dependencies.  We do a bunch of demos of deleting files and rebuilding targets.  The linux 'touch' command is very helpful here.
* mk4 ([26:28](https://www.youtube.com/embed/4ITu7eJBdDY?start=1588)): We introduce Makefile automatic variables ($@ and $<)
{% include quizzes.html id=11 %}
* mk5 ([30:06](https://www.youtube.com/embed/4ITu7eJBdDY?start=1806)): Pattern matching
* mk6 ([34:35](https://www.youtube.com/embed/4ITu7eJBdDY?start=2075)): Makefile functions, and making the makefile more generic.
{% include quizzes.html id=13 %}

## Conclusion

*make* is a powerful tool for collecting the shell commands used for compilation into a single file. With a bit of knowledge, you can make Makefiles that are generic enough to be reused again and again. It simplifies compilation by reducing it to a single, memorable command, and it allows you to automate the repetitive parts of the compilation process.

## Activities

* Check if a project you're working on uses a Makefile to compile. Open up the Makefile, and try to understand what it is doing. A lot of C/C++ projects will use Makefiles automatically generated by CMake, so they may be a bit hard to understand, but definitely take a look!

* Write a short C program of your own, and write a Makefile to compile it.

* Checkout the Makefiles Dr. Goeders used, and experiment with changing things and seeing what happens.

## Certify Your Skills
<a href="https://badgr.com/public/badges/opPKYN_pQFi6UWl1Q_aT5Q"><img src="https://media.badgr.com/uploads/badges/8e853a0b-726b-4101-8cb0-4b299926f19d.png" alt="Make Badge" width="250"/></a>

For those who believe they have mastered Make and Makefiles, we present the Make badge! This badge can be viewed in its entirety on Badgr.com here: [Make Badge](https://badgr.com/public/badges/opPKYN_pQFi6UWl1Q_aT5Q). The Make badge can be used to prove your Makefile knowledge to potential employers, educational institutions, or anyone else! To earn it, you'll have to complete the Make test and use your knowledge to write Makefiles for varying situations. Attempt the Make test and earn the Make badge with the button below!

<div class="collapsible" onclick="location.href='https://github.com/BYUComputingBootCampTests/makeTest'">
    <p class="activity-label h3-clone">EARN THE MAKE BADGE</p>
    <p class="dropdown-arrow h3-clone">&#9654;</p>
</div>

Good luck to those who attempt the test, and if you pass, congratulations! You are now certified in Make and Makefiles by the BYU Computing Boot Camp.

## Additional Resources
* <https://www.gnu.org/software/make/>
* Recursive make considered harmful: <https://accu.org/journals/overload/14/71/miller_2004/>
