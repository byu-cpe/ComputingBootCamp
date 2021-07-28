# How to create Automated Pass-off Tests
In order to award badges, the BYU Computing Boot Camp is currently considering using a mixture of "project" based assessments and "code" based assessments. For the project-based
assessments, users will create an end-product that will involved the subject taught, but will also involve alot of creativity on their part. This will require these projects to
be reviewed by human staff of the Computing Boot Camp website (probably Undergraduates), who will then manually award the badge if they believe the project proves that the user
has sufficient knowledge in the subject. However, the code-based assessments will require the user to create software that conforms to specified instructions, meaning that an
automated pass-off test can be used to evaluate the user's work and then award the badge. Whether a project-based assessment or a code-based assessment is used to award the badge
for a specified sub-module will be up to the discretion of the staff of the BYU Immerse Program.

This guide will attempt to explain how to create an automated pass-off test in order to implement a code-based assessment. This is a complicated guide, and may require a couple of
read-throughs for you to fully understand it, so don't lose hope if parts of this are going over your head. In addition, I'm not a perfect writer, so if something doesn't seem
to be adding up, a quick Google search should be enough to fill in the gaps.

## How it works
First, I want to explain how the Automated Pass-off Tests are currently set up, so that you can understand why we are doing what we are doing. Currently, we are using a GitHub Repository with Github Actions to automated the testing process. The makeTest repository, that is owned by BYUComputingBootCampTests, is a fully functional automated testing repository for the Make Mini-badge. Try it out, see if you can earn the badge! Just reading through the README.md will give you alot of insight into how it works. 

Using the makeTest repository as an example, I'll outline the process. First of all, the user needs to fork the repository, write the necessary code, and then submit a pull requeset. This is necessary because it gives us a way of finding the user's code, through the pull request that has been submitted. It also gives us the liberty of providing starter files for the user to work with, along with a README.md that contains instructions. 

You may be wondering, what happens if the Pull Request gets merged? Wouldn't that potentially mess up the repository? You'd be correct, and for that reason the framework is set up so that the user only needs to SUBMIT a Pull Request, not merge one. The Pass-off files will automatically pull the necessary code from the user's pull request, and so no merging is necessary. In addition, if we allowed merging, users could potentially edit the pass-off tests to cheat the system (more on that later). For this reason, the makeTest repository also has settings enabled that don't allow merging without approving reviews from CODEOWNERS (users on GitHub with "ownership" over the code). The CODEOWNERS file, which is always found within a .github folder in a repository, specifiies which users own which code. The makeTest repository has deemed the BYU ComputingBootCampTEsts user as a CODEOWNER for all the files in the repository, which effectively means that nothing can be merged without our approval, stopping any malicious activity.

After the user submits their pull request, GitHub Actions comes into play. GitHub Actions allows for automated commands to be run on a machine with the repository's contents. Using this functionallity, we can have the machine execute pass-off code to evaluate the user's code. The actions are triggered by workflow files, that are always stored in the .github/workflows folder in a GitHub repository. If the workflow files aren't present here, you won't be able to use them. The workflow files are set up to run once every 5 minutes (but with delay on GitHub's side, this ends up averaging at around every 20 minutes), and once these files run, they look to see if there are any open pull requests. If there are, they start to work their pass-off magic. 

Because these workflow files are stored within the repository itself, that means that every single user has access to look inside these workflow files and edit them if they so desire. This is what would allow users to "cheat the system" if we allowed merging in our repository. All they would have to do is remove all the pass-off lines of code in the workflow files, and leave the line that submits the badge to them. It's incredibly easy, and so we have set up the framework for the user's submited code and our pass-off code to remain seperate at all times (This is also why we don't just have the pass-off files run whenever a pull request is submitted. This would cause GitHub Actions to run the workflow files in the user's code, which could have been edidted by the user). So, even though it may be a little strange, this is why the user submits a pull request, and then the respostiroy itself pull data from the forked repository.

Now, we get into the pass-off magic. There are actually two workflow files that are in the .github/workflows folder, the triggerPRruns.yml workflow and the makeTest.yml. The one that runs every 20 minutes is the triggerPRruns.yml, which I'll refer to as the "Trigger PR Test Runs" workflow. This workflow is in charge of finding all of the open pull requests, and then using a javascript file in the .cbc folder to trigger the makeTest.yml workflow on each one. Why is this necessary, you may ask? This is to allow us to run multiple tests simulaneously. We want the workflow file to run a test for each of the open pull requests, but GitHub Actions only allows us to trigger a certain workflow once every 5 minutes (at the most). By having two workflows, the Trigger PR Test Runs workflow is triggered once every 20 minutes-ish, and it can trigger the makeTest.yml workflow on each and every open Pull Request (up to 12, as the tests take some time, and if two Trigger PR Test Runs workflows run concurretntly, it will break the repository). So, if multiple users submit PRs, they will all have their code testied in around 20 minutes.

The makeTest.yml workflow, which I'll refer to as the Make Test workflow, is what actually tests the user's code. It goes to the specific PR, grabs the files we want to test, and then can use script commands to do all sorts of things (like build and compile code, run other programs, run linux commands, etc). The Make Test workflow grabs two Makefiles from the user's repository, builds code with them, runs the code and asserts that the output is correct, and then issues the Make Badge. All of this is easily facilitated by javascript files that I have written in the .cbc folder, which the Make Test workflow uses frequently. Finally, the Make Test workflow will issue comments on the PR throughout the testing process, so that the user cna know exactly where they passed and exactly what they messed up.

That is the entire process! Hopefully it's not too complicated to understand. A similar process can be used for all code-based automated testing repositories that we want to make in the future. And since all of this code is publicly available in the .github and .cbc folders, it will be easy to reuse and adapt to other pass-off drivers.

## The Specifics
Now, I will go into the specific's of each file and how they work exactly, so that you can edit these files according to your pleasure, or even create your own.

### .github Folder

#### CODEOWNERS

#### triggerPRruns.yml

#### makeTest.yml

### .cbc Folder

#### 

####
