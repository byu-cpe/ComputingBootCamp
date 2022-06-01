---
layout: page
toc: true
title: Parts Database
slug: partsDatabase
type: PCB
order: 2
---


# Parts Database

******************************************************************************************************************************************************************************
# **SUPER IMPORTANT NOTE:**

Database parts are like global variables. **DO NOT modify a part in the Database!** This includes changes to the schematic symbol, footprint, Database part number, and anything else in the Database. Changes you make will most likely break things in other designs.

******************************************************************************************************************************************************************************

When adding parts to the Database, don't worry if similar parts do not have CCL part numbers near each other. You can search for any part by component value (or anything else, but usually the value is what we are most insterested in, at least for resistors and capacitors) in the search box in the Components panel in Altium.

## How to use the Database

The Parts Database is in the Altium_PCB GitHub repository. Once you have cloned the repository:
  - Go to the Components panel in Altium (on the right side).
  - Click on the menu icon (three horizontal lines to the right of the list of components that are currently available to use).
  - Click "File-based Libraries Preferences." This will open a new window.
  - In the new window, click "Install..."
  - Navigate to the Database. You will find it in the Altium_PCB GitHub repository in PartsDatabase -> Database. The file type is "Altium Library Database file." You may have to change the default extension to  .Dblib in order to see the Database. Choose the file by double-clicking it or by highlighting it and clicking "Open." This will add the Database to the Installed Libraries list. The Activated check box next to it should be checked.
  - Note: Altium may give you an error if you do not have a 64-bit access database engine installed. See "Other things to know about the database" below.
  - Click "Close." The folders in the Database will now appear in the list of components to choose from in the Components panel. You can select a folder, search for a part, and drag it onto your schematic.

## How to add parts to the Database

To add a part to the Database, you will need the part's specifications (usually available on [Digi-Key](https://www.digikey.com), schematic symbol, and footprint. You will also need to make sure that you have access to the Database.

One way to get the schematic symbol and footprint of a part affter you have found one on Digi-Key is to search for the part in Altium under the Manufacturer Part Search panel. You can typically download the schematic symbol and footprint directly from there. Then, do the following to add that new part to the database:

  - Open the Microsoft Access file.  It is found in the Altium_PCB GitHub repository. Altium_PCB -> PartsDatabase -> Database -> Altium_Database (If there are two files named Altium_Database, click on the larger one, not the 1kB one)
  - Double-click on the sheet for the type of part you are adding on the left side of the Access file.
  - Fill in each blank space with the appropriate information.
    - **Part Number** should follow the CCL naming scheme: CCL-(TYPE)-(# of that type). Ex. CCL-CAP-000005 (CAP = Capacitor). The following are the categories with their associated naming patterns (The Xs represent numbers, to be incremented for each new part):
        * Capacitor: CCL-CAP-XXXXXX
        * Clock: CCL-CLK-XXXXXX
        * Connector: CCL-CONN-XXXXXX
        * Diode: CCL-DIODE-XXXXXX
        * Ferrite: CCL-FERR-XXXXXX
        * FPGA: CCL-FPGA-XXXXXX
        * IC: CCL-IC-XXXXXX
        * Inductor: CCL-IND-XXXXXX
        * Miscellaneous: CCL-MISC-XXXXXX
        * Relay: CCL-RELAY-XXXXXX
        * Resistor: CCL-RES-XXXXXX
        * Sensor: CCL-SENSR-XXXXXX
        * Switch: CCL-SWTCH-XXXXXX
        * Testpoint: CCL-TSTPT-XXXXXX
        * Transistor: CCL-TRANS-XXXXXX
    - The most important boxes to be filled out are **Library Ref** and **Footprint Ref**. To find the Library Ref, open the schematic symbol library in Altium, go to properties, and copy the Design Item ID into Library Ref in Access. To find the Footprint Ref, open the footprint library file in Altium. On the left there should be a box labeled Footprints. Double-click on the name. This will open a box that will allow you to edit the name of the footprint. Copy and paste this name into Footprint Ref in Access.
    - **Footprint Library** is the name of the library where the footprint is saved and **Schematic Library** is the name of the library where the schematic symbol is saved. For the Database to work properly, each Footprint Library and each Schematic Library must contain only one part.
    - **Value** is normally filled with the strength of the part and its unit. Ex. 1kΩ. If the part does not have a value, you can enter the manufacturer part number into that box. See the final step below to learn how to link this field to the schematic symbol.
    - If the part is on Digi-Key, then **Manufacturer**, **Manufacturer Part Number**, **Cost**, and **Description** come directly from the Digi-Key webpage. The rest of the boxes in Access can be filled out using the device specifications. More information is always better, but it is not essential that all of these remaining boxes be full.
  - Once you are finished place the part's schematic symbol and footprint into their respective files in the Altium_PCB GitHub repository in the Database Footprints and Symbols folders according to the part's type.
  - To ensure that everything is properly linked together, open up a schematic in Altium and attempt to place a part that you just added through the Database. In the Components panel, double check that the schematic symbol image and footprint image are present under Models. If the footprint is not there, follow these steps:
    - Make sure you have saved the Database in Access.
    - Try closing and reopening Altium. Sometimes this will update the links.
    - Double check that the Library Ref and Footprint Ref are correct. These are the fields that make the links.
    - If the models still don't show up, ask for help! They are necessary to complete the design.
  - It is also good to check that all information entered in Access is showing.
  - One final step is to open the schematic symbol and make sure that the Designator and Comment boxes are properly filled. These can be found in the properties tab. In the Comment box, type "=value" to fill the box with whatever is under Value in the Access database. In the Designator box, type a letter followed by a question mark. Ex. "R?". The letter depends on the type of part. If you are unsure of the letter designator for the part that you are working with, you can check another part of the same type.
  - While adding parts it is important to not renumber any of the existing parts. This will affect all parts that have already been placed on a schematic. Is it better to always add parts to the bottom of the list in the database, even if may seem out of order to do so. 

## How to create an Altium Database

All of the CCL parts go in the same Database, so you shouldn't need to do this, but here are some guidelines in case you ever do

  - Create a Microsoft Access File with desired headings (The **Library Ref** and **Footprint Ref** headings are used by default to link the schematic symbol and footprint together, respectively. Be sure to include those headings unless you have changed the default settings. Each part you put in the Database will need a unique identifier, which we will call a part number, so be sure to include a **Part Number** heading as well.)
  - Create a .DbLib file in Altium by going to File -> New -> Library -> Database Library
  - Specify the path in the .DbLib file to map to your Microsoft Access file
  - Install the 64-bit Microsoft Access Engine if needed (instructions for this are found in the "Other things to know about the Database" section of this article below)
  - Click "Connect" in the .DbLib file
  - Make sure Field Settings are both set to Part Number (as long as all part numbers in the Microsoft Access file are unique)
  - Specify the fields to be connected to schematic symbols and footprints by writing [Library Ref] and [Footprint Ref] in their respective Design Parameter fields in the Field Mappings tab, to link these identifiers to the Library Ref and Footprint Ref in the Microsoft Access file
  - Click on "Options" in Field Settings, then "Symbol & Model Search Paths", then search for Library Search Paths, browse to the locations of your schematic symbols and footprints, and "Add" them
  - That's it! Don't forget to follow the instructions in the "How to use the Database" section of this article above

## Other things to know about the Database

To use an Access database, you may need to download and install a 64-bit Access Database Engine. Only worry about this if Altium gives you an error while trying to open the libraries. Altium also will give you a link to download the right software. (If not [here it is](https://www.microsoft.com/en-us/download/details.aspx?id=54920). Once it is installed, the libraries should work normally.

When the database is updated after parts have already been placed, an update of the parts is needed. This is done in the schematic sheet, tools -> update parameters from database. Then it will also be necessary to import changes from schematic sheets for the PCB file.

Merging the Database with old Altium files: The boards and parts for all CCL PCBs were added to GitHub on April 15, 2020. Before this, the version control software was SVN. With SVN, parts were added to boards by dragging the schematic symbol and footprint into the Altium project and then placing it on the board. When everything was moved to GitHub, the relative locations of the boards and parts changed, so Altium no longer knows how to find the symbols and footprints for parts in these projects. When you open a project in this state, you will get notification popups about libraries that cannot be found. If you click "OK" on all of these errors, the project will still open and you will still be able to navigate the schematic and layout. If you click on a schematic symbol or a footprint in this state, the name of the library will show up in the Source box in the Properties tab, but you will need to look through the "Old Library" folder to find the schematic symbol or footprint library. Once the project is saved and pushed to GitHub in this new state, it will no longer look for the libraries when it is opened, so the errors will go away. Since the transition to GitHub was made, schematic symbols and footprints should be placed in the PartsDatabase. All new schematic symbols and footprints are found through the database process described above. A project can include both Old Library parts and Database parts, so you can add parts from the Database to old schematic and PCB files. If you wish to add an Old Library part to a schematic, add it to the Database first and use it from there.
