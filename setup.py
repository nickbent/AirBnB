from setuptools import setup

NAME = "bnb"
VERSION = "0.1.0"

INSTALL_REQUIRES = [
    "pandas",
    "numpy",
    "torch" ,
]
EXTRAS_REQUIRE = {"test": ["pytest", "mockito"]}

setup(
    name=NAME,
    version=VERSION,
    description="AirBnB Analysis package",
    author_email="nicolas.bent@borealisai.com",
    python_requires=">3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    packages=[NAME],
)
