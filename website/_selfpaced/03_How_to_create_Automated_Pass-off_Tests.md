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
First, I want to explain how the Automated Pass-off Tests are currently set up, so that you can understand why we are doing what we are doing. Currently, we are using a GitHub Repository with Github Actions to automated the testing process. The makeTest repository, that is owned by BYUComputingBootCampTests, is a fully functional automated testing repository for the Make Mini-badge. Try it out, see if you can earn the badge! Just reading through the README.md will give you alot of insight into how it works. The link to the repository is here: https://github.com/BYUComputingBootCampTests/makeTest.

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
This folder contains all of the files that outline workflows for GitHub Actions and CODEOWNER information for protecting our files. The workflows are contained in the "workflows" folder (and they have to be here to work), and the CODEOWNERS file is in this directory.

#### CODEOWNERS
The CODEOWNERS file is a file specific to GitHub, and specifies which users on the site are "owners" of code in certain parts of the repository. This doesn't actually make these
users owners of the code, as the repository will still be owned by the creator of the repository, but rather acts more like they have duties to protect the code by reviewing
changes to it.

The syntax for the CODEOWNERS file is as follows:

`<File(s) to be owned> @<User who will be a codeowner for it>`

A CODEOWNERS file can have as many of these lines as desired. The makeTest repository only has one line in it:

`* @BYUComputingBootCampTests`

A CODEOWNERS file can follow the same syntax as the linux terminal, so the * refers to all of the files in the repository. This means that the user "BYUComputingBootCampTests"
becomes a CODEOWNER of every file in the repository. And since the makeTest repository has settings that requires an approving review from CODEOWNERS before any merges can be performed, we effectively have disabled merging to our repository.

#### triggerPRruns.yml
The triggerPRruns.yml file contains the following code:

```
name: Trigger PR Test Runs

on:
  workflow_dispatch:
  schedule:
    - cron: '0/5 * * * *'

jobs:
  triggerRuns:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout Repository
      uses: actions/checkout@v2
    
    - name: Setup Node.js environment
      uses: actions/setup-node@v2.1.5

    - name: Install octokit/core.js
      run: npm install @octokit/core

    - name: Trigger makeTest.yml for each PR
      run: node .cbc/triggerRunForAllPRs.js ${{ secrets.AUTH_TOKEN }}   
```

I'll try to explain this from the top-down. 

Every workflow file should have a name, that will be shown when the workflow file is run in the Actions tab of the repository. I've named this workflow as the "Trigger PR
Test Runs" workflow. The syntax for naming is as follows:

`name: <name of workflow>`

Next, the `on:` defines when a workflow will run. See https://docs.github.com/en/actions/reference/events-that-trigger-workflows for information on the specific formatting
of this part of the yml file. Basically, you can add as many triggers as you want, and triggers can have specific settings (which are denoted by the "-" preceeding them). So,
in this workflow file, I have two triggers: workflow_dispatch and schedule. workflow_dispatch means that I can manually trigger it whenever I want in the Actions tab, which is
useful for debugging. schedule means that the workflow will automatically trigger according to a defined timetable. The line after "schedule:" that says

`cron: '0/5 * * * *`

defines the specific timetable that the workflow will run at. See https://docs.github.com/en/actions/reference/events-that-trigger-workflows#scheduled-events for information on
the syntax of the "cron" setting. This cron means that the workflow should run every 5 minutes (however, with GitHub's delay, this ends up being around 20 minutes on average).

Next, are the jobs, or tasks that the workflow will run. 

```
jobs:
    triggerRuns:
```

In this workflow file, I only have one job called "triggerRuns". 

`runs-on: ubuntu-latest`

This line tells GitHub Actions that I want the following job to be run on the latest Ubuntu version available.

Now, we get to all of the steps, or specific actions, that the job will do. Defining steps uses the following syntax:

```
steps:
  - (name:) (name of first step)
    (id:) (id for first step)
    (uses:) (Action to use)
    (run:) (Bash script commands to run)
  - (name:) (name of second step)
    ...
```
 
All of these options are techincally optional, but you need to have at least one of them for a step that actually does something (and for the workflow to properly compile). For all of the options you can define on a step, see the following documentation: https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idsteps. 

`name:` defines the name of the step to use on GitHub.

`id:` gives the step an id value, by which other steps can refer to this step, and recieve it's output.

`uses:` tells the step to run a pre-built action, that can make our lives alot easier. For example `uses: actions/setup-node@v2.1.5` will automatically install Node.js onto the
machine.

`run:` tells the step to run the following Bash script commands.

You can have as many steps as you want in a job, and they can all work together to pull off basically anything you want. I'll now explain the specific steps that I have in
the Trigger PR Test Runs workflow:

```
- name: Checkout Repository
  uses: actions/checkout@v2
```

This step downloads the repository onto the ubuntu machine.

```  
- name: Setup Node.js environment
  uses: actions/setup-node@v2.1.5
```

This step set-up node.js on the ubuntu machine for running javascript files.

```
- name: Install octokit/core.js
  run: npm install @octokit/core
```

This step installs octokit/core.js, so we can make API calls to the GitHub API using javascript.

```
- name: Trigger makeTest.yml for each PR
  run: node .cbc/triggerRunForAllPRs.js ${{ secrets.AUTH_TOKEN }}   
```

This step runs my custom triggerRunForAllPRs.js file, that uses API requests to the GitHub API to trigger a pass-off test for each open PR in the repository. Note the `${{ secrets.AUTH_TOKEN }}`. This tells GitHub Actions to replace this section with the variable value contained in secrets.AUTH_TOKEN. For the javascript file to sucessfully make
API calls, it needs an authorized token for the BYUComputingBootCamp 

As you can see, this workflow doesn't actually trigger any tests directly. Rather, it just sets up the necessary infrastructure to call a javascript file, which handles
the pass-off triggering.

For information on how to use the "triggerRunForAllPRs.js" file, see the section with the same name below.

#### makeTest.yml
The makeTest.yml contains alot of code, so I won't copy it as one big code block. Instead, I'll go through each line and explain what it does. I'll assume that you already 
have the context explained in "triggerPRruns.yml" section. If you haven't read that yet, go read it now.

`name: Make Test`

Here, I give this workflow the name of "Make Test".

```
on: 
  repository_dispatch:
    types: 
      [test_pr]
```

This tells the workflow to trigger on a GitHub API call, and the `types: [test_pr]` line tells it that the API call must specify the `event_type` as "test_pr" for it to
trigger this workflow.

```
jobs:
  runTests:
    runs-on: ubuntu-latest
    steps:
```

This defines a job called "runTests", tells it to run on the latest version of a ubuntu machine, and tells the file that we are about to outline some steps.

```
- name: Checkout Repository
  uses: actions/checkout@v2

- name: Setup Node.js environment
  uses: actions/setup-node@v2.1.5
  
- name: Install octokit/core.js
  run: npm install @octokit/core
  
- name: Install xmlhttprequest
  run: npm install xmlhttprequest
```

These steps download the repository, set-up Node.js on the machine, and install octokit/core.js and xmlhttprequest for making API calls with Javascript. octokit/core.js is
for making API request to the GitHub API, and xmlhttprequest is for making API calls to the Badgr API (for issuing badges).

```
- name: Get a Pull Request's Repo Name that isn't already being checked
  run: node .cbc/getRepoInfo.js ${{ secrets.AUTH_TOKEN }} full_name > repo.txt

- name: Save Repository name as Output Variable
  id: repo
  uses: juliangruber/read-file-action@v1
  with:
    path: repo.txt
```

These steps are a little bit confusing, but are a workaround for some of the limitations of GitHub Actions. The first step calls a javascript file that finds a PR that
isn't currently being checked (we use labels to be able to detect this), and then outputs the name of the forked repository that corresponds to the PR. This name is saved to a file. The second step takes the repository name from that file and saves it as an output for use later in the workflow. It is used to download the user's code from their forked
repository to then run tests on.

You may be thinking, why not just save the output of the javascript file as a variable? Well, Github Actions wasn't made to be a pass-off driver, and so it doesn't really
have variables in the traditional sense of the word. So, instead, we use this workaround so that the PR's name ends up as an output variable of the second step with the 
id of "repo".

For information on how to use the "getRepoInfo.js" file, see the section with the same name below.

```
- name: Get the Pull Request's Number
  run: node .cbc/getRepoInfo.js ${{ secrets.AUTH_TOKEN }} number > number.txt

- name: Save Repository Number as Output Variable
  id: number
  uses: juliangruber/read-file-action@v1
  with:
    path: number.txt
```

This is the same as the last two steps, except it gets the number of the Pull Request for later use, instead of the name of the corresponding repository. This number is 
used to make commments on the Pull Request so that the user can easily see how the pass-off went.

```
- name: Add "currentlyBeingChecked" label
  run: node .cbc/addLabel.js ${{ secrets.AUTH_TOKEN }} ${{ steps.number.outputs.content }} currentlyBeingChecked
```

This step calls a javascript file that adds a label to the Pull Request called "currentlyBeingChecked". This allows the getRepoInfo.js code to tell if a Pull Request is already
being tested so that it doesn't test a user's code twice, or miss a PR.

The addLabel.js file needs the number of the 

For information on how to use the "addLabel.js" file, see the section with the same name below.

### .cbc Folder
This folder contains all of the javascript files I wrote to assist the workflow files. It also contains an image called CBClogo.png that is used in the README.md of the respository, but for obvious reasons, I haven't documented how it works below. If you want to know what a .png file is, see the following link: https://en.wikipedia.org/wiki/File_format.

#### addLabel.js

#### assertContains.js

#### assertDoesNotContain.js

#### badgeAPI.js

#### getFile.js

#### getRepoInfo.js

#### makeComment.js

#### removeAllLabels.js

#### triggerRunForAllPRs.js

## Future Plans
