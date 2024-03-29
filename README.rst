Table of Contents
=================

1. `General`_

2. `Specifications`_

3. `Installation and deployment`_

4. `Usage`_


General
========
This program is a home assignment of ControlUp.
It demonstrates testing related abilities of an API provided by the WeatherApi site
using Python with Pytest testing framework


Specifications
===============
The assignment has it's own specification described in the "Home Assignment.txt" document

Installation and deployment
===========================

1. Open a command line on your machine (verify git installation) and run the following:
    git clone https://github.com/zeevschneider/ControlUp.git

2. Make sure that you have a machine with Python >= 3.6 installed

3. Open a command line and cd to the /ControlUp folder in the downloaded package

4. The best way is to install requirements into a virtual environment in order not to soil
    your python with unnecessary packages:
    a. Follow the instructions:
        for Windows - https://programwithus.com/learn/python/pip-virtualenv-windows
        for Mac - https://programwithus.com/learn/python/pip-virtualenv-mac
    b. Run the following command to install packages that are listed in the requirements.txt file:
       pip install -r requirements.txt

Usage
======
Run tests:
    CD to {your virtual env}/ControlUp/control_up_tests and type "pytest"
