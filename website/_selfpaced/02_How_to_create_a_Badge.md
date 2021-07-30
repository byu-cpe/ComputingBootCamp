# How to create a Badge

Badges are one of the core elements of the BYU Computing Boot Camp. They motivate those who use our site to put their newly-learned skills to the test by attempting a 
pass-off assessment, and acts as evidence of their knowledge after being earned. The badges we issue are OpenBadges, which contain json metadata with the cerification 
and qualification information so that it can be verified as real and assert the recepient knowledge. We are currently using Badgr to 
issue these badges with their easy-to-use API. The users can then download the badges directly onto their computers as png files (with the aformentioned metadata), 
and/or store it in the Badgr wallet. 

<img src="../media/badgeDocumentation/BadgrPage.png" alt="BYU Computing Boot Camp Badgr Page" width="600"/>

This guide will explain how to create a badge for new modules and sub-modules on the site, as well as giving access to all currently-existent badges. Be sure to read all of the sections, as the "Existing Badges" sections gives alot of context for creating new ones, and might just contain the badge you wanted to make.

## Existing Badges
The BYU Computing Boot Camp already has tons of badge designs that are ready for use. They can be found at the following link, as pngs and as their Adobe Illustrator 
Project Files: [TO DO] . The png files are ready to be uploaded to Badgr, and the Adobe Illustrator files can be used to edit/create badges. 

There is a badge created for almost every module and sub-module currently on the site as of July 2021. For example, the module "Software Development" has it's own Module Badge that looks like this:

<img src="../media/badgeDocumentation/ModuleBadges-01.png" alt="Software Development Module Badge" width="250"/>

Each of the modules on the site have their own Module badge. 

Most of the sub-modules have their own Mini-badges. For example, the sub-module "Git" under the module "Software Development" has it's own Mini-badge that looks like this:

<img src="../media/badgeDocumentation/SoftwareDevelopmentMiniBadges-01.png" alt="Git Mini-Badge" width="250"/>

Almost all of the sub-modules have their own Mini-badge. A few don't have a Mini-badge because they represent too little knowledge to justify
a reward (like "Install Vivado/Vitis"), or they are a duplicate of another sub-module (like "Github" under "PCB", which covers the same knowledge as "GitHub" under
Software Development").

#### Mini-Badges
Mini-Badges are the easiest badges to earn, and represent the smallest amount of knowledge. For example, to earn the "Make" Mini-badge, one must write two Makefiles that
implement functionality taught in the Make sub-module. This means that the Make Mini-badge will represent experience writing functional Makefiles, but not much else. For
this reason, the badge designs are simple yet elegeant. They clearly state the skill that was learned near the top, and state at the bottom that the recepient has a
"knowledge" of the skill. It is not an "expertise", due to the limited amount of code that they have to implement. The Mini-badges also have three logos on them, the Computing
Boot Camp logo on the left (cbc), a logo for Electrical and Computer Engineering on the right (ECE), and the BYU seal in the middle. These logos add legitimacy to the badge, 
represent who issued it, and add to the asthetic appeal of the Mini-badge.

Mini-Badges are color-coded, with the color on the ribbon representing which Module they fall under. The colors are taken from the 4 main colors found on the website 
banner, with the badges using the exact color on the banner, or a slight variation of the color on the banner. 

"Software Development" Mini-badges are light blue, which is a variation of the blue on the website banner.

<img src="../media/badgeDocumentation/SoftwareDevelopmentMiniBadgesAllTogether.png" alt="Git Mini-Badge" width="500"/>

"Commercial FPGA" Mini-badges are pink, which is taken off of the website banner.

<img src="../media/badgeDocumentation/CommercialFPGAMiniBadgesAllTogether.png" alt="Git Mini-Badge" width="500"/>

"Open FPGA CAD" Mini-badges are red, which is taken off of the website banner.

<img src="../media/badgeDocumentation/OpenFPGACADMiniBadgesAllTogether.png" alt="Git Mini-Badge" width="500"/>

"Robotics" doesn't have any sub-modules yet, and so doesn't have any Mini-badges. When they are made, they should have a unique color based off of the colors in
the website banner.

"Networking" Mini-badges are orange, which is taken off of the website banner.

<img src="../media/badgeDocumentation/NetworkingMiniBadgesAllTogether.png" alt="Git Mini-Badge" width="325"/>

"PCB" Mini-badges are blue, which is taken off of the website banner.

<img src="../media/badgeDocumentation/PCBMiniBadgesAllTogether.png" alt="Git Mini-Badge" width="500"/>

When creating a new Mini-badge under an existing module, be sure to make sure the color of the ribbon matches the color of the other Mini-badges under the same module.

#### Module Badges
Module Badges are the hardest to earn, and represent the largest amount of knowledge. This is due to the fact that to earn the Module Badge, one must earn all of the
Mini-badges in all of the sub-modules for that modules. For example, if the user wants to earn the "Software Development" Module Badge, they must earn 14 Mini-badges, 
from "Git" all the way to "Matlab". This means that the Softwawre Development Module Badge will represent experience in all sorts of different software concepts, which
will make it alot more valuable. The idea is that the Mini-badges will help the user be motivated to keep learning and to keep track of their progress, while the
Module badges are what will actually be shared with employeers and educational institutitions as a certification of their skill. Both types of badges could be used
for both purposes, but they will generally fulfill the previously specified roles better.

Here are all six of the Module Badges:

<img src="../media/badgeDocumentation/ModuleBadgesTogether.png" alt="Git Mini-Badge" width="600"/>


#### Computing Boot Camp Badge (idea, not currently implemented)
I have been considering having one badge that represents a knowledge in ALL of the modules taught on the Computing Boot Camp site. This badge would be earned by earning all six
of the Module Badges (or a badge for every Module on the site), and would represent skill in every single topic covered on the site. This would be the ultimate show of learning
in Electrical and Computer Engineering, so instead of saying "Electrical and Computer Engineering Knowledge", it could say "Electrical and Computer Engineering Expertise", or something similar.

We don't currently have a design for this badge. It could be a modified version of the Module Badges, or one we haven't used yet. For this reason, I'm leaving all of my unused
badge design concepts with the rest of the badges in a folder called "Unused". If you want to try and create the Computing Boot Camp Badge, you could try to adapt one of those
designs if you'd like.

## Creating a new Badge
To create a new badge, you are going to need access to Adobe Illustrator, a vector graphics editor and design program, since that's what I used to create the badges. Adobe Illustrator comes as part of the Adobe Creative Cloud, which is free for full-time employees of BYU, and available at a discount to BYU Students for $69 a year (instead of $624 a year). See the following link for information: https://adobe.byu.edu/. You could also just buy Adobe Illustrator for $252 a year, but I wouldn't reccomend it, since you can get ALL of the programs at a lower price.

The process for creating new badges will vary based on the type of badge you are creating.

#### Creating a Mini-Badge in a pre-existing Module
For a new Mini-Badge in a pre-existing module, all you have to do is locate the design files for the previously designed Mini-badges in that module, and then just copy those designs with the name of the new sub-module. First, go to <TO DO>. Here, you'll be able to see .ai files, which is the file format that Adobe Illustrator uses for storing design information. You should see the following files:
  
- CommercialFPGAMiniBadges.ai
- NetworkingMiniBadges.ai
- OpenFPGACADMinibadges.ai
- PCBMiniBadges.ai
- SoftwareDevelopmentMiniBadges.ai

Note that if you want to make a Mini-Badge in the Robotics Module, there haven't been any Mini-Badges created for it, so for all intensive purposes, it's like it's a new module. See the section "Creating a Mini-Badge in a new Module" for more information.
  
Click on the .ai file with the name of the Module you want to create a Mini-Badge for. This should open up Adobe Illustrator (assuming you have access to it). You should see a page like this (note that in this example, I clicked on the CommercialFPGAMiniBadges.ai file):
  

<img src="../media/badgeDocumentation/AdobeEx1.png" alt="Git Mini-Badge" width="900"/>

This is the standard view for editing Illustrator files. You can see each of the previously made Mini-badges are surrounded by white squares. These squares are called ArtBoards, 
and they make it easy to export all of the badges as seperate images. All you need to know is that when you make a new badge, you want it to have an Artboard behind it. So, let's do that. On the left bar, click on the following symbol, which is the Artboard Tool:
  
<img src="../media/badgeDocumentation/AdobeEx2.png" alt="Git Mini-Badge" width="400"/>
  
The screen should then change to look like this:

<img src="../media/badgeDocumentation/AdobeEx3.png" alt="Git Mini-Badge" width="900"/>
  
Now you should see labels for all of the Artboards on the screen. Left-click on the last Artboard, and you should see it light up with a blue outline, like Artboard 06 in this example:
  
<img src="../media/badgeDocumentation/AdobeEx4.png" alt="Git Mini-Badge" width="900"/>
  
Now, hit Ctrl-C, and then hit Ctrl-V. This will copy both the Artboard, and the badge inside it, making a new Artboard for the new Mini-badge:
  
<img src="../media/badgeDocumentation/AdobeEx5.png" alt="Git Mini-Badge" width="900"/>
 
If you want to reposition it, you can left click and drag on the new artboard to move it to a new position. You can use the bars on the bottom and right sides of the view to change your preview of the badges as well. I moved my badge down and to the left, so that I could have three badges on each row:
  
<img src="../media/badgeDocumentation/AdobeEx6.png" alt="Git Mini-Badge" width="900"/>
  
Now, you can start editing the badge to make it unique. The only thing you'll need to change is the text on the upper-rim of the badge, since the color of the ribbon will stay the same. Click on the Type Tool on the Left Bar, so that you can edit the text on your new Mini-badge:
  
<img src="../media/badgeDocumentation/AdobeEx7.png" alt="Git Mini-Badge" width="500"/>
  
Hover over the text on the top of the badge. It should turn blue, like this:
  
<img src="../media/badgeDocumentation/AdobeEx8.png" alt="Git Mini-Badge" width="900"/>
  
Now, left-click on it. A cursor should appear on the text:
  
<img src="../media/badgeDocumentation/AdobeEx9.png" alt="Git Mini-Badge" width="900"/>
  
Change the text to match the subject or skill of the sub-module that the badge will be for. In my example, let's assume that this badge was for a new sub-module called "Debugging", so I'll change the text to say "DEBUGGING" (Notice that it should be in all caps, to match the other badges):
  
<img src="../media/badgeDocumentation/AdobeEx10.png" alt="Git Mini-Badge" width="900"/>
  
You can now see that the text isn't perfectly centered in the badge anymore. Let's fix this. Click on the Selection Tool:
  
<img src="../media/badgeDocumentation/AdobeEx11.png" alt="Git Mini-Badge" width="500"/>
  
This tool will allow us to rotate the text back into a centered position. You should now see a box around the middle of the badge. This box represents the text object. Put your cursor close to one of the four corners of the box, and then left-click and drag to edit the rotation of the text. Let go when you think it's centered. Repeat this process until you've successfully centered the text on the badge. To make it easier to see, you can also hold down Ctrl and Alt, and then use the mouse wheel to zoom in or out.
 
<img src="../media/badgeDocumentation/AdobeEx12.png" alt="Git Mini-Badge" width="900"/>
  
Note that if the box goes away for any reason, you can make it come back by left-clicking on the text.
  
Now your badge is made! All you need to do is export it as a png file. Click on "File" at the top of the screen, then "Export", and then "Export as...":
  
<img src="../media/badgeDocumentation/AdobeEx13.png" alt="Git Mini-Badge" width="900"/>
  
You should see a window like this pop-up:
  
<img src="../media/badgeDocumentation/AdobeEx14.png" alt="Git Mini-Badge" width="700"/>
  
Now, just check the "Use Artboards" box and hit "Export":
  
<img src="../media/badgeDocumentation/AdobeEx15.png" alt="Git Mini-Badge" width="700"/>
  
Congradulations! Your new badge should now be in the same folder as all of the other badges in the sub-module. Be sure to upload it to <TO DO>
  
Now, all that's left is to upload it to Badgr so that it can be awarded to the site's users. See the section "Uploading a Badge to Badgr" below for more information.
  
#### Uploading a Badge to Badgr
  


