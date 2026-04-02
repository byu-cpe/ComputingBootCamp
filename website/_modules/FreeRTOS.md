---
layout: page
toc: true
title: FreeRTOS
slug: freertos
type: development
order: 16
---

# Overview

## What is a Real Time Operating System (RTOS)?

In general, when we talk about Operating Systems (OSs) we are talking about General Purpose Operating Systems (GPOSs). GPOSs are perfect for general user-oriented tasks (e.g., running applications with Graphical User Interfaces (GUIs)) because they prioritize completing the maximum quantity of computations while supporting multitasking (being "fair" to each individual process). This makes them more capable of handling arbitrary software (_general purpose_), but incapable of providing strong timing guarantees for real-time applications.

RTOSs, on the other hand, provide strong real-time guarantees by utilizing a priority-based processor access policy. Higher priority tasks can interrupt lower priority ones (which will resume once the higher priority task has finished), providing immediate execution to time-critical processes. RTOSs are used when there are hard time constraints to processes (e.g., aviation, robotics, machinery controllers, nuclear power plant controllers, etc). Because of the performance-criticality and reduced feature set of RTOSs, they also are generally smaller than GPOSs, making them perfect for microcontrollers and edge systems (Arduino, STM32, ESP32, etc).

## What is FreeRTOS?

[FreeRTOS](https://www.freertos.org/) is an open source RTOS maintained by Amazon Web Services (AWS). It is notable for being industry standard yet simple (the base source code is only [3 (large) files](https://www.freertos.org/Documentation/02-Kernel/06-Coding-guidelines/01-Source-code-organization#freertos-kernel-directory-structure)). Its minimal nature (even among RTOSs) lends it to easy porting to new architectures, making it one of the most widely used RTOSs available. Its permissive MIT license allows for extensive, no-strings-attached modification, including for closed-source projects. FreeRTOS is also extensively documented, and widely considered accessible for beginners in RTOS and embedded systems programming.

# Install

## Prerequisites

- If you use Windows, [install WSL](https://learn.microsoft.com/en-us/windows/wsl/install). Everything in this tutorial (and most things throughout software development) should be done within WSL.
- All users run `sudo apt update && sudo apt install build-essential unzip` from within your terminal (Windows users, remember to use WSL). This will ensure that you have the dependencies necessary for the following tutorials.

## With wget (Recommended)

1. Open a terminal window,
2. Run the following commands (version specified for consistency: in general we recommend the newest version):

```bash
# Move to the desired workspace directory
cd ~/Documents

# Download the specific FreeRTOS release zip file directly
wget https://github.com/FreeRTOS/FreeRTOS/releases/download/202411.00/FreeRTOSv202411.00.zip

# Unzip the downloaded file
unzip FreeRTOSv202411.00.zip
```

## Graphical (Web) Instructions

1. Download the 202411.00 FreeRTOS release with demos from [GitHub](https://github.com/FreeRTOS/FreeRTOS/releases) (version specified for consistency: in general we recommend the newest version). You only need the `FreeRTOSv202411.00.zip` file from the "Assets" section of the release closest to the top of the page. Some FreeRTOS Documentation will point you to [FreeRTOS-Kernel](https://github.com/FreeRTOS/FreeRTOS-Kernel) or [FreeRTOS-LTS](https://github.com/FreeRTOS/FreeRTOS-LTS). Do not use either of these versions, as these are structured differently and do not include demos. If you are using Windows, move the downloaded zip file from your default downloads folder into your WSL-shared drive (from within WSL the default Windows downloads directory can be accessed at `/mnt/c/Users/<YourUsername>/Downloads` and the file in question can be moved with `mv /mnt/c/Users/<YourUsername>/Downloads/FreeRTOSv202411.00.zip ~/Downloads`).
2. Open a terminal (`Ctrl+Alt+T` on Linux). Find where your FreeRTOS download was saved (`cd ~/Downloads` by default on Mac and Linux) and move it to a different directory (`mv FreeRTOSv202411.00.zip ~/Documents`, for example). Move into that directory (`cd ~/Documents`) and unzip the zipped FreeRTOS download (`unzip FreeRTOSv202411.00.zip`).

# Learn More

- [A Survey of Real-Time Operating Systems](https://engineering.lehigh.edu/sites/engineering.lehigh.edu/files/_DEPARTMENTS/cse/research/tech-reports/2019/LU-CSE-19-003.pdf): Sections 1-2 provide a good high-level overview of RTOSs and their scheduling methods. Sections 4-6 are dated and can be skipped.
- [FreeRTOS Beginner's Guides](https://www.freertos.org/Documentation/01-FreeRTOS-quick-start/01-Beginners-guide/00-Overview).
- [Introduction to RTOS](https://www.digikey.com/en/maker/projects/what-is-a-realtime-operating-system-rtos/28d8087f53844decafa5000d89608016) by [DigiKey](https://www.digikey.com/).

# Follow-Up Activities

## Run FreeRTOS on Emulated Hardware

Hardware emulation is simulating real-world hardware using software on a computer that does not match the target hardware. There are [various ways](https://www.freertos.org/Documentation/01-FreeRTOS-quick-start/01-Beginners-guide/03-Build-your-first-project#try-it-now-using-the-windows-or-linux-port-or-in-qemu) to run FreeRTOS on emulated hardware, however we will focus on a [native Linux approach](https://www.freertos.org/Documentation/02-Kernel/03-Supported-devices/04-Demos/03-Emulation-and-simulation/Linux/FreeRTOS-simulator-for-Linux) that should also work on Mac and within WSL. If you run into issues or have further questions, the [FreeRTOS documentation](https://www.freertos.org/Documentation/01-FreeRTOS-quick-start/01-Beginners-guide/03-Build-your-first-project) should be your first resource: it is the source of truth for this activity.

Run a demo FreeRTOS application using the following steps:

1. Download FreeRTOS as outlined [above](#install).
2. Move into the [demo directory](https://www.freertos.org/Documentation/02-Kernel/03-Supported-devices/04-Demos/03-Emulation-and-simulation/Linux/FreeRTOS-simulator-for-Linux#source-code-organization) (`cd FreeRTOSv202411.00/FreeRTOS/Demo/Posix_GCC`). We will be using the "Kernel only" demo, which requires less setup.
3. Run `make CFLAGS+="-DUSER_DEMO=BLINKY_DEMO"` to compile the binary with the Blinky Kernel-only demo selected (the `CFLAGS+="-DUSER_DEMO=BLINKY_DEMO"` flag acts like a `#define` to the compiler, setting the selected demo to `BLINKY_DEMO`), then `cd build` to move into the created `/build` directory.
4. Run `./posix_demo`. You should see output similar to the following:

  ```
  Trace started.
  The trace will be dumped to disk if a call to configASSERT() fails.
  Starting echo blinky demo
  Message received from task
  Message received from task
  Message received from task
  Message received from task
  Message received from task
  Message received from task
  Message received from task
  Message received from task
  Message received from task
  Message received from software timer
  ```

  This will continue until you send an interrupt signal (`Ctrl+C`). A Task/Thread (which are used interchangeably within the FreeRTOS community, even though they are not interchangeable elsewhere) sends a 100 through a queue every 200 milliseconds, while a software timer sends a 200 through the same queue every 2000 milliseconds. A separate task repeatedly drains the queue, printing out "Message received from task" for every 100, and "Message received from software timer" for every 200. (See [FreeRTOS Blinky Demo notes](https://www.freertos.org/Documentation/02-Kernel/03-Supported-devices/04-Demos/03-Emulation-and-simulation/Linux/FreeRTOS-simulator-for-Linux#the-posixlinux-simulator-demos))

## Become Familiar with the FreeRTOS Source Code

> The links below point to the newest version of the FreeRTOS kernel, which is not necessarily the same as the version we used for the simulator above.

- Skim through the [FreeRTOS-Kernel code](https://github.com/FreeRTOS/FreeRTOS-Kernel), focusing on [list.c](https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/list.c), [queue.c](https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/queue.c), and [tasks.c](https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/tasks.c), which are the 3 minimal files required for all FreeRTOS projects. Try to get a sense of the architecture and how the different sections interact. Note the frequent code comments and read through some of them.
- In [tasks.c](https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/tasks.c) find the `tskTaskControlBlock` struct. Look through it and try to understand how tasks are stored and what kinds of attributes they have. Look up anything you don't understand. After you have legitimately worked to understand it, you may even ask a Large Language Model to explain the code and how it fits into the larger project to you (then double check that the code matches the explanation). Note that every task will have a related instantiation of this struct.
