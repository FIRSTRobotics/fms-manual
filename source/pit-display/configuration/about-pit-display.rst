About Pit Display
=================

Introduction
------------

Pit Display is a web based software program, built and distributed by *FIRST*\ |reg|, that is used to relay rankings and tournament information from FMS to the spectators in the Pit at the venue. Pit Display can be run on an computer containing and internet browser (like Firefox or Chrome) and an ethernet port or wireless adapter. This manual will walk through the available data, configuration options, and best practices related to the Pit Display.

Wiring Pit Display
------------------

In order to connect to FMS, the Pit Display must have a wired or wireless connection to FMS. If wired, it needs to be on the same network as the FMS machine (10.0.100.X), and no additional LANs. For wireless access, if field wireless is available, connect to the appropriate wireless network and ensure the target machine receives an address of 10.0.100.X. Wireless networks for *FIRST* fields have different names from truck to truck, contact the FTA for additional information.

Whenever possible, the Pit Display should be on a wired Ethernet connection.

Opening Pit Display
-------------------

To open the Pit Display, simply use an web browser (such as Chrome or Firefox) and open a new page/tab. Navigate to 10.0.100.5/Pit in your browser address bar, and the Pit display for the appropriate tournament level (Qual/Playoff) will open. If the display does not open, ensure your connection to FMS by using ping and (for Off-Season installations) making sure IIS is running on the FMS machine. (IIS will automatically be running on Official *FIRST* fields)

Event Setup Order
-----------------

In order to properly synchronize with FMS, it is highly recommended that you do not run access the Pit Display program until after initial configuration of the event is complete through the Event Wizard and Practice matches are complete. Configuration information is downloaded by the program, and completing in this order should lead to the best experience.

Closing Pit Display
-------------------

To close the software, simply close your web browser (or the Pit Display tab therein) or use the windows hotkey combination of ALT-F4.
