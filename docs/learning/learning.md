# Learning resources

Sometimes people are afraid to tackle a task or join a project because they think they do not have the appropriate
knowledge. While it might sometimes be true, we, at Scrapd, consider our projects as the best opportunity to
learn! And to make it easier for you to learn the ropes, we compiled the best resources!

## Beginners

Let's start with the fundamentals!

### Terminal

The __"Really friendly intro to the command line"__ is a must read/watch for beginners! While targeted for Mac users,
it may help others as well. It comes with a nice illustrated support and a video.
<https://hellowebbooks.com/learn-command-line>

Enjoy this online class which will demistify the terminal in just 40 minutes!  <https://www.udemy.com/command-line>

An interactive tutorial that will reconcile you with the terminal.
<https://linuxsurvival.com/linux-tutorial-introduction>


A tutorial dividded in 13 sections to bring you from newbie to moderate wizard.
<https://ryanstutorials.net/linuxtutorial>

### Git/GitHub

Learn git and GitHub using the __GitHub Learning Lab__. <https://try.github.io>

__Become a git guru__ with Atlassian. <https://www.atlassian.com/git/tutorials>

### Installing Python 3 on Windows 10

Although you can use [Anaconda](https://www.anaconda.com) to install Python, if you want to develop with Python we suggest to bypasss Anaconda and install Python directly as shown below.

1. Open a browser window and navigate to the download page for Windows at python.org.
2. Click on the link for the Latest Python 3 Release - Python 3.x.x. (as of this writing, the latest is Python 3.7.3).
3. Select either the Windows x86-64 executable installer for 64-bit or the Windows x86 executable installer for 32-bit. Download and run the installer (**Important**: Check the 'Add Python 3.x to PATH' box to ensure that the interpreter will be placed in your execution path).
4. Test if Python was installed correctly by opening a command window and typing `python –-version`. If you see the message `python is not recognized as an internal or external command, operable program or batch file`, you need to add Python to you PATH environment variable.
5. (**Optional**) To add Python to the PATH environment variable:
    * Navigate to Control Panel/System Properties. In the 'Advanced' tab, click on 'Environment Variables'.
    * Select ‘Path’ in ‘User variables’ and click 'Edit...'. Click on 'New' and add the following paths
        * C:\Users\\**YourUsername**\AppData\Local\Programs\Python\Python37\Scripts
        * C:\Users\\**YourUsername**\AppData\Local\Programs\Python\Python37\
        * C:\Users\\**YourUsername**\AppData\Roaming\Python\Python37\Scripts
    * Re-test if Python has been added to your PATH.

Chances are, you will want to use Python for more than contributing to this project. If that is the case, type the commands below to install packages in the SciPy Ecosystem for Python 3 on Windows 10

1. `python -m pip install --user numpy scipy matplotlib ipython jupyter pandas`
2. Test that the packages were installed by importing them in the Python interpreter.
    * If the matplotlib import fails with 'ImportError: DLL load failed: The specified module could not be found', install Microsoft’s Visual C++ Redistributable for Visual Studio 2015 (see [matplotlib issues](https://github.com/matplotlib/matplotlib/issues/14322) for more details).
3. `python -m pip install --user spyder`

## Intermediate

Now that you leveled up, let's bring some fun!

### Python

Completely new to Python? Let __Real Python__ help you learn everything about it.
<https://realpython.com/start-here/>

From zero to Hero with __Dive Into Python 3__. This book covers all the facets of python, from writing a simple program,
to using REST APIs, via unit tests. <http://getpython3.com/diveintopython3/>

__The Hitchhiker’s Guide to Python!__ is also a classic. An opiniated handbook which aims at making you a python expert.
<https://docs.python-guide.org/>

### Kubernetes

A bed time story to learn kubernetes: [The illustrated childrens guide to Kubernetes](https://cdn.chrisshort.net/The-Illustrated-Childrens-Guide-to-Kubernetes.pdf).

## Advanced

 _"I'm here to serve you master."_
 
### Python
 
#### Refactoring
 
At some point, your application will grow and you will need to trim a little. When time comes, this [refactoring guide](https://realpython.com/python-refactoring/) will prove handy.
 
#### Anti-patterns

A small book of [Python anti-patterns and worst practices](https://docs.quantifiedcode.com/python-anti-patterns/). Learn them to avoid them!
