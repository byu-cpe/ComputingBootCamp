---
layout: page
toc: true
title: Git
lab: 1
type: development

---


# Git For Source Code Control

You will need to become proficient in the use of GIT for managing source code files.  It turns out to be very complex (and powerful).  As such, don't be worried that it is taking quite some time to feel comfortable with it. You will find yourself constantly referring to reference materials for a while.

On May 6, 2020 we had a Zoom-based Git Tutorial by Prof Nelson.  [You can find the video here]({% link media/GIT_Tutorial.mp4 %}) and [you can find the chat transcript here]({% link media/GIT_Tutorial_Chat.txt %}).

## A Suggested Approach

Git is one of those things that you can only read so much about until you really start using it for a project, which is when you will get good with it.  Thus, it probably merits only a few hours’ work to get familiar with it.  

Re-watch the video from above and replicate the basic steps you see there with some files of your own (make a copy into a new directory so you don’t mess with your existing good copies):

- Initialize a new repository.

- Add some files to it
- Commit them

- Change one or more of them
- See what has changed with “git status”
- See the changes with “git diff”
- Commit the changes

- Add a .gitignore file to the repo and commit it
- Set some aliases in ~/.gitconfig

- Back in your repo, see your history with “git log”

- Create a new branch and then check it out
- Check what branch you are on by noting where it shows up in “git status”.  Also see what “git branch” tells you
- Now, change a file and recommit
- Merge the branch’s changes back into master (you must checkout master to do this since a merge is always “merge something else into my current version")

- Look at the change log again to see how master vs. your branch are represented.
- See the diffs between your current version and some previous version from the change log history (use the first few characters of the big hash value for that other version as the identifier)
- See the diffs between your current version and what is in some other branch (as identified by the branch name)

- Go to a new directory on your computer and clone this repository you have created in a new place to see that you can clone them around just fine.

- Got to github and poke around with any repos you have access to.  Our byuccl/GoogleDeviceRep is not very interesting since there is almost nothing in the repo (it is all in the wiki which is a different repo).  So, if you can poke around some other ones like symbiflow/prjxray.

- Clone the wiki for byuccl/GoogleDeviceRep - it is - https://github.com/byuccl/GoogleDeviceRep.wiki.git
- Poke around it to realize that the wiki you have been reading all this time is itself a git repo.  Look in the various files to see how they compare to what you see on the wiki.

Be sure to do all the above experiments with some files you don’t care about - just copy a bunch into a new directory to experiment. 

## To Learn More


There are hundreds of printed tutorials on the web, find some and read them.  Here are some we have found:

- [Git and Github Tutorial for Beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)

- [Git Tutorial - Commands](https://www.edureka.co/blog/git-tutorial/)

- [Learning Git Branching](https://learngitbranching.js.org/?locale=en_US)

