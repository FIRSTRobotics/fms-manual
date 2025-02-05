.. include:: <isonum.txt>
.. _pit-display-about:

About Pit Display
======================

Introduction
------------

Pit Display is a web based software program, built and distributed by *FIRST*\ |reg|, that is used to relay rankings and tournament information from FMS to the 
spectators in the Pit at the venue. Pit Display can be run on an computer containing and internet browser (like Firefox or Chrome) and an ethernet port. 
This manual will walk through the available data, configuration options, and best practices related to the Pit Display.

Wiring Pit Display
------------------

In order to connect to FMS the Pit Display must have a wired connection to FMS. The target machine must be on the same network as the FMS machine (10.0.100.X), and no additional LANs. 
Whenever possible, the Pit Display should be on a wired Ethernet connection.It is not recommended to attempt to run the Pit Display on a wireless connection. 
Wireless networks for *FIRST* fields have different names from truck to truck, contact the FTA for additional information.

Opening Pit Display
-------------------

To open the Pit Display, simply use an web browser (such as Chrome or Firefox) and open a new page/tab. Navigate to 10.0.100.5/Pit in your browser address bar, 
and the Pit display for the appropriate tournament level (Qual/Playoff) will open. If the display does not open, ensure your connection to FMS by using ping 
and (for Off-Season installations) making sure IIS is running on the FMS machine. (IIS will automatically be running on Official *FIRST* fields)

Event Setup Order
-----------------

In order to properly synchronize with FMS, it is highly recommended that you do not run access the Pit Display program until after initial configuration of the event is 
complete through the Event Wizard and Practice matches are complete. Configuration information is downloaded by the program and completing in this order should lead to the best experience. 
There is no informaiton on the Pit Display during Practice matches, so there is no advantage to running the Pit Display earlier in the event.

Closing Pit Display
-------------------

To close the software, simply close your web browser (or the Pit Display tab therein) or use the windows hotkey combination of ALT-F4.
