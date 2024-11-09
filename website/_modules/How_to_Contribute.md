---
layout: page
toc: false
title: How to Contribute
slug: contribute
type: resources
---

Any contributions to this website are welcomed and appreciated! In order to maintain a consistent layout and flow to the website to provide a more refined learning experience, this page provides a helpful guide on how to create/maintain modules. 

## Guide for Creating a New Module

1. Fork the [ComputingBootCamp repository](https://github.com/byu-cpe/ComputingBootCamp) and clone it. Modify the repository on your cloned repo locally on your computer. 
1. Determine which category your topic falls under (Software Development, Robotics, etc.)
1. Create a new Markdown file for your new module in the ```ComputingBootCamp/website/_modules/``` folder. Follow the naming convention of the other files already in the folder. 
1. Start creating the module page! Follow the format shown below. Make sure to change the ```type: <module_category>``` line at the top of your Markdown folder so it appears in the correct category. 
1. Preview your changes by hosting your website. Follow the instructions on [this page](https://byu-cpe.github.io/ComputingBootCamp/tutorials/setup_website/#try-out-your-website) to host the website locally. 
1. Once you've made all changes/additions: 
  - Stage the changes (using ```git add```)
  - Commit the changes (using ```git commit```)
  - Push the changes to your forked repository (using ```git push```)
  - Go to your forked repo on GitHub, and create a new pull request.

### Format for module pages

  - Overview
    - This may be the first time a student has ever even heard of the topic. Describe it in simple terms, and include a link to an official website (if one exists) that represents the topic. Briefly describe why it will be useful for students doing the Bootcamp.
  - Install
    - Try to be as verbose as possible here. Describe the installation so that anyone could do it, even someone with little to no knowledge of how to use a terminal.
  - Lecture
    - Some topics have previously recorded tutorials by BYU faculty. This section may not apply to new modules, and can be skipped.
  - Learn More
    - This section should contain curated links that contain the best of the best info/tutorials on the topic. Ensure that these links only contain high-quality content.
  - Follow-Up Activities
    - These activities are crucial to help students bridge the gap between simply being tutorial content sponges and becoming capable and skillful engineers. Include several activities that won't exhaust the student, but require them to look beyond simple examples included in tutorials. Open-ended examples are helpful for students to start thinking on their own about how to apply their newfound skills. 

<!-- 

Pages that fit style guide:
  - 

Pages that require changes:
  - 
 
 -->
## Running Website Locally

1. [Install Jekyll](https://jekyllrb.com/docs/installation/)
2. Run `bundle install`
3. Run `make serve`.  The website will be hosted locally. Check the console output for the address.