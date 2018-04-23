# Eclipse IoT-Testware

The Eclipse IoT-Testware project provides testware for the IoT. In addition to test suites for different test types like conformance testing, security testing or performance testing written in [TTCN-3](http://www.ttcn-3.org/), the IoT-Testware provides an infrasturcture to easily test your IoT solutions (under development).

## Getting Started

These instructions will get you a clean IoT-Testware clone up and running on your local machine for development and testing purposes. [//]: # (See deployment for notes on how to deploy the project on a live system.)

### Prerequisites

* Latest version of **Java**
* Latest version of **Python (v2 or v3)**
* Latest version of **Eclipse Titan**. For installation details please consult the official [Titan documentation package](https://projects.eclipse.org/projects/tools.titan/downloads)

### Installing Quickstart

_Note:_ Make sure all prerequisites are met. As we use Eclipse Titan (natively running under Linux) to compile and execute our test suite, the following instruction won't cover other OS like Windows or MacOS. We recommend installing a Linux derivate in a virtual machine. [//]: # (The easiest way is to deploy the whole test system with Docker.)

#### Set up

Firstly, you need to get all needed dependencies to run the test suites. To do so, simply run the python script _install.py_ with your protocol of choice:

```bash
python install.py -p <PROTOCOL>
```

This is the most minimalistic way of getting the dependencies. For a more complete explanation of the installation script please refer to the [documentation](https://github.com/eclipse/iottestware/tree/master/docs/install_script.md).
With Eclipse Titan you are free to choose to work either from the Command Line (CLI) or from Eclipse IDE. Go ahead and read further instructions of your prefered way of working.

##### Terminal

In the _Set up_ section you already set up a clean working directory under ~/Titan by default. The next step would be to generate a Makefile and compile the test suite. You can do that easily with the install script:

```bash
python install.py -p <PROTOCOL> -b
```

##### GUI

In every of our protocol repositories you find a **iottestware.\<PROTOCOL\>.tpd** file that you need to import.
Open the Titan IDE in your desired workspace and use the import feature 
```
File -> Import -> TITAN -> Project from .tpd file
```

<img alt="Import from .tpd file" src="https://user-images.githubusercontent.com/2487708/33207536-56f3f9fc-d10e-11e7-9699-7298ee842a6b.png" width="477">


Klick Next and choose the **iottestware.\<PROTOCOL\>.tpd** from **${PATH_BASE}**

<img alt="Create TITAN Project" src="https://user-images.githubusercontent.com/2487708/33207748-26bf29e0-d10f-11e7-84f3-0b79bddb6fd5.png" width="477">


Klick Next and choose importation options.

<img alt="Importation Options" src="https://user-images.githubusercontent.com/2487708/33207865-aa9ef434-d10f-11e7-8b3e-08ac1d607a96.png" width="477">


Klick Finish and the IDE will import all the required Projects and open the properties for each. Make sure each project is configured to **_generate Makefile for use with the function test runtime_**.

<img alt="Makefile for FTR" src="https://user-images.githubusercontent.com/2487708/33207905-d6019bcc-d10f-11e7-965b-23e0a73b3e3c.png" width="477">


Right-click the **iottestware.\<PROTOCOL\>** project and select **Build Project**. 

<img alt="Build Project" src="https://user-images.githubusercontent.com/2487708/33208541-4135a706-d112-11e7-8cc1-a6ed63bc4f92.png" width="477">
_Note:_ Make sure you are in the TITAN Editing Perspective, otherwise the Build Project might be not available. 

## Built With

* [Eclipse Titan](https://projects.eclipse.org/projects/tools.titan) - TTCN-3 Runtime
* [GNU Make](https://www.gnu.org/software/make/) - Build automation

## Authors

* **Alexander Kaiser** - *Initial work* - [relayr](https://relayr.io/)
* **Sascha Hackel** - *Initial work* - [Fraunhofer FOKUS](https://www.fokus.fraunhofer.de/)
* **Axel Rennoch** - *Initial work* - [Fraunhofer FOKUS](https://www.fokus.fraunhofer.de/)

## License

[Eclipse Public License 1.0 (EPL-1.0)](https://opensource.org/licenses/EPL-1.0)

