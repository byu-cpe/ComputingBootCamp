---
layout: page
toc: true
title: Web Technologies
slug: webTechnologies
type: development
order: 6
---

## Overview
Web browsers rely on a variety of technologies to load webpages and deliver a seamless experience to its users. The fundamentals of web technologies revolve around creating and displaying webpages, handling data, and utilizing network protocols that enable these processes. Most web browsers come with an *Inspect* tool, which allows users to explore a website's HTML, CSS, javascript, sources, and networking protocols that make the site functional.

In this module, you will learn how to:
1. Analyze how websites work using inspection tools.
2. Build your own webserver.

## Lecture Video

On May 16th, 2022 a tutorial was given on Web Technologies by Prof Lundrigan. The video is embedded below:

<iframe width="560" height="315" src="https://www.youtube.com/embed/valULtQpank" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Webpage Inspection Activities

- **Use `curl` to download a webpage's HTML.** Open your terminal and execute the `curl` command to fetch the HTML of a webpage. Examine the structure of the HTML to better understand how the page is built.
    - For example, `curl https://www.example.com` will fetch the HTML of [www.example.com](https://www.example.com).
- **Open your browser's web inspector.** Right-click within any webpage and select the option to "Inspect" or "Inspect Element" to open the Inspect tool in Chrome (or your browser of choice).
    - Explore the "Elements" tab to see the HTML and CSS that determine the structure and style of the page.
    - Explore the "Sources" tab to see all of the resources that contribute to the webpage, including JavaScript files, images, and stylesheets.
    - Explore "Network" tab. Reload the page to see all of the page's sources being downloaded.
- **Host your own webpage on CAEDM.** Create a simple HTML file and host it on CAEDM ([https://caedm.et.byu.edu/wiki/index.php/Web_Space](https://caedm.et.byu.edu/wiki/index.php/Web_Space)).

## Web Servers
When a user agent (such as a web browser) loads a webpage, it communicates with a web server and makes a request for the webpage at the given address. The web server then responds with either the webpage (if successful) or an error message. This communication relies on network protocols such as HTTP or HTTPS, and these protocols enable servers to do much more than just serve static HTML pages—web servers can communicate with the user agent to provide dynamic and interactive experiences in a variety of ways.

There are several web frameworks that help developers create web servers. For example, the BYU Computing Boot Camp website that you are on right now is built with [jekyll](https://jekyllrb.com/), a framework that converts markdown files and other documents into static websites with ease. In contrast, another well-known framework called [Flask](https://flask.palletsprojects.com/en/stable/#) supports the creation of both static and dynamic websites and proves to be quite versatile, making it a popular choice for Python developers.

This module will guide you through building a webserver using the Flask framework.

## Flask Overview
Flask is a Web Server Gateway Interface (WSGI) library for Python. It is a popular web application framework that allows developers to build webservers with ease. Flask was designed with a modular layout, making it very beginner-friendly to less experienced users while simultaneously providing a wide selection of optional tools, libraries, and extensions for use in more advanced applications. As such, setting up Flask for the first time is a rather straightforward process.

## Setting Up Flask
These instructions are based on the [Installation Instructions](https://flask.palletsprojects.com/en/stable/installation/) in Flask's documentation. You will need to make sure that Python is installed on your device (you can check this by executing `python --version` in your terminal). 
1. Begin by creating a project directory for your Flask application.
2. Navigate your terminal to the project directory and create a Python virtual environment. You can do this using Python's build in 'venv' module. Simply run the following command:
```
python3 -m venv .venv
```
3. Activate the virtual environment with the following command:
```
. .venv/bin/activate
```
Note that you can deactivate the virtual environment by simply executing `deactivate` in your terminal.
4. Lastly, install the Flask library with the following command:
```
pip install Flask
```
Because the virtual environment is active, this will install Flask locally rather than system-wide, giving you more control over managing and updating your project's dependencies.

Your Flask project is now set up and ready for web development!

## Creating a Simple Webpage
We will now follow instructions from the [Quickstart Guide](https://flask.palletsprojects.com/en/stable/quickstart/) in Flask's documentation to create a simple webpage that reads, "Hello, World!"

Create a new python file and name it "hello.py" or similar. This will be your main Python script that sets up your Flask application. Add the following code to your Python file:
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
This is all the code you need to make a working "Hello, World!" page. Here's how it works:

**Importing Flask:** 

```
from flask import Flask

app = Flask(__name__)
```
Here, the Flask class is imported, and a Flask application is initialized and saved under the variable `app`. The `__name__` parameter is a special Python variable that returns the name of the python file the code is running in; passing this into our Flask application tells our app to look for resources there.

**Creating a Webpage and Defining a Route**

```
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```
Here, we create a `hello_world()` function that returns a snippet of HTML. `@app.route("/")` is a decorator that tells our Flask app to map this function to the root address of our web server. When you run the webserver locally and navigate to 'http://localhost:5000/' (the default port that Flask uses), the server will respond with the HTML content returned by 'hello_world()'.
   - Note that 'hello_world()' can be mapped to a different address by changing the argument passed to `@app.route()`. For example, if we had used `@app.route("/helloworld/")`, the hello world page would be accessed at 'http://localhost:5000/helloworld/' instead of the root address.

Now that we have created a simple webpage for our application, let's run the application and see it in action!

## Running the Flask App
To run our Flask application, execute the following command in the terminal:
```
flask --app hello run
```
where `hello` is whatever you named the Python file containing your Flask application code. If all is successful, you will see the following in your terminal:
```
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```
Now, control-click on 'http://127.0.0.1:5000' or paste it into the address bar of your browser, and you will see a mostly blank page with the text, "Hello, World!" Congratulations, you have successfully created your first webpage via Flask!

## Flask: Self-Paced Activities
Creating a Hello World webpage using Flask is rather straightforward, but it only scratches the surface of Flask's capabilities. The activities below are designed to help you learn more about the features of Flask and design your own interesting web applications:

* **Create additional webpages.** Add more webpages to your flask web server. Recall that changing the parameter of `@app.route("/")` changes the url of the webpage. Try creating routes for pages like `/about/` or `/contact/`.
* **Build a simple login page.** Follow this [Flask GeeksForGeeks Tutorial](https://www.geeksforgeeks.org/flask-creating-first-simple-application/) to create a simple login page. Begin with the paragraph that reads, *"We can also use HTTP methods in Flask ..."*.
* **Explore the Quickstart Guide.** Continue through the [Flask Quickstart Guide](https://flask.palletsprojects.com/en/stable/quickstart/) to expand your Flask app even further. Look at the different features presented in the guide and play around with them in your Flask project.
* **Create a Makefile.** Create a Makefile to easily run your Flask server normally and in [debug mode](https://flask.palletsprojects.com/en/stable/quickstart/#debug-mode).
* **Learn about template inheritance.** Use [Template Inheritance](https://flask.palletsprojects.com/en/stable/patterns/templateinheritance/) to create a custom title, header, and/or footer shared within all pages of your site.
* **Design a homepage.** Create a homepage that contains the following:
   * A welcome message.
   * An image.
   * At least three links to other pages in your flask project. Make sure each page also links back to the homepage (this can be accomplished automatically with template inheritance).

## Additional Resources
* [Chrome DevTools Documentation](https://developer.chrome.com/docs/devtools)—outlines the capabilities of Chrome's webpage inspection tools.
* [Flask Documentation](https://flask.palletsprojects.com/en/stable/)
* [GeeksforGeeks Flask Tutorials](https://www.geeksforgeeks.org/flask-tutorial/?ref=lbp)
* [Flask-Login](https://pypi.org/project/Flask-Login/)—a Python module that expands Flask's capabilities for user session management.
* Helpful web-related Wikipedia articles:
    * [Web application](https://en.wikipedia.org/wiki/Web_application)
    * [Web server](https://en.wikipedia.org/wiki/Web_server)