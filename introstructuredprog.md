# Team:

### Luis Fernando Koh Avila:
https://github.com/luiskohavila/programming2
### Matthew Esquivel Brandt:
https://github.com/Git-Mekbot/programming2

# Unit 1: Structured Programming

## Classification of Programming Paradigms

### Programming paradigm:
Are a way to classify programming languages based on their features.

### Declarative

- [Functional](https://www.computerhope.com/jargon/f/functional-programming.htm):
Programming paradigm where programs are constructed by applying and composing functions.

- [Dataflow](https://www.computerhope.com/jargon/d/dataflow-programming.htm):
Programming paradigm that models a program as a directed graph of the data flowing between operations, thus implementing data flow principles and architecture.

- [Logic, Constraint-based](https://www.computerhope.com/jargon/l/logic-programming.htm):
Programming paradigm in which program statements express facts and rules about problems within a system of formal logic.

- Template-based:
Programming paradigm in which programs are constructed by using pre built templates.

- Structured:
Programming paradigm aimed at improving the clarity, quality, and development time of a computer program by making extensive use of the structured control flow constructs of selection and repetition, block structures, and subroutines.

### Imperative

- [Von Neumann](https://www.computerscience.gcse.guru/theory/von-neumann-architecture):
Is based on the stored-program computer concept, where instruction data and program data are stored in the same memory.  This design is still used in most computers produced today.

- [Interpreted (Scripting)](https://www.computerhope.com/jargon/s/script.htm):
Is a computer language with a series of commands within a file that is capable of being executed without being compiled.

- [Object-oriented](https://www.computerhope.com/jargon/o/oop.htm):
It is a programming language paradigm. In an object-oriented program, the code can be structured as reusable components, some of which may share properties or behaviors.

### [Implementation methods](https://www.freecodecamp.org/news/compiled-versus-interpreted-languages/)

Interpreted Programming:
- Directly execute source language program
- Fetch source program, decode it, execute it
- Interpreter executes while program executing

Compiled Programming:
- Translate program from source language to target language
- Program in target language is then executed
- Compiler finished before program executed

## Data Representations and Operators

### [Programming languages](https://javarevisited.blogspot.com/2018/08/5-programming-language-every-programmer-learn.html)
Formal languages, which comprise a set of instructions that produce various kinds of output.
Examples:
- Python
- Java
- C
- JavaScript
- Scala

### [Spaghetti Code](https://www.urbandictionary.com/define.php?term=spaghetti%20code)
It is code which flagrantly violates the principles of structured, procedural programming. Usually this means using lots of GOTO statements hence the term, which suggests the tangled and arbitrary nature of the program flow.

### [Sequential Algorithms](https://www.sciencedirect.com/topics/computer-science/sequential-algorithm)
Algorithm that is executed sequentially once through, from start to finish, without other processing executing as opposed to concurrently or in parallel.

### [Source Code](https://searchapparchitecture.techtarget.com/definition/source-code)
Collection of code, possibly with comments, written using a human-readable programming language, usually as plain text.

### Data Representation in Structured Programming Language

- [Identifiers](http://aboutc.weebly.com/identifiers.html):
An identifier is a string of alphanumeric characters that begins with an alphabetic character or an underscore character that are used to represent various programming elements such as variables, functions, arrays, structures, unions and so on. Actually, an identifier is a user-defined word.

- [Variables](https://www.kidscodecs.com/variables/):
Variables are names used to hold one or more values. Instead of repeating these values in multiple places in your code, the variable holds the results of a calculation, database call, results of a database query, or other value. Instead of multiple calculations or the load of multiple database calls to retrieve the same data, the variable is stored in computer memory once and used wherever it is needed in your code. We cannot use keywords as a name of our variable.

- [Constants](https://press.rebus.community/programmingfundamentals/chapter/constants-and-variables):
A constant is a data item whose value cannot change during the program’s execution. Thus, as its name implies – the value is constant.
Constants are used in two ways. They are:
    - Literal constant
    - Defined constant

|  Language  |                     Example                     |
|:----------:|:-----------------------------------------------:|
|      C     | #define PI 3.1416                               |
|     C#     | const double PI = 3.14159;                      |
|     C++    | #define PI 3.1416 or const double PI = 3.14159; |
|    Java    | const double PI = 3.14159;                      |
| JavaScript | const PI = 3.14159;                             |
|   Python   | PI = 3.14159                                    |

- [Reserved Words](https://www.datamentor.io/r-programming/reserved-words/):
Words that are reserved by a program because the word has a special meaning. Reserved Words can be commands or parameters. Every programming language has a set of keywords that cannot be used as variable names.

- Types of Data:

#### 32 bit computer
| Data type | Size |                          Range                          |
|:---------:|:----:|:-------------------------------------------------------:|
|    char   |   1  |                       -128 to 127                       |
|   short   |   2  |                    -32,768 to 32,767                    |
|    int    |   4  |             -2,147,483,648 to 2,147,483,647             |
|    long   |   4  |             -2,147,483,648 to 2,147,483,647             |
| long long |   8  | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
|   float   |   4  |                       -3.4E +/- 38                      |
|   double  |   8  |                       1.7E +/- 308                      |

#### 64 bit computer
| Data type | Size |                          Range                          |
|:---------:|:----:|:-------------------------------------------------------:|
|    char   |   1  |                       -128 to 127                       |
|   short   |   2  |                    -32,768 to 32,767                    |
|    int    |   4  |             -2,147,483,648 to 2,147,483,647             |
|    long   |   4  | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| long long |   8  | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
|   float   |   4  |                       -3.4E +/- 38                      |
|   double  |   8  |                       1.7E +/- 308                      |


- [Data Type Conversion](https://docs.actian.com/ingres/11.0/index.html#page/EmbedSQL/Data_Type_Conversion.htm):
Data type conversion occurs automatically for different numeric types such as from floating-point database column values into integer C variables, and for character strings, such as from varying-length Ingres character fields into fixed-length C character string buffers.

### Operators of Structured Programming Language

- [Conditional](https://www.dotnettricks.com/learn/c/conditional-statements-if-else-switch-ladder):
Conditional statements help you to make a decision based on certain conditions. These conditions are specified by a set of conditional statements having boolean expressions which are evaluated to a boolean value true or false.

If statement: The single if statement in C language is used to execute the code if a condition is true.
    - If the expression is evaluated to nonzero (true) then if block statement(s) are executed.
    - If the expression is evaluated to zero (false) then Control passes to the next statement following it.

If-Else statement: The if-else statement in C language is used to execute the code if condition is true or false.
    - If the expression is evaluated to nonzero (true) then if block statement(s) are executed.
    - If the expression is evaluated to zero (false) then else block statement(s) are executed.

If-Else If ladder: The if-else-if statement is used to execute one code from multiple conditions. It is a chain of if..else statements in which each if statement is associated with else if statement and last would be an else statement.

Switch statement: Is used to test a list of cases. A switch statement contains one or more case labels which are tested against the switch expression. When the expression matches a case then the associated statements with that case would be executed.

- [Logical](https://press.rebus.community/programmingfundamentals/chapter/logical-operators/):

|  Language  | AND |  OR  | NOT |
|:----------:|:---:|:----:|:---:|
|      C     |  && | \|\| |  !  |
|     C++    |  && | \|\| |  !  |
|     C#     |  && | \|\| |  !  |
|    Java    |  && | \|\| |  !  |
| JavaScript |  && | \|\| |  !  |
|   Python   | and |  or  | not |

#### Logical And(&&)
| x     | y     | x and y |
|:-----:|:-----:|:-------:|
| False | False | False   |
| False | True  | False   |
| True  | False | False   |
| True  | True  | True    |

#### Logical Or(||)
| x     | y     | x or y |
|:-----:|:-----:|:------:|
| False | False | False  |
| False | True  | True   |
| True  | False | True   |
| True  | True  | True   |

#### Logical Not(!)
|   x   | not x |
|:-----:|:-----:|
| False |  True |
|  True | False |

- [Relationship](https://press.rebus.community/programmingfundamentals/chapter/relational-operators/):
An operator that gives a Boolean value by evaluating the relationship between two operands. These include numerical equality and inequalities.

| Operator |          Meaning          |
|:--------:|:-------------------------:|
|     <    |         less than         |
|     >    |        greater than       |
|    <=    |   less than or equal to   |
|    >=    |  greater than or equal to |
|    ==    |    equality (equal to)    |
| != or <> | inequality (not equal to) |

### [Basic Functions of Input & Output](https://www.studytonight.com/c/c-input-output-function.php)
- Input: Input means to provide the program with some data to be used in the program
	- scanf: Save a value specifying the type of data with an %, and them the name of the variable with after an &
	- gets: It is used to get a string
	- puts: Writes the string str and a trailing newline to stdout.

- Output: Output means to display data on screen or write the data to a printer or a file.
	- printf: Function returns the number of characters printed by it

## Version Control

### [Distributed Version Control](https://www.perforce.com/blog/vcs/what-dvcs-anyway)

In software development, distributed version control is a form of version control in which the complete codebase, including its full history, is mirrored on every developer's computer.
- Advantages:
    - Branching and merging can happen automatically and quickly
    - Developers have the ability to work offline
    - Multiple copies of the software eliminate reliance on a single backup
- Most popular types of version control:
    - Helix Core (Perforce)
    - Git
    - SVN
    - ClearCase
    - Mercurial
    - TFS

# Git Basics: Chapter 2

## Getting a Git Repository
<img src="https://practicalseries.com/1002-vcs/01-pages/02-02-concept/02-images/fig-02-01.svg" alt="alt text" width="700" height="500">

**Two ways to get a repository**:
- **Take a local directory and turn it into a Git Repository**:
The first thing is to go to the GitHub page and create a new repository, after putting the name you can decide if you want to initialize the repository with a README or on the other hand you can create it by yourself. You must be in the directory that you want to create the repository and follow the commands given by git.
- **Clone an existing one**:
Get the link from the repository you want to clone in the GitHub page and copy it. After that you must use the following command.
```
git clone <https://github.com/user/nameoftherepository.git>
```
## Recording Changes to the Repository

Once we make and add some files in our repository, we can check the status of these files with the command ```git status```.
![status](https://git-scm.com/book/en/v2/images/lifecycle.png)
### To Track New or Modified Files

When we have a file that was modified or created recently, and we want to add it to our GitHub to make a commit and push it, we use the command ```git add <file>```. 

On the other hand, if you don’t want do add some specific files you can use the command ```.gitignore```

### Differences between git file states

- **Untracked:** is the state where the file has not yet been 'crawled'.
- **Unmodified:** is the state where the file has not changed in relation to your reference.
- **Modified:** is the state where the file has changed relative to your reference.
- **Staged:** is the state where the file has already been addressed and is waiting to be transferred to the repository.

### Committing Your Changes

Steps to make a commit
 ```
 git init
 git add *
 git commit -m "first commit"
 git push -u origin master
 ```
### Removing and Moving Files
- **Removing (Delete):** ```rm PROJECTS.md```
- **Moving (Rename):** ```git mv file_from file_to```

### Viewing the Commit History
You will probably want to look back to see what has happened after you have created several commits. The ```git log``` command allows you to do that. Even if you made commits in different branches these commands show you what are all of them in the command line.

![gitlog](https://desarrolloweb.com/archivoimg/general/4092.png)

### Undoing Things
When you make a commit and you forgot to add a file, or you want to come back to the previous status of the files you can use the command ```git commit –amend```, this command takes your staging area and uses it for the commit. For example:
```
git commit -m 'Initial commit'
git add forgotten_file
git commit --amend
```

### Unstaging a Staged File
If you want to undo a commit that you did accidentally you can use the command revert to delete it. The steps are using the git log command and see the commit that you want to delete, then you must copy the ID and use:
```
git revert <commitID>
```
Git revert directly commits the change but if you want to use git revert and then explicitly commit you can use:
```
git revert -n <commitID>
```

### Working with Remotes
Remote repositories are versions of your project that are hosted on the Internet or network somewhere. You can have several of them, each of which generally is either read-only or read/write for you.

#### - Showing Your Remotes:
To see which remote servers you have configured, you can run the ```git remote``` command. It lists the shortnames of each remote handle you’ve specified.

If you’ve cloned your repository, you should at least see origin. If you specify ```-v```, shows you the URLs that Git has stored for the shortname to be used when reading and writing to that remote

#### - Adding Remote Repositories:
To add a new remote Git repository as a shortname you can reference easily, run:
```
git remote add <shortname> <url>
```
#### - Fetching and Pulling from Your Remotes:
The command ```git fetch <remote>``` goes out to that remote project and pulls down all the data from that remote project that you don’t have yet. The git fetch command only downloads the data to your local repository .

If your current branch is set up to track a remote, you can use the ```git pull``` command to automatically fetch and then merge that remote branch into your current branch.

#### - Pushing to Your Remotes:
To share a project, you have to push it upstream. The command for this is:
```
git push <remote> <branch>.
```
#### -Inspecting a Remote:
If you want to see more information about a particular remote, you can use the ```git remote show <remote>``` command.

#### -Renaming and Removing Remotes:
Renaming: ```git remote rename <old_name> <new_name>``` to change a remote’s shortname.

Removing: ```git remote remove <remote_name>``` or ```git remote rm <remote_name>``` to remove a remote.

### Tagging

**Listing Your Tags:** If you want to list all your existing tags to see them easily you can use the command ```git tag```. 

**Creating Tags:** There are two types of tags:
- Annotated Tags: You must include the -a before choosing the tag name, for example:
```
git tag -a v1.4 -m "my version 1.4"
```
- Lightweight Tags: This is basically the commit checksum stored in a file. To create it, just provide a tag name:
```
git tag v1.4-lw
```

**Deleting Tags:** To delete a tag on your local repository, you can use ```git tag -d <tagname>```.

### Git Aliases

To set up an alias for each command using git config. This is used commonly if  you don’t want to type the entire text of each of the Git commands. Example:
```
git config --global alias.co checkout
```

# Git Basics: Chapter 3

## Branches in a Nutshell

Git stores data as a series of snapshots and saves a commit object that contains a pointer to the snapshot of the content you staged.

When making a commit, git stores the metadata of each file as a separate “blob” and uses a “tree” to list the directories of each blob and what is stored in each, while the commit works as a pointer to the tree.

<img src="https://git-scm.com/book/en/v2/images/commit-and-tree.png" alt="alt text" width="700" height="400">

If you make some changes and commit again, the next commit stores a pointer to the commit that came immediately before it.

![pic2](https://git-scm.com/book/en/v2/images/commits-and-parents.png)

A branch in Git is a movable pointer to one of these commits. The default branch name in Git is master. As you start making commits, you’re given a master branch that points to the last commit you made. Every time you commit, the master branch pointer moves forward automatically.

<img src="https://git-scm.com/book/en/v2/images/branch-and-history.png" alt="alt text" width="550" height="350">

### Creating a New Branch

Creating a new branch makes a new pointer for you to move around.

You can do this by using the ```git branch testing``` to create a branch named “testing”.

<img src="https://git-scm.com/book/en/v2/images/two-branches.png" alt="alt text" width="600" height="250">

Git keeps a special pointer called `HEAD` to know in which branch you are currently on.

The `git branch` command only created a new branch, in this case, it’s still on `master`.

<img src="https://git-scm.com/book/en/v2/images/head-to-master.png" alt="alt text" width="550" height="300">

The `git log` command that shows you where the branch pointers are pointing. This option is called `--decorate`.

To switch to an existing branch, we run the `git checkout` command. This moves `HEAD` to point to the `testing` branch.

<img src="https://git-scm.com/book/en/v2/images/head-to-testing.png" alt="alt text" width="500" height="250">

The `HEAD` branch moves forward when a commit is made. But in this case `master` branch still points to the commit when the run git checkout to switch branches was done.

<img src="https://git-scm.com/book/en/v2/images/advance-testing.png" alt="alt text" width="550" height="230">

By default, `git log` will only show commit history below the branch you’ve checked out. To show all of the branches, add `--all` to your `git log` command.

When moving back to the `master` branch after doing a commit on another branch, this will move the HEAD pointer back, and it reverts the files in the working directory back to the snapshot that master points to.

<img src="https://git-scm.com/book/en/v2/images/checkout-master.png" alt="alt text" width="550" height="230">

NOTE: Switching branches changes files in your working directory

By making changes to the `master` branch now, the project will be diverged. Meaning it is possible to switch back and forth between the branches and merge them together when ready.

<img src="https://git-scm.com/book/en/v2/images/advance-master.png" alt="alt text" width="550" height="300">

Using `git log --oneline --decorate --graph --all` it shows how the history has diverged.

To Create a new branch and switch to it at the same time use `git checkout -b <newbranchname>`

## Basic Branching and Merging

### Basic Branching

<img src="https://git-scm.com/book/en/v2/images/basic-branching-1.png" alt="alt text" width="500" height="135">

NOTE: It’s best to have a clean working state when you switch branches.

To merge branches git uses the command `git merge`

In order to delete a branch use the `git branch -d <branchname>` command

### Basic Merge Conflicts

If you change the same part of the same file differently in the two branches you’re merging, Git won’t be able to merge them cleanly.

These conflicts can look something like this:

```
git merge iss53
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

Here git pauses the process while you resolve the conflict.

To see which files are unmerged at any point after a merge conflict, run `git status`

For example: 
```
<<<<<<< HEAD:index.html
<div id="footer">contact : email.support@github.com</div>
=======
<div id="footer">
 please contact us at support@github.com
</div>
>>>>>>> iss53:index.html
```

This means the version in HEAD (your master branch, because that was what you had checked out when you ran your merge command) is the top part of that block (everything above the =======), while the version in your iss53 branch looks like everything in the bottom part. In order to resolve the conflict, you have to either choose one side or the other or merge the contents yourself. For instance, you might resolve this conflict by replacing the entire block with this:
```
<div id="footer">
please contact us at email.support@github.com
</div>
```
After you’ve resolved each of these sections in each conflicted file, run `git add` on each file to mark it as resolved. Staging the file marks it as resolved in Git.

After you exit the merge tool, Git asks you if the merge was successful. If you tell the script that it was, it stages the file to mark it as resolved for you. You can run git status again to verify that all conflicts have been resolved

Once it verifies everything is correct one can use `git commit` to finalize the merge commit.


## Branch Management

By running the `git branch` command with no arguments it lists current branches.

NOTE: The `*` character that prefixes a branch indicates the branch that it’s currently checked out.

Meanwhile `git branch -v` shows the last commit on each branch.

By using the `--merged` and `--no-merged` options one can filter this list to branches that you have or have not yet merged into the branch you’re currently on.

You cannot simply delete unmerged branches using `git branch -d` unless typing `git branch -D` after.

### Branching Workflows

Git uses a simple three-way merge, merging from one branch into another multiple times over a long period is generally easy to do.

One can have several branches that are always open and that you use for different stages of your development cycle; you can merge regularly from some of them into others.

### Long-Running Branches

There is a certain workflow that many git developers use, and it is as follows:
- The `master` branch is for code that is entirely stable.
- A `develop` branch used to work from or use to test stability.
- A `topic` branch to make sure code passes all the tests and doesn't introduce bugs.

<img src="https://git-scm.com/book/en/v2/images/lr-branches-2.png" alt="alt text" width="550" height="225">

## Remote Branching

Remote references are references (pointers) in your remote repositories, including branches, tags, and so on.

To get a full list of remote references explicitly with `git ls-remote <remote>`, or `git remote show <remote>` for remote branches.

Remote-tracking branches are references to the state of remote branches. They are local references one can’t move, kind of like bookmarks, to remind you where the branches in your remote repositories were the last time you connected to them.

Remote-tracking branch names take the form `<remote>/<branch>`.

When you clone a repository Git’s clone command automatically names it `origin` for you, pulls down all its data, creates a pointer to where its master branch is, and names it origin/master locally. Git also gives you your own local master branch starting at the same place as origin’s master branch, so you have something to work from.

To synchronize work with a given remote, run `git fetch <remote>` . This looks up which server “origin” is, fetches any data from it that you don’t yet have, and updates your local database, moving your origin/master pointer to its new, more up-to-date position.

### Pushing

Local branches aren’t automatically synchronized to the remotes you write to.

You can push up work in the same way you pushed your first branch. Run ```git push <remote> <branch>```

### Tracking Branches

Checking out a local branch from a remote-tracking branch automatically creates what is called a “tracking branch” (and the branch it tracks is called an “upstream branch”).

If you’re on a tracking branch and type `git pull`, Git automatically knows which server to fetch from and which branch to merge in.

When using `--track` it allows you to set up a tracking branch.

To get a totally up to date ahead and behind numbers, you’ll need to fetch from all your remotes right before running this. You could do that like this: ```git fetch --all; git branch -vv```

### Pulling

There is a command called `git pull` which is essentially a `git fetch` immediately followed by a `git merge`.

`git pull` will look up what server and branch your current branch is tracking, fetch from that server and then try to merge in that remote branch.

### Deleting Remote Branches

You can delete a remote branch using the `--delete` option to `git push`.

## Rebasing

### The Basic Rebase

With the `rebase` command, you can take all the changes that were committed on one branch and replay them on a different branch.

Take this for example:

![pic11](https://git-scm.com/book/en/v2/images/basic-rebase-2.png)

This operation works by going to the common ancestor of the two branches, getting the diff introduced by each commit of the branch you’re on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, and finally applying each change in turn.

![pic12](https://git-scm.com/book/en/v2/images/basic-rebase-3.png)

### More Interesting Rebases

You can take the changes on client that aren’t on server (C8 and C9) and replay them on your master branch by using the --onto option of git rebase:

<img src="https://git-scm.com/book/en/v2/images/interesting-rebase-1.png" alt="alt text" width="650" height="350">

This takes the client branch, figures out the patches since it diverged from the server branch, and replays these patches in the client branch as if it was based directly off the master branch instead.

![pic14](https://git-scm.com/book/en/v2/images/interesting-rebase-2.png)

### The Perils of Rebasing

NOTE: Do not rebase commits that exist outside your repository and that people may have based work on.

If you push commits somewhere and others pull them down and base work on them, and then you rewrite those commits with `git rebase` and push them up again, your collaborators will have to re-merge their work and things will get messy when you try to pull their work back into yours.

### Rebase vs. Merge

Both of them are used and it is not simple to decide which is better and mostly depends on the person and situation, in general the way to get the best of both worlds is to rebase local changes you’ve made but haven’t shared yet before you push them in order to clean up your story, but never rebase anything you’ve pushed somewhere.
