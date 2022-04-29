---
layout: page
toc: true
title: PCB - Github
slug: github_PCB
type: archive
order: 3
---


# Github

## About Github

Github is an online file sharing website. It allows you to easily access and update schematic, pcb, and other project files.

## Getting Started

###  Making an Account

If you do not already have a github account you will need to create one at https://github.com/join.

###  Accessing Repositories

Repositories are where each group of files are stored. Once you have made your account, you will need to give your username to the administrator of the repository to which you would like access. This most likely is the faculty member in charge of the project. Once they add you to the project you will receive an email with an invitation to join. Once you accept the invitation you will see on the github home on the left a list of all the repositories that you have access to.

## Downloading Files

### Downloading Git Bash

For easy access to a github repository, you will need to download git bash at https://gitforwindows.org/. (If you have mac or linux this website may work, but it has not been tested https://git-scm.com/downloads). 

### Git Bash Commands

First, go the to folder where you would like to store the repository on your personal computer. Then right click and select "Git Bash here". This will open a command prompt. The first time that you add a repository use the command "git clone _"  (This is where you would put the web address of the repository. Ex._https://github.com/byuccl/Altium_PCB)

Once this has been done, the command "git pull" will automatically download updates that have been uploaded to github by other users.

## Uploading Files

### Adding

To upload any changes made to files start with "git add _" (File name). Use "git status" to see the names of every file that has been modified by you. Once you start typing the name of the file you can press 'tab' to autofill the rest of the file name. If they names of multiple modified are similar, keep typing until they differentiate. 

"Git add." can be used to add all modified files. This should only be used if the message that will be attached to the upload is the same for all modified files. (See commit below)

When choosing which files to upload, make sure to only upload files to which you have made meaningful changes. This will minimize the need for others to manually merge files. (Manually merging is discussed in 'uploading' below).

### Committing

After files have been added they must be saved using 'git commit -m "(reason for adding files to github)"'. Actual quotation marks must be used surrounding the reason to be attached to the files. 

If the reason for adding files is different, then multiple commits can be made before uploading any files.

Good commit messages are important because it makes it easier to find earlier versions of your work. 

### Uploading

Before uploading any new files, your computer's copies must be up to date with github. You may have to use "git pull" to retrieve any new files before being able to upload. If multiple people have made changes to the same file this cause an error if they cannot be merged automatically. In this case you will have to merge your changes manually. The easiest way to do this is to copy any files that you modified and then remove them from the github folder on your computer. Then use "git pull" to get the newest changes. If it still won't pull the new changes, delete the entire repository (without deleting your changes) and then reclone the repository. Then open your file and the new file and copy and paste your changes into the new file.

Once all modified have been committed the files can be uploaded to github using "git push". This will prompt you to enter your email and username connected to your github account using the commands 'git config --global user.name "Your Name"' and "git config --global user.email you@example.com".

### Git Ignore

Often programs generate files that aren't necessary to include in a repository. To avoid seeing these files when using "git status" you will have to create a .gitignore file. To do this, open a text document and choose 'save as' and add the file extension .gitignore to the file name. This file should be saved to the base of the repository folder on your computer. To choose which files are ignored using the patterns located [here](https://www.atlassian.com/git/tutorials/saving-changes/gitignore#git-ignore-patterns).

Once you have written and saved your .gitignore file you can git bash and enter the command "git config --global core.excludesfile (your file's name).gitignore". (FIXME I'm not actually sure if this step is necessary, needs further testing) If this doesn't ignore the desired files, trying using different ignore patterns. 

Another way to change which files git tracks is using "git rm - -cached ______(file name)". This command will stop a file from existing at all in the repository. (FIXME It's possible that it actually just makes certain files hidden. The results of using this command haven't been consistent. But it does successfully stop them from showing up as files modified.) 

### SVN

SVN is an alternative version control system and has been used in the past. If needed, [here](https://sliksvn.com/download) is the svn download link.

### Uploading through Altium

Once an Altium project has been made and uploaded to github it is also push changes through Altium. However, this only works with Altium files, so any other files in the repository will need to uploaded as explained above. 

To upload using Altium the project file must be open. From there, right click on any sheet that you would like to upload in the projects side panel. Then go to "version control". Select "Commit..." to upload one file at a time. Select "Commit whole project" to upload multiple files. Within the commit whole project option it is still possible to select which files will be uploaded. There will be a box for a commit message that should be filled in with a helpful message about the changes made. Using the commit whole project will apply one commit message to everything that is selected to be uploaded. Once the commits have been made you can go to version control -> push(#) to upload the commits. The # will let you know how many commits will be uploaded. 
