from pathlib import Path

from invoke import task
from nox.virtualenv import VirtualEnv

DEFAULT_VENV_NAME = 'venv'


@task
def build(c):
    """Build the documentatrion site."""
    mkdocs = mkdocs_bin()
    c.run(f'{mkdocs} build -v -s')


@task
def clean(c):
    """Remove unwanted files and artifacts in this project (!DESTRUCTIVE!)."""
    clean_repo(c)


@task
def clean_repo(c):
    """Remove unwanted files in project (!DESTRUCTIVE!)."""
    c.run('git clean -ffdx')
    c.run('git reset --hard')


@task
def nox(c, s=''):
    """Wrapper for the nox tasks (`inv nox` for details)."""
    if not s:
        c.run('nox --list')
    else:
        c.run(f'nox -s {s}')


@task
def publish(c):
    """Publish the site to github pages."""
    mkdocs = mkdocs_bin()
    c.run(f'{mkdocs} gh-deploy -v --clean')


@task()
def serve(c):
    """Serve the documentation using the development server."""
    mkdocs = mkdocs_bin()
    c.run(f'{mkdocs} serve')


@task(default=True)
def setup(c):
    """Setup the developper environment."""
    c.run('nox --envdir .')


def mkdocs_bin():
    """Find mkdocs binary in default venv."""
    location = Path(DEFAULT_VENV_NAME)
    venv = VirtualEnv(location.resolve())
    venv_bin = Path(venv.bin)
    mkdocs = venv_bin / 'mkdocs'
    return mkdocs
