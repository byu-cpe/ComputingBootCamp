# How to create a Badge

Badges are one of the core elements of the BYU Computing Boot Camp. They motivate those who use our site to put their newly-learned skills to the test by attempting a 
pass-off assessment, and acts as evidence of their knowledge after being earned. The badges we issue are OpenBadges, which contain json metadata with the cerification 
and qualification information present, so that it can be verified as real and contain information on the knowledge the recepient has. We are currently using Badgr to 
issue these badges, using their easy-to-use API. The users can then download the badges directly onto their computers as png files (with the aformentioned metadata), 
and/or store it in the Badgr wallet. 

This guide will explain how to create a badge for new modules and sub-modules on the site, as well as giving access to all currently-existent badges just in case the
badge you want to create has already been made. Be sure to read all of the sections, as the "Existing Badges" sections gives alot of context for 

## Existing Badges
The BYU Computing Boot Camp already has tons of badge designs that are ready for use. They can all found at the following link, as pngs and as their Adobe Illustrator 
Project Files: [TO DO] . There is a badge created for almost every module and sub-module currently on the site. For example, the module "Software Development" has it's own 
Module Badge that looks like this:

Each of the modules on the site have their own Module badge (as of 7/28/2021). 

Most of the sub-modules have their own Mini-badges. For example, the sub-module "Git" under the module "Software Development" has it's own Mini-badge that looks like this:

Almost all of the sub-modules have their own Mini-badge. A few don't have a Mini-badge because they represent too little knowledge to justify
a reward (like "Install Vivado/Vitis"), or they are a duplicate of another sub-module (like "Github" under "PCB", which covers the same knowledge as "GitHub" under
Software Development").

### Mini-Badges
Mini-Badges are the easiest badges to earn, and represent the smallest amount of knowledge. For example, to earn the "Make" Mini-badge, one must write two Makefiles that
implement functionality taught in the Make sub-module. This means that the Make Mini-badge will represent experience writing functional Makefiles, but not much else. For
this reason, the badge designs are simple yet elegeant. They clearly state the skill that was learned near the top, and state at the bottom that the recepient has a
"knowledge" of the skill. It is not an "expertise", due to the limited amount of code that they have to implement. The Mini-badges also have three logos on them, the Computing
Boot Camp logo on the left (cbc), a logo for Electrical and Computer Engineering on the right (ECE), and the BYU seal in the middle. These logos add legitimacy to the badge, 
represent who issued it, and add to the asthetic appeal of the Mini-badge.

Mini-Badges are color-coded, with the color on the ribbon representing which Module they fall under. The colors are taken from the 4 main colors found on the website 
banner, with the badges using the exact color on the banner, or a slight variation of the color on the banner. 

"Software Development" Mini-badges are light blue, which is a variation of the blue on the website banner.

"Commercial FPGA" Mini-badges are pink, which is taken off of the website banner.

"Open FPGA CAD" Mini-badges are red, which is taken off of the website banner.

"Robotics" doesn't have any sub-modules yet, and so doesn't have any Mini-badges. When they are made, they should have a unique color based off of the colors in
the website banner.

"Networking" Mini-badges are orange, which is taken off of the website banner.

"PCB" Mini-badges are blue, which is taken off of the website banner.

When creating a new Mini-badge under an existing module, be sure to make sure the color of the ribbon matches the color of the other Mini-badges under the same module.

### Module Badges
Module Badges are the hardest to earn, and represent the largest amount of knowledge. This is due to the fact that to earn the Module Badge, one must earn all of the
Mini-badges in all of the sub-modules for that modules. For example, if the user wants to earn the "Software Development" Module Badge, they must earn 14 Mini-badges, 
from "Git" all the way to "Matlab". This means that the Softwawre Development Module Badge will represent experience in all sorts of different software concepts, which
will make it alot more valuable. The idea is that the Mini-badges will help the user be motivated to keep learning and to keep track of their progress, while the
Module badges are what will actually be shared with employeers and educational institutitions as a certification of their skill. Both types of badges could be used
for both purposes, but they will generally fulfill the previously specified roles better.


## Creating a new Badge
While creating a new badge, be sure to use the previous designs as templates, so that all of the badges can blend well asthetically and make logical sense to the user.
