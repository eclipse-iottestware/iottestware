================
Quickstart Guide
================

The easiest way to get started is to use Docker.
The provided Dockerfile hides the complexity of TTCN-3 from the user. Therefore the user has more time to test his systems.

Preparations
------------
* Make sure you have a working `Docker <https://www.docker.com/>`_ installation

* (optional) Set the following environment variables

  .. code-block:: bash

    TESTWARE=iot_testware


Dashboard
---------
The easiest way to get started with the Eclipse IoT-Testware is to use the Dashboard Docker image.

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

CLI
---
If you are already familiar with concepts and the CLI of `Eclipse Titan <https://projects.eclipse.org/projects/tools.titan>`_ than this way is a light-weight solution to run the Testware without webserver and dashboard.

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
Fortunately, we already have all the components in Docker. Let's see how we can run some conformance tests against your System Under Test (SUT).

1. Change directory to the MQTT playground and make yourself familiar with the provided files.

  .. code-block:: bash

    cd /home/titan/playground/mqtt; ls

2. (optional) By default, the public MQTT Broker ``iot.eclipse.org`` is set. If you want to change the configuration follow the instructions.

  .. code-block:: bash

    vi ./BasicConfig.cfg

3. (optional) To configure the TS for your SUT you can change the ``hostName``, ``portNumber`` and ``credentials`` definitions.

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

4.1 Run the whole test campaign given in ``BasicConfig.cfg``

  .. code-block:: bash

    ttcn3_start iottestware.mqtt BasicConfig.cfg

4.2 Run a single test case ``TC_MQTT_BROKER_CONNECT_001`` from ``MQTT_TestCases``

  .. code-block:: bash

    ttcn3_start iottestware.mqtt BasicConfig.cfg MQTT_TestCases.TC_MQTT_BROKER_CONNECT_001

Manual Installation
-------------------
The IoT-Testware is composed of several test suites from different repositories with once again several dependencies to the
Eclipse TITAN runtime. Hence, the installation process can become quite complex. Therefore we provide several 'flavours' of installation.

.. toctree::
   :maxdepth: 2
   :caption: Installation options:

   install_script.rst
   install_ide.rst
   install_docker.rst
