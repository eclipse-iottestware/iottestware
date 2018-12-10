################
Quickstart Guide
################

The easiest way to get started is to use Docker.
The provided Dockerfile hides the complexity of TTCN-3 from the user. Therefore the user has more time to test his systems.

Prerequisites
=============
* `Docker Container Platform <https://www.docker.com/>`_

Build Docker
============
First, we define some default values.

.. code-block:: bash

  TESTWARE=iot_testware

1. Build the Docker image

.. code-block:: bash

  docker build -t TESTWARE .

2. Start the Docker container

.. code-block:: bash

  docker run -ti TESTWARE /bin/bash

Run Test Campaigns
==================
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

3. (optional) To change SUT you must change the ``hostName`` definition within the definition with the ``id := "mqtt_server"``

4. Run the whole test campaign

.. code-block:: bash

  ttcn3_start iottestware.mqtt BasicConfig.cfg

4.1 Run a single test case

.. code-block:: bash

  ttcn3_start iottestware.mqtt BasicConfig.cfg MQTT_TestCases.TC_MQTT_BROKER_CONNECT_001
