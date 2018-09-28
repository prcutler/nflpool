import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.txt")) as f:
    README = f.read()
with open(os.path.join(here, "CHANGES.txt")) as f:
    CHANGES = f.read()

requires = [
    "pyramid",
    "pyramid_chameleon",
    "pyramid_debugtoolbar",
    "pyramid_handlers",
    "sqlalchemy",
    "waitress",
    "pendulum",
    "requests",
    "mailer",
    "html2text",
    "passlib",
    "rollbar",
    "sphinx",
    "sphinx-autobuild",
    "sphinx_rtd_theme",
    "logbook",
]

tests_require = ["WebTest >= 1.3.1", "pytest", "pytest-cov"]  # py3 compat

setup(
    name="nflpool",
    version="2.0",
    description="nflpool",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="Paul Cutler",
    author_email="paul.r.cutler@gmail.com",
    url="",
    keywords="web pyramid pylons nfl nflpool",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={"testing": tests_require},
    install_requires=requires,
    entry_points={"paste.app_factory": ["main = nflpool:main"]},
)
