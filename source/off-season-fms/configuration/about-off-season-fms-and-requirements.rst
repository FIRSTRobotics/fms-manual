.. include:: <isonum.txt>
.. _off-season-about:

About Off-Season FMS and Requirements
============================================

Overview
--------

The Field Management System (FMS) is the electronics core of a *FIRST* Robotics Competition (FRC) playing field and encompasses both hardware and software components. The software package is used to control all the field electronics (LED Displays, Station Control Cabinets, E-stops, enable/disable of the Robots, network security, etc.) and is used to manage the event by creating match schedules, scoring the matches in real-time, and posting information to the Audience screen. The FMS Off-Season version is designed to work without the full set of FRC field electronics, but retain much of the functionality that remains useful to events without *FIRST* hardware.

Additional information about the software can be found in the other articles of this documentation.

Hardware Requirements
---------------------

To run the Off-Season version the following minimum hardware items are required:

* Laptop or desktop computer with Ethernet Port
* WiFi Access Point (Linksys WRT610N or equivalent)
* Ethernet Switch (Unmanaged, 8 port, qty 3 recommended)

Other items, such as speakers or a projector, are recommended to supplement the user experience but not required for basic functionality.

Software Requirements
---------------------

In order to install Off-Season FMS, the target machine must meet these minimum requirements:

* Operating System: Windows 10
* Processor Speed: 64 bit OS
* CPU: 2.0 GHz
* Memory: 4 GB RAM
* Hard drive: 1 GB free hard disk space
* Hardware: Ethernet and USB Port
* Resolution: 1920x1080 or higher for best visibility

Audience Display Requirements
-----------------------------

The Audience Display program controls all audio and graphics intended for audience consumption. It can be run on the same machine as Off-Season FMS or on a separate Windows machine located on the same network as the FMS installation.
The machine being used as the Audience Display must have a modern graphics card capable of running an extended monitor at 1280x720 or 1920x1080 with 100% scaling (based on the Windows scaling settings). For game sounds, the machine must have 
speakers or connect to a system capable of accepting the audio output of the machine (such as a 1/8" heaphone jack). If using a secondary machine as the Audience Display, it should be connected via Ethernet, not wireless.

Important Off-Season Notes
--------------------------

Do not install FMS Off-Season on top of a previous installation of the software. It is safest to completely uninstall and remove any previous installations of FMS from your computer before installing a new version.
For assistance in properly removing a previous version, please :ref:`see this article <off-season-upgrading>`.

.. note::
    Important: Do not install FMS Off-Season on machines that are school or business "owned" or controlled. These machines often include restrictive user accounts, additional firewall and security programs, etc, which are not tested by *FIRST* and may interfere with FMS's ability to function properly.
