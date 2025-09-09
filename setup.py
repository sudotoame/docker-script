from setuptools import setup, find_packages

with open("requirements.txt") as file:
    requirements = file.read().splitlines()

setup(
    name="docker-scripts",
    version="0.1.0",
    packages=find_packages(include=["modules", "modules.*"]),
    install_requires=requirements,
    author="yukitoame",
    author_email="devops@yukitoame.ru",
    description="scripts for docker",
)
