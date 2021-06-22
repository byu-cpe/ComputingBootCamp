---
layout: page
toc: true
title: Git
slug: git
type: development
order: 1
---


## Overview

You will need to become proficient in the use of GIT for managing source code files.  It turns out to be very complex (and powerful).  As such, don't be worried that it is taking quite some time to feel comfortable with it. You will find yourself constantly referring to reference materials for a while.

## Install
```
sudo apt install git
```

## Lecture

On May 6, 2020 we had a Zoom-based Git Tutorial by Prof Nelson.  The video is embedded below and [you can find the Zoom chat transcript here]({% link media/GIT_Tutorial_Chat.txt %}).

<iframe width="800" height="600" allow="fullscreen"
src="https://www.youtube.com/embed/sh_YkYK5p0o">
</iframe>

## Follow-Up Activities

Git is one of those things that you can only read so much about until you really start using it for a project, which is when you will get good with it.  Thus, it probably merits only a few hours’ work to get familiar with it.  

### Try the Basics
Re-watch the video from above and replicate the basic steps you see there with some files of your own (make a copy into a new directory so you don’t mess with your existing good copies):

1. Initialize a new repository.
1. Add some files to it, and commit them.
1. Change one or more of them, see what has changed with “git status”, see the changes with “git diff”, and commit the changes.
1. Check the history with `git log`.  
    * What other features does git log offer? For example, try it with `--stat`.
1. Add a .gitignore file to the repo and commit it.
    * Can you have multiple .gitignore files in your repo?
    * When you add an entry in a .gitignore file, is it recursive? Ie, are all files in the repo that match the entry ignored, or only those in the current directory?  Can you ignore files only in the current directory (not recursive)?

### Learn About Git Aliases
1. Set some aliases in ~/.gitconfig
1. Find some handy git aliases online.  One of my favorites: <https://stackoverflow.com/questions/1057564/pretty-git-branch-graphs>

### Play With Branches
1. Create a new branch and then check it out
1. Check what branch you are on by noting where it shows up in `git status`.  Also see what `git branch` tells you.
1. Now, change a file and recommit.
1. Merge the branch’s changes back into master (you must checkout master to do this since a merge is always “merge something else into my current version")
1. Look at the change log again to see how master vs. your branch are represented.
1. See the diffs between your current version and some previous version from the change log history (use the first few characters of the big hash value for that other version as the identifier)
1. See the diffs between your current version and what is in some other branch (as identified by the branch name)

### Merging and Conflicts
1. Experiment with merging between branches.
1. Can you forcibly create a conflict?  
1. If you start a merge and run into a conflict, how do you back out and abort?
1. Get comfortable with the steps to resolve a conflict.

### Fun With Remotes
1. Clone a repo from Github.  You could try:
    * The bootcamp website: <https://github.com/byu-cpe/ComputingBootCamp>
    * The ECEN 330 student repo: <https://github.com/byu-cpe/ecen330_student>
    * Want to look at something with lots of branches, issues, PRs? <https://github.com/verilog-to-routing/vtr-verilog-to-routing>
1. Check what branches you have locally.  Can you view all the remote branches locally?
1. Can you have multiple remotes?  Why would you want to do that?

### Git Merge vs Rebase

Learn about merge vs rebase:
  * <https://www.youtube.com/watch?v=CRlGDDprdOQ>
  * <https://stackoverflow.com/questions/804115/when-do-you-use-git-rebase-instead-of-git-merge>

### Git GUI Tools
There are many great tools to [visualize your Git repositories and histories](https://www.tecmint.com/best-gui-git-clients-git-repository-viewers-for-linux/). Try one out.  

### Git is Always Changing
  * <https://stackoverflow.com/questions/57265785/whats-the-difference-between-git-switch-and-git-checkout-branch>
  * <https://github.blog/2020-07-27-highlights-from-git-2-28/#introducing-init-defaultbranch>


## To Learn More
There are hundreds of printed tutorials on the web, find some and read them.  Here are some we have found:

- [Git and Github Tutorial for Beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
- [Git Tutorial - Commands](https://www.edureka.co/blog/git-tutorial/)
- [Learning Git Branching](https://learngitbranching.js.org/?locale=en_US)

