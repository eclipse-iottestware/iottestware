##########
install.py
##########

.. |titan| raw:: html

   <a href="https://projects.eclipse.org/projects/tools.titan" target="_blank">Eclipse Titan</a>

.. |titan_downloads| raw:: html

   <a href="https://projects.eclipse.org/projects/tools.titan/downloads" target="_blank">downloads</a>

.. |titan_dev_resources| raw:: html

   <a href="https://projects.eclipse.org/projects/tools.titan/developer" target="_blank">developer resources</a>

.. |python| raw:: html

   <a href="https://www.python.org/downloads/" target="_blank">Python</a>

This documentation helps you to understand and use the `install.py <https://github.com/eclipse/iottestware/blob/master/install.py>`_ script.

Prerequisites
=============
* Latest version of |python|
* Latest version of |titan|. For installation details please consult the official |titan_downloads|

help command
============
You can refer to the help command if you don't know how to continue at any point.
Simply run one the following command:

.. code-block:: bash

  python install.py -h
  python install.py --help

The result gives you a first idea, what is possible with the script. The output looks like this:

-h                  show this help message and exit
-p PROTO            available protocol test suites are {mqtt, coap, opcua}
                    sets a protocol that will be cloned together with its
                    dependencies
-b                  build the project and create a Makefile
--path PATH         specify optionally your root directory, where all
                    dependencies will be stored
-e NAME             set the name of the executable that will be generated
-v                  progress status output is verbose


protocol command
================
The protocol command is the a **mandatory** flag. It will scan your working directory to check whether all dependencies are met. In case there is something missing, the script will download the missing dependencies automatically.
The command demands a parameter representing the interesting protocol.

Let's assume you would like to run tests against a CoAP implementation. Run one of the following command to get the CoAP conformance test suite and all it's dependencies:

.. code-block:: bash

  python install.py -p coap
  python install.py --protocol coap


Use the same procedure for any available protocol.

build command
=============
This optional command can be used to build the IoT-Tesware. It builds a *Makefile* first and creates an executable afterwards. You can only build one protocol at a time. It is determined by the `protocol command`_.
To build the CoAP test suite for example, run one of the following commands:

.. code-block:: bash

  python install.py -p coap -b
  python install.py -p coap --build


path command
============
When you run the install script, it creates a folder structure under ``~/Titan`` by default. This is your base directory where the IoT-Testware and all it's dependencies are stored:

**IoT-Testware**
You find the test suites for the protocols you have chosen via the ``protocol`` command. It creates a folder for every protocol separately in the form of ``iottestware.<PROTOCOL>``

**Libraries**
Collection of libraries needed for the specific IoT-Testware protocol.

**ProtocolModules**
The protocol modules, provided in |titan_dev_resources|, are included inside this directory. The subset of protocol modules are protocol dependent. They define the protocol types.

**TestPorts**
To bridge the gap between the test suite and the system under test (SUT), test ports are needed. They are provided by `Eclipse Titan <https://projects.eclipse.org/projects/tools.titan/developer>`_ project.

executable command
==================
With this command it is possible to name the executable that is generated when calling the `build command`_. In contrast, the install script chose a default name for the executable following the scheme:

``iottestware.<PROTOCOL>``

To set your own name for the resulting executable, let's say "myExecutable" simply run one of this command:

.. code-block:: bash

  python install.py -p coap -e myExecutable
  python install.py -p coap --executable_name myExecutable


verbose command
===============
If you set this command, the console output will be verbose and give you more information during the process. By default, the output is quite, meaning only important messages are shown.
To switch the verbose output on, you add either `` -v `` or `` --verbose `` to your command like in the following examples:

.. code-block:: bash

  python install.py -p coap --verbose -e myExecutable
  python install.py -p coap -b -v
  python install.py --verbose --protocol coap
