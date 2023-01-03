from setuptools import setup, find_packages

version_of_project = open('../VERSION', 'r').read() #Return version from VERSION file

setup(name = 'tikbot',
    packages = find_packages(),
    version=version_of_project,
    package_data={'app':['**']},
    author='Robson J'
)