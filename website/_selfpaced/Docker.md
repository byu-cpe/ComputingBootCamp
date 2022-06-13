---
layout: page
toc: true
title: Docker
slug: docker
type: development
order: 12
---
## Docker
A brief intro to Docker. It allows you to run processes in isolated containers. A docker 'containter' is standalone package of software that will run reliable regardless of the computing environtment. 
Docker can be used to build software and aplications, share content and colaborate with other developers, and run the resulting applications. 
## Installation
  1. Update the `apt` package index and install necessary packages
``` 
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```
  2. Add Docker's official GPA key
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
  3. Set up the stable repository
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
  4. Install the Docker Engine (hit `enter` when asked "Do you want to continue?")
```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
  5. Verify installation
```
sudo docker run hello-world
```
   This should present a message that begins with "Hello from Docker!" 

#### Common Error
When trying to run your first docker, you might get this error: 
```
docker: Got permission denied while trying to connect to the Docker daemon socket at...
```
If this happens, enter `sudo chmod 666 /var/run/docker.sock` to change the permissions on the docker.sock file.

## Lecture Video
On May 21, 2021 Prof Lundrigan discussed how to use Dockers. The video is embedded below. 

<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/RP3QTEr58_Q"> </iframe>

#### Time Stamps
 - 1:20 - What is Docker?
 - 9:50 - Terminology
 - 11:50 - ps
 - 12:46 - run ubuntu
 - 22:00 - run python
   - 24:35 - volumes
   - 27:40 - docker hub
   - 29:29 - docker files
   - 35:53 - portainer
 - 40:15 - build and run image from Dockerfile
 - 46:24 - build docker that runs as web app

## Docker Cheat Sheet
Commands:  
  - ps (-a): Shows current dockers that you have
  - run: creates a container
  - start: restarts a previous container
  - exec: runs a command for an existing container
  - stop:
  - images: shows your repo of images
  - build: an image from a dockerfile

Options:  
  - --rm: automatically removes containter
  - -it: interactive terminal
  - -v: volume, enter absulote path to directory and name of directory as you want it to appear in container, synchronizes this folder

## Conclusion
Summarize the key takeaways, add furthur application

## Activities
 - Run your csv_parser.py program in a docker container, you will need to create a container using -v to have the files you need
 - Install portainer
 - explore portainer website, crete a new image using portainer


## Certify your skills
We might add a badge

## Additional Resources
Add links to sources that dive deeper
