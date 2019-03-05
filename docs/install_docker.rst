###################
Install with Docker
###################
For an easy deployment, you can use the shipped Dockerfile coming with the repository.

Docker is a computer program that performs `operating-system-level virtualization <https://en.wikipedia.org/wiki/Operating-system-level_virtualization>`_.
It uses the resource isolation features of the Linux kernel to allow independent containers to run within a single Linux instance, avoiding the overhead of staring and maintaining virtual machines.

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Docker-linux-interfaces.svg/440px-Docker-linux-interfaces.svg.png
   :width: 350px
   :alt: linux-interfaces
   :align: center

`Docker <https://www.docker.com/>`_ will perform all the heavy lifting of virtualization and running the IoT-Testware including Eclipse Titan.
Therefore, an installed and functioning Docker is the only prerequisite.

.. note:: Although, it is possible to run Docker containers on different operating systems, Docker is primarily developed for Linux. Hence, it is recommended to run the Docker containers on a Linux machine.

Preparations
============
* Make sure you have a working `Docker <https://www.docker.com/>`_ installation

* (optional) Set the following environment variables

  .. code-block:: bash

    TW_TESTWARE=iot_testware
    TW_NETWORK_NAME=iottestware_net
    TW_SUBNET=172.18.0.0/16
    TW_FIXED_IP=172.18.0.4

    TW_VOLUME_NAME=testware_volume
    TW_VOLUME_PATH=/home/titan/iottestware.webserver/backend/resources/history

* (optional) Create separated Docker network

  .. code-block:: bash

    docker network create --subnet $TW_SUBNET $TW_NETWORK_NAME
    docker network ls

* (optional) Create `persistend storage <https://docs.docker.com/storage/>`_ and `docker volumes <https://docs.docker.com/storage/volumes/#create-and-manage-volumes>`_

  .. code-block:: bash

    docker volume create $TW_VOLUME_NAME

Build
=====
