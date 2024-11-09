---
layout: page
toc: true
title: Docker
slug: docker
type: development
order: 13
---

## Docker
Docker is a way to separate processes into what can be thought of as lightwieght virtual machines. It allows you to run processes in isolated containers. A docker 'containter' is a standalone package of software that will run reliably regardless of the computing environtment. Have you ever had the issue of a program working on your friend's machine but not on yours? Giving everybody a well configured Docker container to run the program in can solve this problem. This is especially powerful when used to build software and applications, or to share content and colaborate with other developers. You can also add an extra level of secuirity by running a webapp through docker. If your webbapp is hacked, they will only have access to your docker container and not to your local machine.

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
If this happens, use the command `sudo chmod 666 /var/run/docker.sock` to change the permissions on the docker.sock file.

## Lecture Videos

### Lecture 1
On May 21, 2021 Prof Lundrigan discussed how to use Dockers. The video is embedded below. 

<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/RP3QTEr58_Q"> </iframe>

#### Time Stamps

[0:00](https://www.youtube.com/watch?v=RP3QTEr58_Q&t=0s) Introduction<br>
[1:20](https://www.youtube.com/watch?v=RP3QTEr58_Q&t=80s) What is Docker?<br>
[9:50](https://www.youtube.com/watch?v=RP3QTEr58_Q&t=590s) Terminology<br>
[11:50](https://www.youtube.com/watch?v=RP3QTEr58_Q&t=710s) ps<br>
[12:46](https://www.youtube.com/watch?v=RP3QTEr58_Q&t=766s) Run Ubuntu<br>
[22:00](https://www.youtube.com/watch?v=RP3QTEr58_Q&t=1320s) Run Python<br>
[24:35](https://www.youtube.com/watch?v=RP3QTEr58_Q&t=1475s) volumes<br>
[27:40](https://www.youtube.com/watch?v=RP3QTEr58_Q&t=1660s) Docker Hub<br>
[29:29](https://www.youtube.com/watch?v=RP3QTEr58_Q&t=1769s) Docker files<br>
[35:53](https://www.youtube.com/watch?v=RP3QTEr58_Q&t=2153s) portainer<br>
[40:15](https://www.youtube.com/watch?v=RP3QTEr58_Q&t=2415s) Build and run image from Dockerfile<br>
[46:24](https://www.youtube.com/watch?v=RP3QTEr58_Q&t=2784s) Build Docker that runs as web app

### Lecture 2
On May 20, 2022 Professor Lundrigan gave another lecture on Docker. The video is below.

<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/yB_D04Yt5P4"> </iframe>

## Docker Cheat Sheet
Commands:  
  - ps: print a list of the docker containers that are currently running
     - -a will also print containters that were created but are not currently running
  - run [image name]: creates a container
     - -it makes the container interactive
     - --rm will delete the container as soon as it is done running
     - -v [path/to/host/folder:/name_of_folder_in_container] allows you to access certain files from a container
     - -p [localport:containerport] maps port from the container to a port on your local machine to run the webapp
  - start [name]: restarts a previously created container
  - exec [command]: allows you to interact with containers that are running in the background
  - stop [name]: stops running a container
  - images: shows your repo of images
  - build: build an image from a dockerfile
     - -t tags the container for you

## Conclusion
Docker is a powerful tool for developers to build, ship, and run applications. You can stage a standardized environment that can be easily set up and used across an organization, or a team of developers. It is excellent for finding and fixing bugs. You can execute the testing of an application in a Docker container, then make edits and relaunch your design when bugs are identified. This provides quick verification of your fixes and leads to an efficient developement process. Updates are then easy to distribute by pushing your new docker image to the production environment. The ability to easily set up isolated environments is perfect for use in continuous integration and continous deployment. There is also a wide variety of docker images and applications that you can take advantage of as a user. Check out some of these examples:  
 - [Plex](https://hub.docker.com/r/linuxserver/plex) media server
 - [Home Assisntant](https://hub.docker.com/r/homeassistant/home-assistant)
 - [Handbrake](https://hub.docker.com/r/jlesage/handbrake) digital video transcoder
 - [Unifi](https://hub.docker.com/r/linuxserver/unifi) WiFi managemer
 - [Watchtower](https://hub.docker.com/r/containrrr/watchtower) automates updates to docker images

## Activities
 - Run your csv_parser.py program in a docker container (you will need to create a container using -v to have the files you need)
 - Install portainer
 - Explore the portainer website, create a new image using portainer
 - Browse dockerhub and find a couple of cool images. Find the image layers of their latest version

## Additional Resources
 - [Official Docker Overview](https://docs.docker.com/get-started/overview/)  
 - [Awesome-docker](https://awesome-docker.netlify.app/)  
 - [A 13 Part Docker Tutorial Series](https://rominirani.com/docker-tutorial-series-writing-a-dockerfile-ce5746617cd)  
 - [A Docker Container Manager in Minecraft](https://github.com/docker/dockercraft)  
