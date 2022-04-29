---
layout: page
toc: true
title: Creating Your Own Website
slug: setup_website
type: resources
order: 4
---


## Install

Follow the instructions to install Jekyll on Ubuntu: <https://jekyllrb.com/docs/installation/ubuntu/>

## Create Your Repo

1. Go to <https://github.com/byu-cpe/student_website_template>
2. Click **Use this template**
3. Name your repository appropriately:
    * Each Github user can have a website at *username.github.io*.  If you want to use this URL, you should name your repo *username.github.io*.  For example, if your Github username was *jgoeders*, you would name your new repository *jgoeders.github.io*.
    * Otherwise, you can name your repository anything else, and it will be available at *username.github.io/repo_name*.  For example, if your Github username was *jgoeders* and you named the repository *test_website*, the website would be hosted at *https://jgoeders.github.io/test_website/*.
4. Choose *Public* or *Private*.  Either is fine.  You can have your repository files be private and still host a public website. If you use the later option, you will need to use your student privileges to sign in to github. The server will not allow you to host a private website from github on a free account. 
5. Click *Create repository from template*

## Activate Github Pages

1. Go to your repository URL.
2. Click *Settings*.
3. Select the *Pages* page.
4. Choose to host your *main* branch (This may already be activated):

<img src = "{% link media/student_website/github_pages.png %}" width="600">


## Clone Your Repository

Make a copy of your website on your own computer using *git clone* (we will talk more about Git soon):

 For example, if I wanted to clone my website to the `website` directory in my home folder, I would do the following:

```git clone git@github.com:jgoeders/test_website.git ~/website```
 
 You can find the link for cloning your repo by going to your github page and clicking the ```Code``` button in the top left. Then select the *SSH* option and copy the link. Note that you will need to configure your machine with an SSH key to use this method (Google how to do this). Configuring your machine with a key will allow you to push and pull from your repo without signing in to your github account from the terminal every time.

 **Not recommended:** If you would like to just sign in to your repository each time you pull or push from your repo, then you can skip creating the SSH key and use the *HTTPS* option to clone your repo:
 
 ```git clone https://github.com/jgoeders/test_website.git```

## Configure your website

Open the `_config.yml` file, and look for the *baseurl* and *url* entries.  You will need to update both of these to the correct values:

For example, if I choose the first URL option above, I would set them to:
```
baseurl: ""
url: "https://jgoeders.github.io"
```
If I chose the second URL option, I would set them to:
```
baseurl: "/test_website/"
url: "https://jgoeders.github.io"
```

## Try Out Your Website

Jekyll allows you to host your website locally and try out any changes before you publish them.  

First you need to install the necessary packages for your website.  This only needs to be done once:
```
cd ~/website
bundle update
```
If you are having trouble with the `bundle update` command, you can try disabling ipv6. Run the following commands, 
and then run `bundle update` repeatedly until it successfully downloads all the packages:

```
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
sudo sysctl -w net.ipv6.conf.default.disable_ipv6=1
sudo sysctl -w net.ipv6.conf.lo.disable_ipv6=1
```

Then, to host your website simply run the following:
```
bundle exec jekyll serve
```
For the lazy, a *Makefile* is also provided that will run this when you type `make serve`.

When you run this, you should see output like this:
```
Configuration file: /home/jgoeders/website/_config.yml
            Source: /home/jgoeders/website
       Destination: /home/jgoeders/website/_site
 Incremental build: disabled. Enable with --incremental
      Generating... 
                    done in 0.432 seconds.
 Auto-regeneration: enabled for '/home/jgoeders/website'
    Server address: http://127.0.0.1:4000/test_website/
  Server running... press ctrl-c to stop.
  ```

The line to pay attention to is the `Server address: http://127.0.0.1:4000/test_website/`.  If you visit this URL in your browser you can preview your page.

Leave this running for now and we will make some changes in the next section.


## Make an Edit

1. In your browser, navigate to the *IMMERSE Log* page.
2. Now open your `_pages/log.md` file, update an entry and save the file.
3. Refresh your web browser and you should immediately see the change.


## Publishing Your Changes

Any changes you push up to Github will automatically be published after a short delay (usually not more than a few minutes).  We will talk about Git and Github soon.