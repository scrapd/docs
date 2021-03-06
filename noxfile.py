import nox

# Behavior's options.
nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["venv"]


@nox.session()
def venv(session):
    """Setup the developper environment."""
    session.install("--upgrade", "pip", "setuptools")
    session.install("-r", "requirements.txt")
