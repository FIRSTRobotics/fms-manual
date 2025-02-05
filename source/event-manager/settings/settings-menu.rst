.. _settings-menu:

Settings Menu
======================

.. image:: images/settings-menu-0.png

The Settings screen can be accessed from the Settings tab along the top of the window. This screen contains important global settings for network, hardware, backup, and data configurations within the FMS Software.
Some items within the Settings screen may be used by Scorekeepers and FTAs, such as Backup Configuration, some network settings, spare hardware configuration, and others.
However, some of the items are protected via a Settings Lock and can only be unlocked by FRC Engineering staff. These items are deemed "Critical" (as in the case of AP channel
configuration or changing the Data Sync state) or "Experimental"  (as in the case of purging tournament data). Items within the Settings page that are protected by the Settings Lock are followed
by an asterisk (*). In the Off-Season version of the software the Settings are permanently unlocked though some features (such as hardware configuration or Data Sync) are disabled because they do not apply.

The left bar of the Settings Page (pink box) contains quick-access information and available tabs. Information also includes the current server time information and the currently active time zone.


.. important::
    It is critical that the time zone of the server be set correctly for the location the event is being held, especially if the event will have schedules and data available online. 

Clicking the tabs on the left will change which data is available on the right side of the screen (green box). Information about each tab can be found in its associated documentation step.

The bottom has buttons for a few operations:

[*Restart FMS Services*] Click to reset the underlying FMS Services on the Server, which requires the FTA password

[*Awards Mode*] Enable all LEDs on the field to match their alliance color and display the current year on the Team Signs

[*Night Mode*] Turn off all LED Displays and put the field in a low power state
