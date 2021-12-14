---
layout: page
toc: true
title: JTAG
slug: JTAG
type: hardware
order: 1
---


# JTAG


In an effort to create a standardized way to access the internals of increasingly small circuits for testing and manufacturing, the Joint Test Action Group created the industry standard *JTAG*. This standard became official in 1990. Testing PCB's from the outside was becoming infeasible, and so JTAG provides a standardized way to see what is going on in a circuit without having to use big traditional electronic tools.


Some Vocabulary:
*JTAG* is the interface
*Boundary Scan* is the test tech where cells are placed on I/O pins
*1149.1* is the standard

“The IEEE standard defines the Test Access Port (TAP), a sequential state machine called the TAP controller that’s implemented in the IC, the Instruction Register, and a number of Data Registers.” See more [here](https://www.jtag.com/ieee-1149-1/)

<img src="{% link media/JTAG_PIC.png %}">

TAP (Test access port) includes the following:

TDI (Test Data In)
TDO (Test Data Out)
TCK (Test Clock)
TMS (Test Mode Select)
TRST (Test Reset) optional.

Here is a really helpful animation to understand the state machine, the registers, and the modes.

<video width="800" controls>
    <source src="{% link media/jtag_shift_ir_animation_817.mp4 %}" type="video/mp4">
</video>

You can chain several JTAG devices together by their JTAG ports.

We use JTAG in Dr. Wirthlin's lab to effectively read status registers and configure, among other things.

Helpful links:
 * [Overview](https://www.jtag.com/ieee-1149-1/)
 * [State Machine and Pictures](https://www.xjtag.com/about-jtag/jtag-a-technical-overview/) (SM and JTAG pics)
 * [High level guide](https://www.xjtag.com/about-jtag/jtag-high-level-guide/)
<!-- [Animation Video and Router Hack](https://blog.senr.io/blog/jtag-explained) -->
 * [JTAG Tutorial](https://www.youtube.com/watch?v=PhaqHKyAvR4)
