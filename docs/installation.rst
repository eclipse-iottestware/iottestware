==============
Installation
==============

Target Environment
------------------

It is possible to install and run (parts of) the IoT-Testware in at least three different ways:

* Dashboard_
* CLI_
* Manual_

For each of the mentioned possibilities exists different requirements for the environment to be set up. Please consider your favorite way of using the IoT-Testware and make sure you fullfill all requirements.

.. _Dashboard:

Dashboard
---------
Preparation
##################
* Make sure you have a working `Git installation <https://git-scm.com/>`_

* Make sure you have a working `Docker installation <https://www.docker.com/>`_

* (optional) Set the following environment variables

  .. code-block:: bash

    TESTWARE=iot_testware

Installation
##################
1. Clone the IoT-Testware Dashboard project

  .. code-block:: bash

    git clone https://github.com/eclipse/iottestware.dashboard
    cd iottestware.dashboard

2. Build the Docker image

  .. code-block:: bash

    docker build -t $TESTWARE .

3. Start the Docker container

  .. code-block:: bash

    docker run --network=host -ti $TESTWARE

4. Call the Dashboard in your browser from ``https://localhost:3001``

.. _CLI:

Dockerized Command Line
-----------------------
If you are already familiar with concepts and the CLI of `Eclipse Titan <https://projects.eclipse.org/projects/tools.titan>`_ than this way is a light-weight solution to run the Testware without webserver and dashboard.

Preparation
##################

* Make sure you have a working `Git installation <https://git-scm.com/>`_

* Make sure you have a working `Docker installation <https://www.docker.com/>`_

Installation
##################
1. Clone the main IoT-Testware project

  .. code-block:: bash

    git clone https://github.com/eclipse/iottestware
    cd iottestware

2. Build the Docker image

  .. code-block:: bash

    docker build -t TESTWARE .

3. Start the Docker container

  .. code-block:: bash

    docker run -ti TESTWARE /bin/bash

Run Test Campaigns
##################
The IoT-Testware Docker image ships currently two test suites for MQTT and CoAP. We will show you quickly how to configure and run the
test suites.

Starting test suites with TITAN

.. code-block:: bash

  ttcn3_start [-ip host_ip_address] executable [file.cfg] {module_name[.testcase_name]}

Looks quite easy: in order to start a test campaign TITAN requires us to provide an **executable** test suite.
As we want also be able to provide different kinds of configurations, we also need to provide a **.cfg** file.
Fortunately, we already have all the components in Docker. Let's see how we can run some MQTT conformance tests against your System Under Test (SUT).

1. Change directory to the MQTT playground and make yourself familiar with the provided files.

  .. code-block:: bash

    cd /home/titan/playground/mqtt; ls

By default, the public MQTT Broker ``iot.eclipse.org`` is preconfigured in the provided configuration file.
If you want to change the default configuration follow the next instructions.

1.1 (optional) get started with your own configuration

  .. code-block:: bash

    cp BasicConfig.cfg YOUR_CONFIG.cfg
    vi YOUR_CONFIG.cfg

1.2 (optional) to configure the TS (Test System) for your SUT you can change the ``hostName``, ``portNumber`` and ``credentials`` definitions.

  .. code-block:: guess
    :emphasize-lines: 5,6,13-16

    tsp_addresses :=
    {
      {
        id := "mqtt_server",
        hostName := "iot.eclipse.org",
        portNumber := 1883
      }, {
        id := "mqtt_client",
        hostName := "0.0.0.0",
        portNumber := 45679,
        credentials :=
        {
          clientId := "CLIENT_ID",
          username := "USER_NAME",
          password := "PASSWORD",
          topicName := "your/mqtt/topic/name"
        }
      }
    }

1.3 (optional) put together your own test campaing by choosing test cases from the ``[EXECUTE]`` section.

  .. note::
    The configuration file can contain any white space characters. There are three ways to put
    comments in the file: you can use the C comment delimiters (i.e. /* and */). Additionally, characters
    beginning with # or // are treated as comments until the end of line.


  .. code-block:: guess
    :emphasize-lines: 1,3,4

    [EXECUTE]
    ### CONNECT Control Packet
    MQTT_TestCases.TC_MQTT_BROKER_CONNECT_001   # <- will execute
    MQTT_TestCases.TC_MQTT_BROKER_CONNECT_002   # <- will execute
    #MQTT_TestCases.TC_MQTT_BROKER_CONNECT_003  # <- won't execute
    ...

2.1 Run the whole test campaign given in ``YOUR_CONFIG.cfg``

  .. code-block:: bash

    ttcn3_start iottestware.mqtt YOUR_CONFIG.cfg

2.2 (alternative) Run a single test case ``TC_MQTT_BROKER_CONNECT_001`` from ``MQTT_TestCases``

  .. code-block:: bash

    ttcn3_start iottestware.mqtt YOUR_CONFIG.cfg MQTT_TestCases.TC_MQTT_BROKER_CONNECT_001

.. _Manual:

Manual Installation
-------------------
The IoT-Testware is composed of several test suites from different repositories with once again several dependencies to the
**Eclipse Titan** runtime. Hence, the process for a native installation can become quite complex.
However, a native installation is very helpful for development. Therefore we provide additional 'flavours' of installation for development purposes.

* We highly recommend to consider the `Titan installation guide <https://projects.eclipse.org/projects/tools.titan/downloads>`_ to set up Titan properly (check the supported OS ons the side beforehand).

* If you are not using one of the supported OS, we recommend to set up a virtual machine or use Titan with Docker.

.. toctree::
   :maxdepth: 2
   :caption: Installation options:

   install_script.rst
   install_ide.rst
   install_docker.rst
