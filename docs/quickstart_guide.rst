================
Quickstart Guide
================

The easiest way to get started is to use `Docker <https://www.docker.com/>`_.
The provided Dockerfile hides the complexity of TTCN-3 from the user. Therefore the user has more time to test his systems.

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
