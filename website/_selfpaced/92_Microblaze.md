---
layout: page
toc: true
title: "Microblaze Soft Processor"
slug: microblaze
type: fpga_commercial
order: 7
---

## Lecture Videos
On June 21, 2021 we had a Vivado Vitis Tutorial by Prof Goeders. The video is embedded below:

<iframe width="800" height="600" src="https://www.youtube.com/embed/suO89IG7Mho"> </iframe> 

## Create Vitis Projects

Run Vitis (`vitis`), and choose a workspace location. I used _lab_vitis/sw_ for my workspace location.


## Run Your Applicaton on the Board
*  Right-click on your executable folder (down one level from the *_system* project created in the last step -- see image below), choose *Run As->Launch on Hardware (Single Application Debug*.  
<img src = "{% link media/vitis/run_program.png %}" width="800">


* You should see the message *Hello World*.

