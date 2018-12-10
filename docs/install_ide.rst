########################
Install with Eclipse IDE
########################

These instructions will get you a clean IoT-Testware clone up and running on your local machine for development and testing purposes.

Prerequisites
=============
* Latest version of **Java**
* Latest version of **Python (v2 or v3)**
* Latest version of **Eclipse Titan**. For installation details please consult the official `Eclipse Titan <https://projects.eclipse.org/projects/tools.titan/downloads>`_

Installing Quickstart
=====================

*Note:* Make sure all prerequisites are met. As we use Eclipse Titan (natively running under Linux) to compile and execute our test suite, the following instruction won't cover other OS like Windows or MacOS. We recommend installing a Linux derivate in a virtual machine.

Set up
======
Firstly, you need to get all needed dependencies to run the test suites. To do so, simply run the python script ``install.py`` with your protocol of choice:

.. code-block:: bash

  python install.py -p <PROTOCOL>


This is the most minimalistic way of getting the dependencies. For a more complete explanation of the installation script please refer to the documentation.
With Eclipse Titan you are free to choose to work either from the Command Line (CLI) or from Eclipse IDE. Go ahead and read further instructions of your preferred way of working.


Eclipse IDE
===========

In every of our protocol repositories you find a **iottestware.\<PROTOCOL\>.tpd** file that you need to import.
Open the Titan IDE in your desired workspace and use the import feature
``File -> Import -> TITAN -> Project from .tpd file``

.. image:: https://user-images.githubusercontent.com/2487708/33207536-56f3f9fc-d10e-11e7-9699-7298ee842a6b.png
    :width: 500px
    :alt: Import from .tpd file
    :align: center

Klick Next and choose the **iottestware.\<PROTOCOL\>.tpd** from **${PATH_BASE}**

.. image:: https://user-images.githubusercontent.com/2487708/33207748-26bf29e0-d10f-11e7-84f3-0b79bddb6fd5.png
    :width: 500px
    :alt: Create TITAN Project
    :align: center

Klick Next and choose importation options.

.. image:: https://user-images.githubusercontent.com/2487708/33207865-aa9ef434-d10f-11e7-8b3e-08ac1d607a96.png
    :width: 500px
    :alt: Import options
    :align: center

Klick Finish and the IDE will import all the required Projects and open the properties for each. Make sure each project is configured to **_generate Makefile for use with the function test runtime_**.

.. image:: https://user-images.githubusercontent.com/2487708/33207905-d6019bcc-d10f-11e7-965b-23e0a73b3e3c.png
    :width: 500px
    :alt: Makefile for function test runtime
    :align: center

Right-click the **iottestware.\<PROTOCOL\>** project and select **Build Project**.

.. image:: https://user-images.githubusercontent.com/2487708/33208541-4135a706-d112-11e7-8cc1-a6ed63bc4f92.png
    :width: 500px
    :alt: Build project
    :align: center

*Note:* Make sure you are in the TITAN Editing Perspective, otherwise the Build Project might be not available.
