from setuptools import find_packages, setup

"""
THIS IS A STUB FOR RUNNING THE APP
"""

setup(
    name="eth2deposit",
    version='1.2.6',
    py_modules=["eth2deposit"],
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires=">=3.7,<4",
)
