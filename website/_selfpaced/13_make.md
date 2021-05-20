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
  * Even more boardly, *make* is often used as a shorthand for issuing multiple shell commands in a single statement.

## Install

```
sudo apt install make
```

## Lecture Video
On May 5, 2021 we had a Make Tutorial by Prof Goeders. The video is embedded below

<iframe width="800" height="600" src="https://www.youtube.com/embed/4ITu7eJBdDY"> </iframe> 

## Example

The lecture video presents a simple C program that implements and interactive calculator, and then discusses how to use *make* to compile it.  The lecture walks through how a Makefile works, starting with a very simple example, and building up to a more complex, generic makefile.  

<!-- The code is the split calculator code from the compiler lecture, so it makes sense to position this lecture after that one. -->

The files used in the lecture video can be found here: <https://github.com/byu-cpe/ComputingBootCamp/tree/main/make>

The lectures starts by creating a very simple *Makefile*, which is copied from `makefiles/mk1`.  It then walks through the steps of modifying this *Makefile* to the one in `makefiles/mk2`, then `makefiles/mk3`, and so on.  

<!-- Last time I showed them mk6 first, and showed how cryptic it was, and then talked about how we will walk through the steps to understanding this. -->

The various stages of makefile development shown in the lecture are:
* mk1: The simplest makefile where we discuss makefile "recipes" (targets).  Build and clean only.
* mk2: Variables
* mk3: We split up the compilation/linker steps, and introduce chained dependencies.  We do a bunch of demos of deleting files and rebuilding targets.  The linux 'touch' command is very helpful here.
* mk4: We introduce Makefile automatic variables ($@ and $<)   
* mk5: Pattern matching
* mk6: Makefile functions, and making the makefile more generic.

## Other Resources
* <https://www.gnu.org/software/make/>
* Recursive make considered harmful: <https://accu.org/journals/overload/14/71/miller_2004/>
