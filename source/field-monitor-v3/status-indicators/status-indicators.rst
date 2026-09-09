.. _field-monitor-v3-status-indicators:

Status Indicators
=================

This page describes the status indicators on the :ref:`Field Monitor <field-monitor-v3-live-simple>`.

Driver Station
--------------

.. note::
    For suggestions on resolving issues with the Driver Station computer and software, please go to the Driver Station Troubleshooting section of the :ref:`Connectivity Guide <field-monitor-v3-connectivity-guide>`

========================================  ===========
Indicator                                 Explanation    
========================================  ===========
.. image:: images/ds-bad.png              No device is detected.
.. image:: images/ds-partially-ok.png     A device is connected at the station, but FMS cannot communicate with the Driver Station software.
.. image:: images/ds-ok.png               A device is connected with Driver Station software running and correct team number assigned.
========================================  ===========


Robot radio
-----------

.. note::
    For suggestions on resolving issues with the robot radio, please go to the Robot Troubleshooting section of the :ref:`Connectivity Guide <field-monitor-v3-connectivity-guide>`

===================================  ===========
Indicator                            Explanation    
===================================  ===========
.. image:: images/radio-bad.png      The radio is not connected to the Robot Access Point.
.. image:: images/radio-laptop.png   The radio is connected to the Robot Access Point, but cannot be pinged by the Driver Station software.
.. image:: images/radio-1-bar.png    The radio is connected to the Robot Access Point, can be pinged by the Driver Station software, and has poor connection quality.
.. image:: images/radio-2-bars.png   The radio is connected to the Robot Access Point, can be pinged by the Driver Station software, and has fair connection quality.
.. image:: images/radio-3-bars.png   The radio is connected to the Robot Access Point, can be pinged by the Driver Station software, and has good connection quality.
.. image:: images/radio-4-bars.png   The radio is connected to the Robot Access Point, can be pinged by the Driver Station software, and has excellent connection quality.
===================================  ===========

roboRIO
-------

.. note::
    For suggestions on resolving issues with the roboRIO, please go to the Robot Troubleshooting section of the :ref:`Connectivity Guide <field-monitor-v3-connectivity-guide>`

========================================  ===========
Indicator                                 Explanation    
========================================  ===========
.. image:: images/rio-bad.png             roboRIO is not detected.
.. image:: images/rio-partially-ok.png    roboRIO is detected, but no robot code is observed running.
.. image:: images/rio-ok.png              roboRIO is detected, with robot code running.
========================================  ===========


Robot Status
------------

These robot status indicators show in the top right corner of the station. Outside of a match, only the E-Stop, A-Stop, Bypassed, or Not Ready will show.

========================================  ===========
Indicator                                 Explanation    
========================================  ===========
.. image:: images/e-stop.png              Robot is E-Stopped.
.. image:: images/a-stop.png              Robot is A-Stopped.
.. image:: images/auto-disabled.png       Robot is disabled in Auto mode.
.. image:: images/teleop-disabled.png     Robot is disabled in Teleoperated mode.
.. image:: images/auto-enabled.png        Robot is enabled in Auto mode.
.. image:: images/teleop-enabled.png      Robot is enabled in Teleoperated mode.
.. image:: images/bypassed.png            Robot has been bypassed by the Scorekeeper and will not run in this match.
.. image:: images/not-ready.png           Robot is not fully connected and ready for match operation. This indicator is driven by the same data that drives the roboRIO indicators. This will only show after Pre-Start and before Match Start.
========================================  ===========


Additional Radio Indicators
---------------------------

These radio indicators will appear next to the station indicator (ie "Station 3").

========================================  ===========
Indicator                                 Explanation    
========================================  ===========
.. image:: images/new-radio.png           The radio currently connected to the Field Access Point has a different MAC address than the one used by this team in their previous match.
.. image:: images/new-key.png             The team has not yet participated in a match (their WPA key has not been used).
========================================  ===========


Station Status Indicators
---------------------------

When any of these indicators appear, all of the status indicators for the station will be hidden. They will appear again once the issue from the indicator is resolved.

========================================  ===========
Indicator                                 Explanation    
========================================  ===========
.. image:: images/move-to-blue-3.png      The device connected to the station is running DS software configured for the team that is scheduled to be in Blue Station 3.
.. image:: images/move-to-red-1.png       The device connected to the station is running DS software configured for the team that is scheduled to be in Red Station 1.
.. image:: images/team-mismatch.png       The device connected to the station is running DS software configured for a team that is not scheduled to be in this match.
========================================  ===========