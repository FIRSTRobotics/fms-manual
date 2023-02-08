.. _scorekeeper-setup:

Setup (Day 0)
======================

Prepare the field and arena for play

Setup
-----

For a three-day Regional event, setup is done on the day preceding the Practice matches; Regional Directors can choose to also allow pit load-in during setup, but this does not affect setup activities. For a two-day District event, setup may happen on the same day as Practice matches and robot Inspection. For the purposes of this document, setup is just considered the “setup activity” and is not specific to event type.

#. Check in with your FTA and find out of the FMS System has been setup.
#. Launch the FMS Event Manager software (if not already loaded)
#. Check to determine if the Internet Connection provided by the venue for FMS has an overlapping IP range by checking the Smart Router - the Smart Router is a device within the Scorpion that automatically handles issues between external venue and internal IP address conflicts. As such, issues with the Smart Router will be handled on an individual basis. Launch the FMS Event Manager software, and click on the “Settings” button at the top of the application. The “Network Status” tab in the resulting panel should be automatically selected. If not, please select this tab. Click on the button marked, “Get Smart Router Configuration” under the “Smart Router (External)” heading. If the “Venue IP” is marked as “unknown”, click the button again. Determine if the "Venue IP" (first item in the "WAN/Venue") and "LAN IP" (first item in the "Local Network") are the same. If so, you may have an overlapping IP. If the problem persists, the FTA should contact HQ Support. If the venue requires a specific static IP address, uncheck “Use Venue DHCP” and enter the details in the “Venue Internet” section. This should only be done with your FTA.

   * Launch the FMS Event Manager software, and click on the “Settings” button at the top of the application.
   * The “Network Status” tab in the resulting panel should be automatically selected. If not, please select this tab.
   * Click on the button marked, “Get Smart Router Configuration” under the “Smart Router (External)” heading. If the “Venue IP” is marked as “unknown”, click the button again. Determine if the "Venue IP" (first item in the "WAN/Venue") and "LAN IP" (first item in the "Local Network") are the same. If so, you may have an overlapping IP. If the problem persists, the FTA should contact HQ Support.

      * If the “Venue IP” is marked as “unknown”, click the button again.
      * Determine if the "Venue IP" (first item in the "WAN/Venue") and "LAN IP" (first item in the "Local Network") are the same. If so, you may have an overlapping IP.
      * If the problem persists, the FTA should contact HQ Support.

   * If the venue requires a specific static IP address, uncheck “Use Venue DHCP” and enter the details in the “Venue Internet” section. This should only be done with your FTA.

#. Once the FMS System is setup, contact HQ support via Slack to determine if there are any FMS updates or maintenance that needs to be done for your event. It may not be possible for you to perform a successful Data Download without authorization from HQ support. Do not create the event database until HQ support ok’s you to complete this action. If an update was required, you will also need to update the Audience Display toughbook. This can be done using the "Check for Updates" button within the Audience Display configuration panel or by copying the installer to a USB drive (ask the FTA for one). Remember, DO NOT launch the Audience Display software until a database has been created for the event! The easiest way to obtain the Audience Display installer (if the Audience Display Application is not already installed on the computer) is to: Ensure the remote Audience Display is on the FMS Network Open a web browser (Chrome Preferred) to the following address: http://10.0.100.5/FRCDownloads This will open a browser page to select the available applications to download. Select the Audience Display application to download. Install the Audience Display application on the local computer.

   * If an update was required, you will also need to update the Audience Display toughbook. This can be done using the "Check for Updates" button within the Audience Display configuration panel or by copying the installer to a USB drive (ask the FTA for one). Remember, DO NOT launch the Audience Display software until a database has been created for the event! The easiest way to obtain the Audience Display installer (if the Audience Display Application is not already installed on the computer) is to: Ensure the remote Audience Display is on the FMS Network Open a web browser (Chrome Preferred) to the following address: http://10.0.100.5/FRCDownloads This will open a browser page to select the available applications to download. Select the Audience Display application to download. Install the Audience Display application on the local computer.

      * Remember, DO NOT launch the Audience Display software until a database has been created for the event!
      * The easiest way to obtain the Audience Display installer (if the Audience Display Application is not already installed on the computer) is to: Ensure the remote Audience Display is on the FMS Network Open a web browser (Chrome Preferred) to the following address: http://10.0.100.5/FRCDownloads This will open a browser page to select the available applications to download. Select the Audience Display application to download. Install the Audience Display application on the local computer.

         #. Ensure the remote Audience Display is on the FMS Network
         #. Open a web browser (Chrome Preferred) to the following address: http://10.0.100.5/FRCDownloads This will open a browser page to select the available applications to download.

            * http://10.0.100.5/FRCDownloads
            * This will open a browser page to select the available applications to download.

         #. Select the Audience Display application to download.
         #. Install the Audience Display application on the local computer.

#. Load the Audience Display software on the Audience Display Toughbook ONLY if the event database has been created. Without an event database, the Audience Display may not load correctly. The Audience Display has two hotkey combinations to load its configuration panel. CTRL-SHIFT-F12 CTRL-SHIFT-C Use the hotkey CTRL-SHIFT-1 to move and center the audience display onto the primary monitor, or if using HDMI output use CTRL-SHIFT-2 to move and center the audience display to the secondary monitor. A/V might want to run their own Remote Audience Screen. If so, let them follow the same process to get an updated version of the Audience Display.

   * The Audience Display has two hotkey combinations to load its configuration panel. CTRL-SHIFT-F12 CTRL-SHIFT-C

      * CTRL-SHIFT-F12
      * CTRL-SHIFT-C

   * Use the hotkey CTRL-SHIFT-1 to move and center the audience display onto the primary monitor, or if using HDMI output use CTRL-SHIFT-2 to move and center the audience display to the secondary monitor.
   * A/V might want to run their own Remote Audience Screen. If so, let them follow the same process to get an updated version of the Audience Display.

#. Within the FMS Event Manager software, click the “Field Test” button at the top of the application and ensure all of the hardware is online. All component LEDs should be Green – you may need to click “Refresh Indicators” to get updated information. Some update via refresh, some only make you think they do. Any elements under “Field Hardware” that remain Red may need HQ Support to help troubleshoot. The FTA should help troubleshoot all components of the Field.

   * All component LEDs should be Green – you may need to click “Refresh Indicators” to get updated information. Some update via refresh, some only make you think they do. Any elements under “Field Hardware” that remain Red may need HQ Support to help troubleshoot. The FTA should help troubleshoot all components of the Field.

      * Any elements under “Field Hardware” that remain Red may need HQ Support to help troubleshoot.
      * The FTA should help troubleshoot all components of the Field.

#. Run Match Test and confirm that all field components operate correctly. This process should be coordinated with the FTA You cannot access the Match Test area (the button will not become active) until the Data Download step (Step 1) has been completed in the Event Wizard, an event is selected (Step 2), and the database has been created. Contact HQ support for assistance if this has not been completed yet.

   * You cannot access the Match Test area (the button will not become active) until the Data Download step (Step 1) has been completed in the Event Wizard, an event is selected (Step 2), and the database has been created. Contact HQ support for assistance if this has not been completed yet.

#. Coordinate with the FTA and A/V crew to ensure that all game sounds play correctly. You can use the “Test Sound” buttons within the Audience Display configuration panel to play test sounds, or use the continuous sound player in the audience screen’s Jump Menu (right-click the Audience Display icon in the task bar).
#. Verify that the printer is working correctly.
#. Set up event by using the “Event Wizard” at the top of the FMS Event Manager software. Check with Event Registration and make any necessary changes (add/delete) to the list of participating teams. Verify with the FTA before making any changes.
#. Generate Practice Match schedules (be sure to use the Lunch checkbox if applicable) and activate the Practice schedule (Steps 3 through 6 in the Event Wizard) and print out sufficient copies to distribute to teams (from the “Reports” button at the top of the application). In some venues, the Pit Admin may only need a single copy of the schedule and they’ll go and make copies. Work with the Event Manager and the FTA to ensure that the Practice Match schedule works within the overall timeframe of the practice portion of the event.
#. Work with the FTA to determine if you need to print the Announcer’s Report for practice matches. Often this is not necessary.
#. Work with the FTA to ensure that the WPA key file is transferred to the radio programming kiosk. The WPA key file can be imported to the kiosk via the FMS network, or exported from the “Practice Team Selection” step (Step 3) from the Event Wizard. Most FTAs will prefer to import the key file over the network, so exporting the file should be a rare requirement.
#. Ensure the Backup Configuration settings have been set. Select “Settings”, click on the “Backup Config” tab, and click “Browse” to set a backup location. This MUST be on a thumbdrive or other external storage.

   * Select “Settings”, click on the “Backup Config” tab, and click “Browse” to set a backup location.
   * This MUST be on a thumbdrive or other external storage.

#. For events that move directly from Setup to Practice, go on to Practice. For all others, determine when you will be leaving for the evening. When you leave for the evening, please put the field lighting into “Night Mode”. You can access “Night Mode” from within the “Settings” page, the button marked “Night Mode” is under the button marked “Awards Mode” in the center top of the application.

   * When you leave for the evening, please put the field lighting into “Night Mode”. You can access “Night Mode” from within the “Settings” page, the button marked “Night Mode” is under the button marked “Awards Mode” in the center top of the application.
