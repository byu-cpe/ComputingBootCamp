---
layout: page
toc: false
title: Quiz Questions
slug: quizzes
type: resources
---
In order to provide a better learning experience and check the learner's understanding of material, we have included some templates for quiz questions to embed throughout the various pages of the site. Consider adding a question or two to pages that don't have any already!

## Adding a New Question
This tutorial will not go over Git and Github. See [How to Contribute]({% link _selfpaced/01_How_to_Contribute.md %}) for help setting up your repository.

All of the data for you question will be stored at ```ComputingBootCamp/website/_data/questions.yml```. Navigate to this file and append your question's info to the end.

See below the list of currently supported question types and examples:

### Multiple Choice

{% highlight yaml %}
- id: 1 # A unique identifier you create used to embed the question
  type: multiple_choice
  help: "Hint: Tool Command Language" # Optional
  prompt: Which scripting language was created first? 
  responses: 
    - text: Python
    - text: Tcl 
      correct: true
    - text: Ruby
{% endhighlight %}

{% include quizzes.html id=1 %}

### Matching

{% highlight yaml %}
- id: 2 # A unique identifier you create used to embed the question
  prompt: Select the most appropriate pairs
  type: matching
  responses: 
    - text: interpreted
      correct: python
    - text: compiled
      correct: c++
    - text: HDL
      correct: System Verilog
{% endhighlight %}

{% include quizzes.html id=2 %}

### Fill in the Blank

Note: The number of underscores in each text field is irrelevant. Responses are not case sensitive

{% highlight yaml %}
- id: 3 # A unique identifier you create used to embed the question
  prompt: Finish the fight song!
  type: fill_in
  responses:
    - text: Rise all loyal Cougars and hurl your _________ to the foe.
      correct: challenge
    - text: You will fight, day or night, rain or ____.
      correct: snow
    - text: _____, strong, and true
      correct: loyal
{% endhighlight %}

{% include quizzes.html id=3 %}

## Embed the Question
Once the question data has been added using the steps above, find the markdown file of the section where you want the question to appear ```ComputingBootcamp/website/_selfpaced/*.md```. Then simply paste the following line where you want the question to appear (be sure to replace the ```id``` value with your id you put in ```questions.yml```):

{% raw %}
```{% include quizzes.html id=1 %}```
{% endraw %}