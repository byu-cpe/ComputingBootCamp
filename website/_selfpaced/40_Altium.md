---
layout: page
toc: true
title: Altium
slug: altium
type: PCB
order: 1
---


# Altium

## Setup

### Altium Account

When you first go to [download Altium](https://www.altium.com/products/downloads), you will need an Altium account. If you haven't been set up with one yet, submit a ticket to request one from the CSRs/Systems Administrators at https://eceticket.byu.edu/.

### License Manager

When you first open Altium, it will bring up the License Manager. If it doesn't automatically come up, go to the user information drop-down in the very top right, and select 'Licenses...'.

If you are logged in with a valid account, you will be able to use a seat from the available licenses. Click one of the options, then select 'Use'. You should now be able to open and edit Altium PCB files.

Be aware that there are more students that use Altium than available licenses, so make sure to close Altium when you are finished using it.

## Altium Organization

There are two main file types used when designing a PCB. There are schematic and PCB file types. You begin designing the board as a schematic, then export that data and create a PCB file  where you can then arrange all of the parts on the board.

The other file types are used when exporting the board to send the files to the PCB manufacturer.

If this is your first time using Altium or PCB design software, watch this [Altium tutorial series](https://www.youtube.com/playlist?list=PL3aaAq2OJU5H_V1wJfcxn9RtUf2hs2FU6) to learn the basics of Altium. If you think you are too cool to watch tutorial videos, you are welcome to try and figure out Altium on your own, just remember to come back here when you get stuck. 

There is a lot of information in those tutorial videos. You don't need to learn everything in one go. One idea to help learn the material is to make a practice project to use to follow the instructions in the videos.

After watching these videos, when you run into problems, or there is something that you don't know how to do, consider checking [Altium's documentation](https://www.altium.com/documentation/altium-designer).

## Design

### Schematics

Each PCB project can have multiple schematics. The software links all of the schematic pages together to make the PCB. Schematics detail how each part is connected. It is important to keep your schematics organized since they are how you will show others how your board is put together. To help with organization of our github schematic files are generally named boardName_schematicName. They do not need revision numbers. Past revisions are kept in a seperate folder named with its revision number. 

### PCB

The PCB interface is used to 'build' the board. It is where you place each part and tell the computer where copper will go to connect them. 

To create a PCB document, go to the schematic of the board. In the 'Design' dropdown on the top of the window, select 'Update PCB Document <name>'. This will either generate a new PCB document or update the existing one. Remember that any time the schematic is changed, you need to do this. The PCB document does not automatically update itself. Once the PCB file is created, this can also be done there under the 'Design' tab. 
 
More about PCB design can be found on the Layout Guidelines page.

### Libraries/Database

Libraries contain the information about each part, as well as link the schematic sybmol to the PCB footprint, or part shape. Because having a library for every part becomes messy very quickly, we use a database instead. See the Parts Database page for more information. Make sure to enter all relavant informationinto the database when adding a new part. All of the information about a part that you will use is usually listed on digikey (where we buy almost all of our parts). Digikey also usually has a link to that part's datasheet which has even more information.

### Footprints

Footprints are documents that contain the pin assignment and shape and size of every part. These need to linked to the schematic symbols through the database for each part or it will not show up when you create the PCB document. 

To add a footprint, go to the 'PCB Library' tab, then select 'Add'. This will add a new footprint that you can now edit. Double click the entry and rename the footprint. However, it is usually easier to go to an already existing footprint and make a copy. For more complex parts, sometimes the manufacturer will actually have a part footprint available on their website. There are also websites where you can download footprint and schematic symbols such as https://www.snapeda.com/ and https://www.ultralibrarian.com/. It is recommended to double check dimensions when using these websites to make sure that they match the information in the parts datasheet. 

Now you can add pads or pins to the footprint, depending on if the part is surface mount or through-hole mount, respectively. In the properties tab, you can change the pad dimensions and which layer it is on. With surface mount parts, the pads are usually on the top layer.

*Note: we usually use the rounded rectangle shape for the pads, as it the best at keeping the part aligned when the solder paste starts melting.

Next, add the top overlay lines. These are lines that will be printed in white on the PCB. They are used to indicate where the black plastic part of the package physically is in reference to the pads. For more information, see the "Altium Layers" section below. Make sure to also designate where pin 1 is located, or match whatever polarity marker the part has. 

[Altium's page](https://www.altium.com/documentation/altium-designer/creating-the-pcb-footprint-ad?version=19.0) on creating a footprint from scratch or by using their wizard.

## Altium Layers

### Footprint Layers

When designing a footprint for a component there are many layers than can be added to the design. The most important are listed below.

#### Top Layer

This is the layer where the pads of the parts need to be. This layer determines where soldering pads or holes will be placed on the board.

#### Bottom Layer

This layer is only needed for through hole parts. The soldering holes need to be the same as on the top layer to ensure that there is a hole all the way through the board. 

#### Mechanical 1

This layer outlines the area that the part will take up. It is generally drawn with a line around the edge.

#### Mechanical 13

This layer outlines the 3D extruded model of the part. It is not essential, but helps when looking at a 3D model of the board. Without this layer there is simply a blank space on the 3D model. However, a board can still be printed without this layer.

#### Mechanical 15

This layer is also known as the courtyard layer. This determines the allowed proximity between one part and another. A certain clearance is required and can be adjusted using the PCB design rules. This layer is generally drawn around the edge of the part. 

#### Top Overlay

This layer is also known as the silk screen. This layer provides a direction to the person placing the component of where to place the part. It is the only layer that will be visible once the board has been printed other than the soldering pads. It should contain a general outline of the part, but should not touch or come too close (less than 10 mils) to the pads. If it comes too close to the pads, it does not need to completely outline the part. It also should contain information of the part's orientation if that is important to the part. 

### Board Layers

When choosing how many layers and what type of layers to include on a board, here are some things to consider.

  * Layers can be edited in the Layer Stackup Manager menu which can be accessed on the PCB document by right clicking on any layer listed at the bottom of the page.
  * Look at other boards for examples of how to set up the layers. Tortoise 1 and 2 are good examples of an 8 layer board.
  * The number of layers determines where a board can be purchased. For more information see the OrderPCB page.
  * Layers must be added in pairs. Either 2 signal layers or 2 planes. In pairs of planes, there must always be one ground plane and one power plane. 
  * Types of layers must be balanced. For example, 2 planes 2 signals. 4 planes 2 signals or 2 planes 4 signals is also acceptable, while 2 planes 6 signals is not. 
  * Power and ground planes can be split, but this should not be done anywhere where high speed signals will be routed, as it will affect their integrity. 

## Miscellaneous

### Differential Pairs

In several of the boards in the lab, differential pairs are used. Routing differential pairs is very similar to routing single wires. To route a differential pair, right click the icon used to route a single wire, and select the differential pair option. The key thing to remember is that the two wires shouldn't get too far apart from each other as they are routed. The more closely matched the pair is, the more effective it is. This means route them on the same layers and the same path as much as possible.

### Length Tuning

When the signals on the board are high enough frequency, the signal traces on the PCB need to be tuned to be the same length. Otherwise, some signals get to the other end before others. To tune trace lengths select the 'Interactive Length Tuning' icon (right next to the trace routing icon). Then, click on the trace that you want to tune. As you move the mouse, it will automatically change the shape of the trace(s) to increase length. You can go to [this link](https://www.altium.com/documentation/18.0/display/ADES/((Length+Tuning))_AD) for documentation on options for changing the trace geometry.

To set the length tolerances required for a group of nets, go to the design rules and change it there.

### Altium Keyboard Shortcuts

A complete list of shortcuts can be found on [Altium's website](https://www.altium.com/documentation/altium-designer/altium-designer-shortcut-keys?version=19.0). That web page also explains how to change which keys are used for shortcuts.

