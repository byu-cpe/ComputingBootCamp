---
layout: page
toc: true
title: Soldering Station
slug: solderingStation
type: PCB
order: 6
---


# PCB Assembly

Each PCB has a corresponding binder or binders containing all the necessary components. There is a metal stencil in the binder that you place on top of the PCB, aligning the holes in the stencil with each soldering pad. Use tape to ensure it stays in place. Get the soldering paste from the fridge in the break room (459E) and apply it to the stencil and spread in evenly across all the holes using the flat plastic scraper (found in the toolbox). Lift the stencil and ensure that each pad has sufficient solder paste on it. Also check that there is not paste between pads, as this will increase the chance of bridging. 

Each divider of the binder contains specific components and shows you where to place them on the board. Use tweezers to place the components and be sure not to apply much downward pressure as the solder paste can spread and possibly bridge connections. Do not place any components that go on the opposite side of the board or ones that have pins that go through holes in the board, these should be soldered on after the board is heated in the soldering oven. 

Most components need to be oriented correctly. This designation is usually shown by a dot or notch, and a matching dot on the PCB. Capacitors, if polarized, will have a line on the part and the board. Diodes usually have a triangle and a line on the board and a line on the part. Match the two lines to the same side.

A few of the boards built here have parts on the underside of the board. These parts are either small resistors or an FMC connector. They will be placed in the front of the parts binder if they are to placed first. Apply paste to this side first, place all parts and cook the board before applying paste to the reverse side. On boards with 0402 or 0603 parts, these parts are small enough that the surface tension of the solder will prevent them from falling off while being baked for the reverse side. On boards with the FMC connector, additional PCB scrap parts will have to be placed underneath the board while being baked a second time. 2-3 are usually enough to ensure that the board is lying flat. 

**WATCH THESE VIDEOS**. They give a very good idea of how using a stencil to apply solder paste works:

Basics: [Sparkfun](https://www.youtube.com/watch?v=WDIqtGMROjM)

More in depth: [EEVblog](https://www.youtube.com/watch?v=qyDRHI4YeMI)

## Solder Paste

The solder paste we use comes in syringes and can be bought from this link [here](https://www.amazon.com/Kester-EP256-Solder-Syringe-Dispenser/dp/B006UTCYM2/ref=sr_1_2?dchild=1&keywords=kester+solder+paste&qid=1585170588&sr=8-2). To maintain good viscosity, reflow, and overall performance, it should be refrigerated when not in use. Make sure to only use fresh solder paste. When you buy the paste, it will have a date of manufacture (D.O.M.) printed somewhere on the label. Typical shelf life of this kind of solder paste is about 6 months from the D.O.M, so make sure that you are using good paste.

Let the solder paste warm up before use, as this will ensure that it flows over the stencil more easily.

When you have used all the paste in a syringe or if the batch is expired, take the syringe to Joe Bussio in the ELC (CB 416), and he will safely dispose of it.

## Soldering Oven

There is a switch on the rear side of the oven to power it on. For all of our boards, we select the second temperature profile so that the plastic parts don't get too hot. The default profile is profile #1, so you need to switch it to profile #2 every time you do a board. To switch profiles, hit the F3 button, then F1 to switch to profile #2. After that, hit F4 a couple times. It has a glitch where it turns to Chinese, so keep hitting F4 until it switches back to English. Place the board in the middle of the oven so that the air vents are below all parts of the board (no part of the board should be over the non-vented metal sections). This ensures that each component solders properly to the board. Then hit F1 to start the oven.

After the process finishes, the oven will beep until you press and hold the S button. Then you can open it up and pull out the board(s). Of course, it will be hot so be careful and don't get burned. 

## Hand Soldering

Hand soldering is for through hole components (where there is a hole in the board instead of a flat pad). This is generally done after the board has been baked, as baking a board with through hole parts attached will disrupt their placement. These are most often connectors that have plastic that would melt if placed in the oven. 

If you have never hand soldered before, make sure to watch [this tutorial](https://www.youtube.com/watch?v=Qps9woUGkvI) before beginning. We use leaded solder here, which is bad for you to breathe in, so make sure to wear a N95 mask or have a fan sucking away any fumes from soldering.

There is a lot more to know about soldering, and if you are ever having difficulty getting good results, don't be afraid to look up how to improve your soldering. Here are some basic tips. Apply the solder to the opposite side of the pad from the iron. Solder flows towards heat, so this will ensure a good connection around the entire pad. Choosing the largest tip is better for good heat transfer, but you don't want a tip that is larger than the pad you are trying solder, as it could damage the board. Be careful while changing tips that you don't burn yourself. The solder iron will transfer heat better if the tip is tinned and clean. The iron on the tip will oxidize quickly if the tip is not covered in solder. Whenever you wipe off the tip in the brass or on a sponge, make sure to apply just a bit of solder to the tip before you begin soldering again. When soldering, make sure to apply the solder to the pad and not to the tip itself. This will ensure better connections as well as longer life of your tips.

# Power Cords

We use the USB 2.0 A-B cable to make the power cords for JCM boards revisions 3.1 and older. Since the newer JCMs use USB-C to power them, we have little need for these power cords at the moment. If you need one, make sure to look around the lab (they are probably in 459A) before making a new one.

Use scissors to cut off the USB B connector (the rounder one) and strip the black wire casing. The white and green wires are not needed so they can be cut as well. Strip a little bit of the red and black wires and bend them downwards. Once the wires are stripped, tin the ends of them by applying a small amount of solder to uniformly cover the exposed wire. Prepare four smaller separate wires with the casing stripped from both ends and crimp the golden socket contacts to the one of the ends of each wire. Solder the other ends to the red and black wires, 2 on each wire, and make sure all the socket connectors are facing the same direction. Bind the two soldered connections using heatshrink and a heat gun (found in the shop) and then bind everything together using a larger heatshrink and leave the four socket contacts exposed. Then insert the socket contacts into the white pin connector head. Make sure the black wire pins go into the right slots and the red wire pins go into the left slots and that they click all the way in.
