---
layout: page
toc: true
title: Ordering PCBs
slug: orderPCB
type: PCB
order: 5
---


# How to Order PCBs

The following gives some general information regarding PCB ordering for the CCL.


## Creating Output Files

### Gerber Files

These are the files that need to be send to the manufacturer. They also contain the files needed to create a board stencil. (More about stencils below)

From the PCB document, click File -> Fabrication Outputs -> Gerber X2 Files. This will allow you to create the gerber as well as the drill files at the same time. Gerber and drill files can also be created separately if needed. Once this is open, there are several settings that are ok to change. The "Format" lists the decimal precision to be outputed, with 2:6 being the most precise. This is the recommended option for boards with high density parts, such as an FPGA or an FMC connector. Increasing the precision may increase the price of the board, but that has never actually been tested.  

On the right side there are 2 tabs, "Layers To Plot" and "Drills". On both pages the files to be created are shown. All the files with relevant information for the board need to be created. This can easily be done by clicking "Plot Layers" -> "Used on". This must be done for both pages. 

The default settings also have the box checked for "Generate DRC Rules export file (.RUL)". This does not need to be sent to the manufacturer. You can create it anyways if you want. 

The following files are required for board manufacturing. The first part is the Altium extension for the file, the second is the layer the file describes. **Make sure** you zip up the NC Drill files with the Gerber files, or the mechanical board holes will not be drilled. The zip file containing all of these files is what needs to be sent to the manufacturer.

You can check that the files were generated correctly using a Gerber viewer online. jlcpcb.com is a good one.  Go to the website, click "QUOTE NOW" and upload your zipped folder of all the Gerber and Drill files using the "Add your gerber file" button.  Be sure to check that the drill holes are actually holes in the image and that any cutouts or unusual board outline shapes are cut as they should be. These files can also be opened one at a time by Altium. You should go thorugh every file to make sure that everything looks like you expect it to.

GTL - Gerber Top Layer
GTO - Gerber Top Overlay
GTS - Gerber Top Solder Mask

GP[1...4] - Gerber Plane [1...4]
G[1...2] - Gerber Signal [1...2]

GBL - Gerber Bottom Layer
GBO - Gerber Bottom Overlay
GBS - Gerber Bottom Solder Mask

GKO - Gerber Keep Out

txt - NC Drill File

### PDF Files

For documentation reasons and to easily view and share the schematics, it is needed to make into a PDF. This can be done from any file that is part of the project. Click File -> Smart PDF ... Follow the steps and a PDF file will be created. By default, a PDF of the board will also be included. This version of the board will be messy as it will try to show all layers at the same time and all of the traces. To have a nice looking board output, either output this PDF before beginning routing or export an Assembly drawing instead. From the PCB document, File -> Assembly Outputs -> Assembly Drawings.

### Bill of Materials

The bill of materials lists all of the parts, and the quantity of each one. It gets this information from the parts database, so make sure that information for any new parts has been added. See the Parts Database page for more information. To create a bill of materials click Reports -> Bill of Materials. On the right there is a tab "Columns". The columns that will be included in the file are shown on the right. You can choose whichever ones you want, but make sure that "Designator, Supplier (1 and 2 if applicable), Supplier Part Number, and Quantity" are selected.

From the "General" tab you can select the type of file to be exported. CSV or excel is recommended to be able to upload this file to digikey directly. Doing so makes ordering parts a lot easier. You will have to create a digikey account to be able to upload it, but since it is free to do so, just do it, it'll make your life easier. 

Once all the correct settings are chosen, you can click "OK" to save the settings, or "Export..." to create the bill of materials file. If it doesn't give you the option of where to save it, it will probably show up in the "Project Outputs for (projet name)". 

### Stencil Manufacture Files

We order stencils through [Osh Stencil](http://oshstencil.com). Osh Stencil provides both mylar and steel stencils. We use frameless 4 mil steel. The Shrec coordinator has an account to Osh Stencil that we use to order the stencils. Zip the following files and send them to the Shrec coordinator with instructions of where and how to order one. Stencils are needed for any board that has surface mounts parts. Unless you plan on soldering all the surface mounts parts by hand... which I would not recommend...

For a top layer stencil the following files are required.

GTP - Gerber Top Paste
GKO - Gerber Keep Out

For a bottom layer stencil use the these.

GBP - Gerber Bottom Paste
GKO - Gerber Keep Out

### Other Information

The manufacturer will also need to know the width and material of each layer. This information can be exported as a CSV file by going to layer stackup manager > file > export as CSV.

The manufacturer may also ask about what material to use for the surface finish, but most will just use a default option. [This website](https://www.epectec.com/articles/pcb-surface-finish-advantages-and-disadvantages.html) contains information about different types of surface finish. The cheapest is generally HASL(with lead) which will be good enough for most boards.

When ordering from JLCPCB, don't worry about either of these, just use the default options. 

## Ordering Process

We usually go to the Shrec coordinator to order parts, boards, and stencils with the department accounts. She will have the usernames and passwords to login.

We usually order parts from these suppliers:

### Components
  * [Digi-Key](https://www.digikey.com/)
    * For Digi-Key components, you can put all the components in a Digi-Key cart as a guest. Then go to your cart, click "Cart Share" in the list of Cart Tools on the right-hand side of the page, copy the link, and email it to the Shrec coordinator.
  * [Mouser](https://www.mouser.com/) is another company like Digikey.

### Boards and Stencils
  * [JLCPCB](https://jlcpcb.com/) (for boards < 6 layers thick)
  * [OSHPark](https://oshpark.com/) (not sure when to use this one... I never have while working here)
  * [Advanced Circuits](https://www.4pcb.com/) (for boards >= 8 layers, or for boards with complex routing patters, ex. an FPGA)

### Stencils
  * Stencils: [OSH Stencil](https://www.oshstencils.com/)
    * When ordering a board from JCLPCB, it is easiest to just order a stencil at the same time. While Advanced Circuits does offer stencils, they are expensive. A cheaper stencil from OSH stencil will get the job done.  
  
### Professional PCB Assembly

We have not actually submitted a PCB for assembly. We have, however, investigated the process. We have contact with Pat Farnell (pat@aapcb.com) from [Advanced Assembly](http://aapcb.com). To do an assembly you need the following files:

- Bill of Materials
- XYRS - X position, Y position, Rotation, Side

Be warned that quotes can take a long time to be processed. Pat tries to complete them within 24 hours. Many other assembly houses take much longer and this has been an issue in trying to do professional assembly. Professional assembly is designed for when boards need to be mass produced (high initial engineering cost, low quantity increase cost). Since we generally are only making a few of each board, this is not currently needed. 
