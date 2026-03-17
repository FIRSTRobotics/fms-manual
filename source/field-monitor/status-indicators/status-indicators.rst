.. _field-monitor-status-indicators:

Status Indicators
=================


Driver Station (DS)
-------------------

.. note::
    For suggestions on resolving issues with the Driver Station computer and software, please go to the Driver Station Troubleshooting section of the :ref:`Connectivity Guide <field-monitor-connectivity-guide>`

========================================  ===========
Indicator                                 Explanation    
========================================  ===========
.. image:: images/yellow-x.png            No device is detected.
.. image:: images/yellow-exclamation.png  A device is connected at the station, but FMS cannot communicate with the Driver Station software.
.. image:: images/white-check.png         Device is connected with Driver Station software running and communicating with FMS. 
========================================  ===========


Radio
-----

.. note::
    For suggestions on resolving issues with the robot radio, please go to the Robot Troubleshooting section of the :ref:`Connectivity Guide <field-monitor-connectivity-guide>`

===================================  ===========
Indicator                            Explanation    
===================================  ===========
.. image:: images/yellow-x.png       No device is detected.
.. image:: images/yellow-laptop.png  A radio is connected to the Robot Access Point, but cannot communicate with the Driver Station software. **NOTE**: The radio communicates with the Driver Station software through the Rio, so if the Rio is not connected this indicator will still show.
.. image:: images/radio-1-bar.png    Radio is connected to the Robot Access Point, can communicate with the Driver Station software, and has poor connection quality.
.. image:: images/radio-2-bars.png   Radio is connected to the Robot Access Point, can communicate with the Driver Station software, and has fair connection quality.
.. image:: images/radio-3-bars.png   Radio is connected to the Robot Access Point, can communicate with the Driver Station software, and has good connection quality.
.. image:: images/radio-4-bars.png   Radio is connected to the Robot Access Point, can communicate with the Driver Station software, and has excellent connection quality.
===================================  ===========

Rio
---

.. note::
    For suggestions on resolving issues with the Rio, please go to the Robot Troubleshooting section of the :ref:`Connectivity Guide <field-monitor-connectivity-guide>`

========================================  ===========
Indicator                                 Explanation    
========================================  ===========
.. image:: images/yellow-x.png            No device is detected.
.. image:: images/yellow-exclamation.png  Rio is powered on and responding to ping, but the code is likely not running.
.. image:: images/white-check.png         Rio is powered on and responding to ping with code running.
========================================  ===========


Robot Status
------------

========================================  ===========
Indicator                                 Explanation    
========================================  ===========
.. image:: images/white-square.png        Robot Status not being displayed. Auto and Teleoperated status is hidden outside of the match and will show this indicator. **NOTE**: the E-Stop and A-Stop indicator will show outside of a match if the robot is in either of those states.
.. image:: images/yellow-x.png            Robot Status is unknown
.. image:: images/black-e.png             Robot is E-Stopped
.. image:: images/black-a.png             Robot is A-Stopped
.. image:: images/yellow-a.png            Robot is disabled in Auto mode
.. image:: images/yellow-t.png            Robot is disabled in Teleoperated mode
.. image:: images/white-a.png             Robot is enabled in Auto mode
.. image:: images/white-t.png             Robot is enabled in Teleoperated mode
========================================  ===========