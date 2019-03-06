##########################
About Eclipse IoT-Testware
##########################

IoT-Testware Team
=================
`Who's involved <https://projects.eclipse.org/projects/technology.iottestware/who>`_

Objective
=========
As stated in :cite:`maggi_fragility_nodate` communication protocols for the IoT are currently in a
immature state and offer different kinds of attack vectors.
We believe... *TODO!*

Conformance Test Methodology and Framework
==========================================
The IoT-Testware test suites will have a well-defined test suite structure (TSS) and a set of
protocol implementation conformance statements (PICS) as well as
protocol implementation extra information for testing (PIXIT).
The work will follow the standardized approach as defined in ISO “Conformance Test Methodology and Framework”
ISO 9646 and the best practices as described by ETSI White Paper No 3 “Achieving Technical Interoperability – the ETSI Approach”.

.. image:: images/process.png
   :width: 500px
   :alt: Conformance Test Methodology
   :align: center

Implementation
==============
The Eclipse IoT-Testware project provides standardized Abstract Test Suite (ATS) for popular IoT protocols.
For the implementation of the ATS for CoAP and MQTT we apply `ETSI <www.etsi.org>`_ Test Methodology which
is well-proven in standardizing and testing of telecommunication systems.

Such an ATS contains of several parts which are required to implement the Conformance Test Methodology and Framework.
But ATS, as the name says, are abstract, which means we need a system which executes the ATS.
Just like Java code requires the JVM to be executed, an ATS requires in our case a `TTCN-3 <http://www.ttcn-3.org/>`_ runtime.
As our TTCN-3 runtime we have chosen `Eclipse Titan <https://projects.eclipse.org/projects/tools.titan>`_ which can compile and run
our ATS.

.. image:: http://www.sioktatas.hu/doc/Titan_architecture.png
    :width: 500px
    :alt: Titan Architecture
    :align: center

The Executable Test Suite (ETS) is, as the name states, is a test suite under execution, just like running Java code.
