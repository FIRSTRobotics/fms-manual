.. _field-monitor-status-indicators:

Status Indicators
=================

This page describes the status indicators on the :ref:`Field Monitor <field-monitor-live-simple>`.

Driver Station
--------------

.. note::
    For suggestions on resolving issues with the Driver Station computer and software, please go to the Driver Station Troubleshooting section of the :ref:`Connectivity Guide <field-monitor-connectivity-guide>`

========================================  ===========
Indicator                                 Explanation    
========================================  ===========
.. image:: images/yellow-x.png            No device is detected.
.. image:: images/yellow-exclamation.png  A device is connected at the station, but FMS cannot communicate with the Driver Station software.
.. image:: images/white-check.png         A device is connected with Driver Station software running and correct team number assigned.
========================================  ===========


Robot radio
-----------

.. note::
    For suggestions on resolving issues with the robot radio, please go to the Robot Troubleshooting section of the :ref:`Connectivity Guide <field-monitor-connectivity-guide>`

===================================  ===========
Indicator                            Explanation    
===================================  ===========
.. image:: images/yellow-x.png       The radio is not connected to the Field Access Point.
.. image:: images/yellow-laptop.png  The radio is connected to the Field Access Point, but cannot communicate with the Driver Station software. The radio communicates with the Driver Station software through the roboRIO, so if the roboRIO is not connected this indicator will still show.
.. image:: images/radio-1-bar.png    The radio is connected to the Field Access Point, can communicate with the Driver Station software, and has poor connection quality.
.. image:: images/radio-2-bars.png   The radio is connected to the Field Access Point, can communicate with the Driver Station software, and has fair connection quality.
.. image:: images/radio-3-bars.png   The radio is connected to the Field Access Point, can communicate with the Driver Station software, and has good connection quality.
.. image:: images/radio-4-bars.png   The radio is connected to the Field Access Point, can communicate with the Driver Station software, and has excellent connection quality.
===================================  ===========

roboRIO
---

.. note::
    For suggestions on resolving issues with the roboRIO, please go to the Robot Troubleshooting section of the :ref:`Connectivity Guide <field-monitor-connectivity-guide>`

========================================  ===========
Indicator                                 Explanation    
========================================  ===========
.. image:: images/yellow-x.png            roboRIO is not detected.
.. image:: images/yellow-exclamation.png  roboRIO is detected, but no robot code is observed running.
.. image:: images/white-check.png         roboRIO is detected, with robot code running.
========================================  ===========


Robot Status
------------

========================================  ===========
Indicator                                 Explanation    
========================================  ===========
.. image:: images/yellow-x.png            Robot Status is unknown.
.. image:: images/white-square.png        Robot is ready, and is not e-stopped or a-stopped.
.. image:: images/black-e.png             Robot is E-Stopped.
.. image:: images/black-a.png             Robot is A-Stopped.
.. image:: images/yellow-a.png            Robot is disabled in Auto mode.
.. image:: images/yellow-t.png            Robot is disabled in Teleoperated mode.
.. image:: images/white-a.png             Robot is enabled in Auto mode.
.. image:: images/white-t.png             Robot is enabled in Teleoperated mode.
========================================  ===========


Other Indicators
----------------

========================================  ===========
Indicator                                 Explanation    
========================================  ===========
.. image:: images/radio.png               The radio currently connected to the Field Access Point has a different MAC address than the one used by this team in their previous match.
.. image:: images/key.png                 The team has not yet participated in a match (their WPA key has not been used).
.. image:: images/bypassed.png            The robot has been bypassed by the Scorekeeper and will not run in this match.
.. image:: images/not-ready.png           The robot is not fully connected and ready for match operation. This indicator is driven by the same data that drives the roboRIO indicators.
========================================  ===========