# Installing Python 3 on Windows 10

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