---
layout: page
toc: true
title: Make (and Makefiles)
slug: make
type: development
order: 4
---

## About Make

[make](https://www.gnu.org/software/make/manual/make.html) is a powerful tool that helps you organize and issue collections of shell commands.  It is commonly used to:
  * Determine which parts of a program need to be compiled, and issue shell commands to compile these programs.  While C/C++ is the most commonly compiled language, *make* can be used to compile any language that uses a command-line interface for compiling.
  * More broadly, *make* can be used for any task where files are created or modified via shell commands, and need to be updated when other files change.
  * Even more broadly, *make* is often used as a shorthand for issuing multiple shell commands in a single statement.

## Install

From a Linux terminal, run:

```
sudo apt install make
```

<details>
  <summary> Wondering what this does? </summary>

    <em>sudo</em> - This command elevates the privileges of the next command to an administrator level, allowing you to install <em>make</em> system-wide.  <br>
    <em>apt</em> - This command runs the command-line interface of the APT (advanced package tool), which handles the installation of <em>make</em>. <br>
    <em>install</em> - This is an <em>apt</em>-specific command that installs the packages named as inputs. <br>
    <em>make</em> - The name of the package to install. <br>

</details>

## Lecture Video
On May 5, 2021 we had a Make Tutorial by Prof Goeders. The video is embedded below

<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/4ITu7eJBdDY"> </iframe> 

## Example

The lecture video presents a simple C program that implements and interactive calculator, and then discusses how to use *make* to compile it.  The lecture walks through how a Makefile works, starting with a very simple example, and building up to a more complex, generic makefile.  

<!-- The code is the split calculator code from the compiler lecture, so it makes sense to position this lecture after that one. -->

The files used in the lecture video can be found here: <https://github.com/byu-cpe/ComputingBootCamp/tree/main/make>

The lectures starts by creating a very simple *Makefile*, which is copied from `makefiles/mk1`.  It then walks through the steps of modifying this *Makefile* to the one in `makefiles/mk2`, then `makefiles/mk3`, and so on.  

<!-- Last time I showed them mk6 first, and showed how cryptic it was, and then talked about how we will walk through the steps to understanding this. -->

The various stages of makefile development shown in the lecture are:
* mk1: The simplest makefile where we discuss makefile "recipes" (targets).  Build and clean only.
{% include quizzes.html id=7 %}
* mk2: Variables
* mk3: We split up the compilation/linker steps, and introduce chained dependencies.  We do a bunch of demos of deleting files and rebuilding targets.  The linux 'touch' command is very helpful here.
* mk4: We introduce Makefile automatic variables ($@ and $<)
{% include quizzes.html id=6 %}
* mk5: Pattern matching
* mk6: Makefile functions, and making the makefile more generic.
{% include quizzes.html id=8 %}

## Other Resources
* <https://www.gnu.org/software/make/>
* Recursive make considered harmful: <https://accu.org/journals/overload/14/71/miller_2004/>

## Make Badge
<a href="https://badgr.com/public/badges/opPKYN_pQFi6UWl1Q_aT5Q"><img src="https://media.badgr.com/uploads/badges/8e853a0b-726b-4101-8cb0-4b299926f19d.png" alt="Make Badge" width="250"/></a>

For those who believe they have mastered Make and Makefiles, we present the Make badge! This badge can be viewed in its entirety on Badgr.com here: [Make Badge](https://badgr.com/public/badges/opPKYN_pQFi6UWl1Q_aT5Q). The Make badge can be used to prove your Makefile knowledge to potential employers, educational instutitions, or anyone else! To earn it, you'll have to complete the Make test and use your knowledge to write Makefiles for varying situations. Attempt the Make test and earn the Make badge with the button below!

<div class="collapsible" onclick="location.href='https://github.com/BYUComputingBootCampTests/makeTest'">
    <p class="activity-label h3-clone">EARN THE MAKE BADGE</p>
    <p class="dropdown-arrow h3-clone">&#9654;</p>
</div>

Good luck to those who attempt the test, and if you pass, congratulations! You are now certified in Make and Makefiles by the BYU Computing Boot Camp.









