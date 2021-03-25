---
layout: page
toc: false
title: Comments and Working Notes
lab: 1
---

The following goes through the webpage (not the schedule) to discuss what to do with each thing there...

Should next revisit the schedule and see what is missing...

# Brent
Since I wrote many/most of these last spring I am happy to do initial reorganizing and refactoring.  

But, I have no ties to any specific ones and won't be offended if others shred them.   Most were thrown up in anywhere from 5-45 minutes without much thought, just to get something up so we had a topic for the next week.
## Get a VM - DELETE
- The get VM doesn't really make sense any more. 

## Create a VM - RENAME, UPDATE, NO_SELF_PACED, NO_LECTURE, BY_WHOM?
- The create VM only makes sense if we don't have sufficient seats for our students since  I propose we plan on in-person and insist our students come in. Proposal: 
    - Point them at an on-line tutorial to do the clean instalon really how to do a clean install 
    - Add fold the Customize Your VM stuff into the end of this
    - Move FPGA-specific stuff elsewhere
    - Rename to "Create and Set Up a Linux VM"
- In the end, its existence is only for reference - no need to lose the info, may come in handy

## Customize Your VM - MOVE_CONTENT_ELSEWHERE, DELETE
- Move the FPGA-specific stuff
- Delete outdated stuff (RapidSith)
- Move good stuff into topic above

## VS Code - CREATE, SELF_PACED, BY_WHOM?
- I had students balk at using VS code last summer.  I plan on telling them they ing them use something without a good debugger was not worth it.
- Need to flesh this out, have listed a few topics on the page itself.

## Linux Stuff - SELF_PACED, UPDATE, BY_WHOM?
- Clearly needs fixing up - was the result of a good 4 minutes of my time last spring...
- Should point at some good tutorials
- Should decide what we really want them to know, I would hope we could go beyond the 220/330 level treatment and expect them to actually know command line.  
- But that begs the question - why, especially given our conversation of today? I thus recommend we have some serious command line stuff to maybe motivate it - would want them to be things that would be quite difficult graphically.  See bottom of that page for some new things we might could add....

## Git - SELF_PACED, UPDATE, BY_WHOM?
- Currently is just an overview, pointer to video, links to tutorials
    - Is that enough or should we force them to do something specific with it on a real set of files?  I think we should.
    - Should we also add github stuff to this one and call it 'Git and Github'?
        - We do have something on Github Contribution Best Practices at the byu-cpe/BYU-Computing-Tutorials that we could copy over
- Once this is in place I think we should make them then install jekyll and do a pull request regarding updating the CCL page like you suggested.

## cmake and make - INFORMATION-ONLY???, SELF_PACED???, BY_WHOM?
- Currently nothing is here but we have link to Goeders' video from last year at byu-cpe.
- Do we want to go beyond that or consider this an information only topic.
    - I sort of lean to information only but don't feel strongly.
    - I would hope that the students were exposed to it so they don't panic when they see cmake files and have a resource to go back to when they do
- Either way, should point to on-line tutorials (there have to be many)

## Python and Conda - SELF_PACED, BY_WHOM?
- On byu-cpe we have some stuff:
    - Goeders' talk on python/C++ programming and development ideas
    - A python virtualenv page
    - A conda virtual environments page
    - Something on managing multiple virtual environments (I think we should nuke that one - it can cause problems)
- I propose we pull them together into one page
- I propose we come up with a self-paced activity for conda - I have migrated to that one 100% and already have my own recipes and notes on how to use it I could add as well
    - I have had a couple grad students mess up large shared machines by not using a venv
    - I have had a grad student get something working that I don't think should have, and I have always feared he messed up a machine doing so

## SQL Basics - INFORMATION-ONLY, BY_WHOM?
Don't know where this came from but I believe it was one of my students (Ethan?)
- Doesn't hurt but a link to sqliteonline.com would be sufficient
- What has been useful to my Symbiflow projects (litghost's stuff) is students being able to interact with sqlite from within Python
    - Adding that could have value but it seems pretty specialized
- I could go with NUKE or INFORMATION-ONLY

## Install Vivado/Vitis - KEEP, UPDATE?, BY_WHOM?
- Good stuff - anything missing?
    - Do we want instructions on pointing to a license server?  I assume that is too specialized.  We rarely, if ever, need anything we cannot do with the open version...

## Vivado Tutorial - KEEP, UPDATE?, BY_WHOM?
- What is there is specific to IP integrator, block designs, the PS.  
    - Should keep but could be in a later section or different document?
    - How about the first section being a vanilla Vivado tutorial from 220?  We could just point to it, or we could copy over the relevant stuff, or we could ...
        - I note that the 220 one it has both GUI and Tcl ways of doing a couple of things.

## Tcl and Vivado - SELF_PACED, UPDATE, MORE_SPECIFIC_ACTIVITIES, BRENT
- I wrote this and am happy to take first cut at updating it
- First goal is to simply make them run an entire design through Vivado in case they are rusty.
- Second goal is to learn how to redo all that using Tcl only
- Third goal is to learn how to interact with a device or implemented design in Vivado: `get_cells -hierarchical`, `get_pins -of $c`, ...
- Fourth goal was to learn a bit about lists, file I/O, loops, etc.
- Would be nice if the self paced activities were more relevant to something they care about.

## Vitis Tutorial - SELF_PACED?, JEFF
- Love it but not sure if it needs anything

## Vitis HLS Tutorial - DITTO_TO_ABOVE
- Jeff?

## Project X-Ray - NUKE?, INFORMATION_ONLY?, SELF_PACED?, BY_WHOM?
We were pretty new to it last year and so didn't have much to say.

- Content free - just says to install it by following instructions
- Idea #1: replace that with pointers into the Symbiflow site - informational only
- Idea #2: make them install it and do something that requires them to pick through the database files
- Idea #3: give them a talk on it as enrichment.  

I would prefer not to nuke it completely

Maybe a guided read through the various Symbiflow projects and their documentation for big picture sakes is enough? 

Or, maybe make them do something in Python to interrogate the database files to get a slightly deeper introduction.

Or, maybe just give them an easter egg hunt - ask them a bunch of questions which can only be answered via database files or documentation or github repo (looking at the various projects).

## prjxray Install - MERGE_IF_KEPT, BY_WHOM?
- Overlaps with above Project X-Ray topic as well as the virtual environments stuff
    - Just merge in with them if kept at all...

## FASM, fasm2bels, symbiflow-examples - ???
- In each case is not terribly deep
- How to handle them
    - Good in that it points them to it so they are even aware of their existence
    - Running them asre and might be an 'aha' moment
        - Platform to talk about primitives vs. behavioral Verilog code with fasm2bels
        - Would see Verilog netlists
    - But, do we have much to add w.r.t. this other than that they should run it?
- See below for idea

## bram-patch - SELF_PACED, BRENT
- This project could be interesting in that it pulls together a number of things from above: prjxray, bits2fasm, Vivado, Tcl, etc.
    - Maybe have this be the vehicle to lead them through an entire project 
        1. Do simple design in Vivado that has some BRAM's with INIT files
        2. Implement it
        3. Use bram-patch to change the BRAM initial contents and patch FASM\
        4. Update bitstream using fasm2bits
        5. Re-execute design in hardware (if boards available)
- Thoughts?

## Symbiflow VTR - ???
- Once again, not sure how to get them to engage with this.  
    - symbiflow-examples from above has some end-to-end designs you can run
        - Get them to engage with VTR by running the visualization tools?

# Other Topics
- Last year we talked about some things that we have nothing for