# Developer setup

ScrAPD is written in Python and supports multiple platforms. See the instructions below to setup your ScrAPD development environment in Python on macOS, Windows, and Linux.

## macOS

You will need to install the Python 3 packages [invoke](https://docs.pyinvoke.org/) and [nox](https://nox.thea.codes/) (see [Installing Python 3](https://docs.scrapd.org/learning/learning) if you don't have Python 3 installed):

`pip3 install --user nox invoke`

Check that the packages were installed:

    inv --list
    nix --list

Setup a local dev environment:

    inv
    source venv/bin/activate

Run the CI tasks locally:

`inv nox -s ci`

Use `inv --list` and `inv nox` to see all the available targets.

The nox tasks can be invoked by running either:

`inv nox -s {task}`

for instance `inv nox -s test`, or directly with `nox -s test`

## Windows

You will need to install the Python 3 packages [invoke](https://docs.pyinvoke.org/) and [nox](https://nox.thea.codes/) (see [Installing Python 3](https://docs.scrapd.org/learning/learning) if you don't have Python 3 installed):

`pip3 install --user nox invoke`

Check that the packages were installed:

    inv --list
    nox --list

Setup a local dev environment (run the commands below in the docs folder):

    inv
    venv\Scripts\activate

Run the CI tasks locally:

`inv nox -s ci`

Use `inv --list` and `inv nox` to see all the available targets.

The nox tasks can be invoked by running either:

`inv nox -s {task}`

for instance `inv nox -s test`, or directly with `nox -s test`

## Linux

You will need to install the Python 3 packages [invoke](https://docs.pyinvoke.org/) and [nox](https://nox.thea.codes/) (see [Installing Python 3](https://docs.scrapd.org/learning/learning) if you don't have Python 3 installed):

`pip3 install --user nox invoke`

Check that the packages were installed:

    inv --list
    nix --list

Setup a local dev environment:

    inv
    source venv/bin/activate

Run the CI tasks locally:

`inv nox -s ci`

Use `inv --list` and `inv nox` to see all the available targets.

The nox tasks can be invoked by running either:

`inv nox -s {task}`

for instance `inv nox -s test`, or directly with `nox -s test`
