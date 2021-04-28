# Intro
Why you care about it

How you use it yourself
How you use it with others

Source code control system
    - How do you keep track of versions of my files
    - You've all done this

Worried about overwriting
    - Make a "new" files
    - Make "new2"
    - Awful version of source control

# Let's Begin

    git init
    ls 
    ls -a

Never have to touch .git folder

    git status

## Add Files

    git add ...
    git add ...

    git status

## Ignore Files

 * Create `.gitignore` 
<!-- . -->
    git status
    
## Commit

    git commit
    git log

## Add more

    Add more files 

    git rm
    git rm --cached
    git status
    git log

# Versioning

### Checkout old commit

  * Add new file and commmit
  * Maybe I don't want that
<!-- . -->
    git checkout <hash>

### Make modifications
  * Edit file and commit
<!-- . -->
    git diff


# Branching

  * Create new branch
  * Switch to branch
  * Edit file and commit
  * `cat`, Switch to master, `cat` and switch back

### Merging

    git merge

What branch am I on?

    git branch


# Working With Others

    git clone <github repo>

* New branch
* Modify file
* Git add

(Github knows nothing about this yet)

* git push


