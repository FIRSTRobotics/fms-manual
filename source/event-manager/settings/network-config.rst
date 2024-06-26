.. _settings-network-config:

Network Config
======================

.. image:: images/network-config-0.png

The Network Config tab on the Settings page contains all of the network settings that may be adjusted for the FMS hardware and software. It has four sections: Smart Router, Field Router and the Access Points.

[ *Blue* - Access Point (2.4)] Contains functions for setting the Access Point configuration within the FMS Hardware set. Set Access Point can be used to configure the radio used on the Field.
The SSID and WPA Key is configurable by the FTA without a password, but once set the WPA Key value will not persist once the software navigates away from the Settings page.
If the WPA Key is forgotten, a new one must be set by the FTA.

[ *Red* - Access Point (5/6)] Used to configure the Robot facing side of the radio network. Do not change the settings on the Router without FTA and/or FRC Engineering support.
Additional options allow support staff to configure the minimum rate for operation of the robot facing side of the radio. For events with multiple fields, the "Group" option can be changed to avoid overlap in radio test groups across access points.

[ *Pink -* Field Router] Provides functions for setting configuration information for the Router inside the #33 case.
Set Router can be used to configure the router settings for venue-specific network access configuration. Do not change the settings on the Router without FTA and/or FRC Engineering support.
In almost every case, the Field Router need not be adjusted, as the Smart Router would be updated to the venue-specific settings instead.

[ *Yellow* - Smart Router] Contains functions for setting the Smart Router configuration within the FMS Hardware set.
Set Router Configuration can be used to configure the router settings for venue-specific network access configuration. Do not change the settings on the Smart Router without FTA and/or FRC Engineering.

To change the type of Router or Access Point in use, visit the :doc:`Hardware <hardware>` tab. For Status information visit the :doc:`Status <network-status>` tab.
