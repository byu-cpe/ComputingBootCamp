---
layout: page
toc: true
title: Markdown
slug: markdown
type: setup
order: 5
---

Markdown is useful for taking notes and is frequently used in GitHub repositories for the `README.md` and other descriptive pages.

## Basics

```
This is how you make words **bold** 
and other words *italic* with Markdown. 
And this is how you make a [link to Google!](http://google.com)
```
This is how you make words **bold** 
and other words *italic* with Markdown. 
And this is how you make a [link to Google!](http://google.com)

***

## Headers
```
## This is an \<h2> tag
### This is an \<h3> tag
#### This is an \<h4> tag
this is normal text
```
## This is an \<h2> tag
### This is an \<h3> tag
#### This is an \<h4> tag
this is normal text

***

## Lists
### Unordered
```
* Item 1
* Item 2
  * Item 2a
  * Item 2b
* Item 3
```
* Item 1
* Item 2
  * Item 2a
  * Item 2b
* Item 3

### Ordered
```
1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b
1. Item 4
```
1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b
1. Item 4

***

## Links
```
http://github.com - automatic!
[GitHub](http://github.com)
```
http://github.com - automatic!
[GitHub](http://github.com)

***

## Blockquotes
```
As George Washington said:
> Knowledge is in every country
> the surest basis of public happiness
```
As George Washington said:
> Knowledge is in every country
> the surest basis of public happiness

***

## Inline code
```
I think you should use an
`<addr>` element here instead.
```
I think you should use an
`<addr>` element here instead.

***

## Other Markdown Features

***

### Syntax Highlighting

```
```python
def foo():
    if not bar:
        return True
``
```
Open and close a long comment with ` ``` `
```python
def foo():
    if not bar:
        return True
```

***

### Tables
Tables are super super handy!!
```
Header 1 | Header 2
-------- | --------
Content from cell 1 | Content from cell 2
Data     | More Data
```
Header 1 | Header 2
-------- | --------
Content from cell 1 | Content from cell 2
Data     | More Data

***

### Task Lists
```
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item
```
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

***

### Strikethrough
Strikethrough
Any word wrapped with two tildes (like `~~this~~`) will appear crossed out.
```
I want to go ~~home~~ to the park.
```
I want to go ~~home~~ to the park.

***

### Images
Images are similar to links to other pages, but with an `!` in front, and a link to the location of your image.

On your Jekyll website, you'll want to use the format below instead.

```
<img src = "{% link media/Basys-3.png %}" width="600">
```
<img src = "{% link media/Basys-3.png %}" width="600">

***

To work with Markdown from within VS Code, download the `Github Markdown Preview` Extension. 

Then you can click the `Open Preview to the Side` Icon on the top right of the editing window to open the preview of the Markdown you have open.

Use `bundle exec jekyll serve` to see what the page will actually look like on a jekyll server. 
