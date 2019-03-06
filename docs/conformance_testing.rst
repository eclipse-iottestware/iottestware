############################
Protocol Conformance Testing
############################

.. ###> Abbreviations for this document
.. |mqtt| replace:: :abbr:`MQTT (MQ Telemetry Transport)`
.. |ics| replace:: :abbr:`ICS (Implementation Conformance Statement)`
.. |iut| replace:: :abbr:`IUT (Implementation Under Test)`
.. |tdl_to| replace:: :abbr:`TDL-TO (Test Description Language - Structured Test Objective Specification)`
.. |tp| replace:: :abbr:`TP (Test Purpose)`
.. |tp_term| replace:: :term:`Test Purpose`
.. |tc| replace:: :abbr:`TC (Test Case)`
.. |tss| replace:: :abbr:`TSS (Test Suite Structure)`
.. |ts| replace:: :abbr:`TS (Test System)`
.. |tsstp| replace:: :abbr:`TSS&TP (Test Suite Structure & Test Purposes)`
.. |etsi| replace:: :abbr:`ETSI (European Telecommunications Standards Institute)`
.. |iso| replace:: :abbr:`ISO (International Organization for Standardization)`

.. contents::

General
=======
The purpose of conformance testing is to determine to what extent a single implementation of a particular standard conforms to the individual requirements of that standard.
Please find additional and more detailed information about `conformance testing <https://portal.etsi.org/services/centrefortestinginteroperability/etsiapproach/conformancetesting.aspx>`_ at ETSI's *Center for Testing & Interoperability*

The |iso| standard for the methodology of conformance testing (ISO/IEC 9646-1 and ISO/IEC 9646-2) as well as
the |etsi| rules for conformance testing (ETSI ETS 300 406) are used as a basis for the test methodology.

To implement this methodology we require several intermediary artefacts.
Those single artefacts break down the whole complexity of conformance testing
into smaller pieces, each with a specific perspective on the problem.

.. image:: images/process.png
   :width: 500px
   :alt: Conformance Test Methodology
   :align: center

Test Suite Structure
====================
In the first step we define a |tss| for a specific |iut|.

The |tss| reflects the coverage of the reference specification by the |ts|: it is a synopsis of "which tests are
performed on which aspects of the reference specification". The conformance requirements and the |ics|
proforma of the base specification are an essential source of cross-reference to check that the coverage
of the test suite specified by the |tsstp| is acceptable.


Test Configurations
====================
*TODO: Why do we need Test configurations?*

Test Purpose Catalogues
=======================
A |tp| (|tp_term|) is a formal description of a test case. A formal description in the form of a |tp| offers a possibility of describing
the purpose of a test without having the later technical implementation in mind. Following the |tss| the tester is supported in
systematically covering the complete |iut| specification.

The listing below shows a simple |mqtt| |tp| specified in |tdl_to|.

.. code-block:: guess

    Test Purpose {
      TP Id TP_MQTT_Broker_CONNECT_001

      Test objective
      "The IUT MUST close the network connection if fixed header flags in CONNECT Control Packet are invalid"
      Reference
        "[MQTT-2.2.2-1], [MQTT-2.2.2-2], [MQTT-3.1.4-1], [MQTT-3.2.2-6]"
      PICS Selection PICS_BROKER_BASIC

      Expected behaviour
      ensure that {
        when {
            the IUT entity receives a CONNECT message containing
            header_flags indicating value '1111'B;
        }
        then {
            the IUT entity closes the TCP_CONNECTION
        }
      }
    }

The exemple below shows a simplified tabular representation for the |tp|.

=============  ===============================================
**TP-ID**      TP_MQTT_BROKER_CONNECT_01
-------------  -----------------------------------------------
**Selection**  PICS_Broker
-------------  -----------------------------------------------
**Summary**    The IUT MUST close the network connection if...
-------------  -----------------------------------------------
**Reference**  [MQTT-2.2.2-1], [MQTT-2.2.2-2]
-------------  -----------------------------------------------
**Expected bahaviour**
--------------------------------------------------------------
*initial condition* statement
--------------------------------------------------------------
*ensure that* statement
==============================================================

IoT-Testware Test Suites
========================
This steps focuses on a technical implementation of the TPs. We use `TTCN-3 <http://www.ttcn-3.org/>`_ and `Eclipse Titan <https://projects.eclipse.org/projects/tools.titan>`_
to implement each |tp| into a |tc| and orchestrate to executable test suites.

.. toctree::
   :maxdepth: 1

   mqtt_test_suite.rst
   coap_test_suite.rst
   opc_test_suite.rst
