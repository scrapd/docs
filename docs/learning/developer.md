# Developer setup

ScrAPD is written in Python and supports multiple platforms. See the instructions below to setup your ScrAPD development environment in Python on macOS, Linux, and Windows.

## Install the required Python 3 packages
### macOS, Linux, and Windows

You will need to install the Python 3 packages [invoke](https://docs.pyinvoke.org/) and [nox](https://nox.thea.codes/) (see [Installing Python 3](https://docs.scrapd.org/learning/learning) if you don't have Python 3 installed):

`pip3 install --user nox invoke`

Check that the packages were installed:

    inv --list
    nix --list
    
## Setup the local dev environment

Setup a local dev environment (run the commands below in the scrapd folder):
### macOS and Linux

    inv
    source venv/bin/activate

### Windows

    inv
    venv\Scripts\activate

## Run the CI tasks
### MacOS, Linux, and Windows

Run the CI tasks locally:

`inv nox -s ci`

Use `inv --list` and `inv nox` to see all the available targets.

The nox tasks can be invoked by running either:

`inv nox -s {task}`

for instance `inv nox -s test`, or directly with `nox -s test`
