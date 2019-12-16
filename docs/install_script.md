# IoT-Testware installation script documentation
Great that you considering the IoT-Testware to test your implementations. We would like to guide you to start with our test suites.
As you might found out, the easiest way to start is the [IoT-Testware installation script](https://github.com/eclipse/iottestware/blob/master/install.py).

This documentation helps you to understand the script.

## The **_help_** command
You can refer to the help command if you don't know how to continue at any point.
Simply run one the following command:

``` python install.py -h ```  
``` python install.py --help ```

The result gives you a first idea, what is possible with the script. The output looks like this:

```bash
-h, --help            show this help message and exit
-p {mqtt,coap,opcua}, --protocol {mqtt,coap,opcua}
                      sets a protocol that will be cloned together with its
                      dependencies
-b, --build           build the project and create a Makefile
--path PATH           specify optionally your root directory, where all
                      dependencies will be stored
-e EXECUTABLE_NAME, --executable_name EXECUTABLE_NAME
                      set the name of the executable that will be generated
-v, --verbose         progress status output is verbose
```

## The **_protocol_** command
The protocol command is the a **mandatory** flag. It will scan your working directory to check whether all dependencies are met. In case there is something missing, the script will download the missing dependencies automatically.  
The command demands a parameter representing the interesting protocol.

Let's assume you would like to run tests against a CoAP implementation. Run one of the following command to get the CoAP conformance test suite and all it's dependencies:

```
python install.py -p coap
python install.py --protocol coap
```

Use the same procedure for any available protocol.

## The **_build_** command
This optional command can be used to build the IoT-Tesware. It builds a ```Makefile``` first and creates an executable afterwards. You can only build one protocol at a time. It is determined by the [protocol command](https://github.com/eclipse/iottestware/tree/master/docs/install_script.md#the-protocol-command).
To build the MQTT test suite for example, run one of the following commands:

```
python install.py -p coap -b
python install.py -p coap --build
```

## The **_path_** command
When you run the install script, it creates a folder structure under ```~/Titan``` by default. This is your base directory where the IoT-Testware and all it's dependencies are stored:
* **IoT-Testware**  
  You find the test suites for the protocols you have chosen via the ```protocol``` command. It creates a folder for every protocol separately in the form of ```iottestware.<PROTOCOL>```
* **Libraries**  
  Collection of libraries needed for the specific IoT-Testware protocol.
* **ProtocolModules**  
  The protocol modules, provided by [Eclipse Titan](https://projects.eclipse.org/projects/tools.titan/developer), are included inside this directory. The subset of protocol modules are protocol dependent. They define the protocol types.
* **TestPorts**  
  To bridge the gap between the test suite and the system under test (SUT), test ports are needed. They are provided by [Eclipse Titan](https://projects.eclipse.org/projects/tools.titan/developer) project.

## The **_executable_** command
With this command it is possible to name the executable that is generated when calling the [build command](https://github.com/eclipse/iottestware/tree/master/docs/install_script.md#the-build-command). In contrast, the install script chose a default name for the executable following the scheme:  

```
iottestware_<PROTOCOL>
```

To set your own name for the resulting executable, let's say "myExecutable" simply run one of this command:

```
python install.py -p coap -e myExecutable  
python install.py -p coap --executable_name myExecutable
```

## The **_verbose_** command
If you set this command, the console output will be verbose and give you more information during the process. By default, the output is quite, meaning only important messages are shown.  
To switch the verbose output on, you add either ``` -v ``` or ``` --verbose ``` to your command like in the following examples:

```
python install.py -p coap --verbose -e myExecutable  
python install.py -p coap -b -v
python install.py --verbose --protocol coap
```
