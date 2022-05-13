---
layout: page
toc: true
title: Docker
slug: docker
type: development
order: 12
---

## Lecture Video
On May 21, 2021 Prof Lundrigan discussed how to use Dockers. The video is embedded below. 

<iframe width="800" height="600" allow="fullscreen" src="https://www.youtube.com/embed/RP3QTEr58_Q"> </iframe>

## Installing Docker
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
  4. Install the Docker Engine
```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
  5. Verify installation
```
sudo docker run hello-world
```
   This should present a message that begins with "Hello from Docker!" 
