.. _scorekeeper-setup:

.. note::
    This document may contain links that begin with "10.0.100.5" but look like traditional web links. These links will only work when attached to an FRC field.

.. note::
    If you leave the FMS Computer unattended (such as for lunch break) please be sure to "Lock" it using the Windows Key + "L" to protect the scoring data.

Setup (Day 0)
======================

For a three-day Regional event, setup is done on the day preceding the Practice matches; Program Delivery Partners can choose to also allow pit load-in during setup, but this does not affect setup activities.
For a two-day District event, setup may happen on the same day as Practice matches and robot Inspection. For the purposes of this document, setup is just considered the "setup activity" and is not specific to event type.

Setup Process
-----------------

#. Check in with your FTA and find out of the FMS System has been setup.
#. Launch the FMS Event Manager software (if not already loaded).
#. Check that the FMS is connected to the internet.

   * If the FMS does not have an internet connection, jump to the **Network Troubleshooting** section.

#. Once the FMS is set up and connected to the internet, contact FRC Support via Slack to determine if there are any updates or maintenance that needs to be done for your event.

   * It may be possible to perform a successful Data Download at this time, however, you should not update FMS or create the Event Database until FRC Support has approved these actions.

#. Once the Event Database has been created, start setting up the Audience Display.

   * If an FMS update was required, you will also need to update the Audience Display. This can be done using the "Check for Updates" button within the Audience Display configuration panel. 
   * If the Audience Display application is not already on the computer, connect to the FMS Network and navigate to http://10.0.100.5/FRCDownloads where you can download the current Audience Display installer.
   * A/V or Webcast may need to run their own Audience Display. They can follow the same process to get an up-to-date version of the Audience Display
   * Create a folder on the Desktop where you can store commonly accessed reports, like team lists and schedules.

#. Launch the Primary Audience Display software and configure the display(s) using the following hotkey combinations. Note that the Audience Display does not run on the FMS Server, but rather the laptop with the "Audience Display" sticker. At some events, the A/V department may be responsible for this setup.

   .. list-table::
      :widths: 35 65
      :header-rows: 0

      * - CTRL-SHIFT-F12
        - Load Configuration Panel
      * - CTRL-SHIFT-C
        - Load Configuration Panel
      * - CTRL-SHIFT-1
        - Center AD on Primary Display
      * - CTRL-SHIFT-2
        - Center AD on Secondary Display

#. Within the FMS Event Manager software, click the "Field Test" button at the top of the application and ensure all of the hardware is online.

   * All component LEDs should be Green. You may need to click "Refresh Indicators" to get updated information.
  
      * Any elements under "Field Hardware" that remain Red may need HQ Support to help troubleshoot.
      * The FTA should help troubleshoot all components of the Field.

#. Run Match Test to confirm that all field components operate correctly. This process should be coordinated with the FTA.

   .. note::
       You cannot access the Match Test area (the button will not become active) until the Data Download (Step 1) has been completed, an event is selected, and the database has been created (Step 2). Contact FRC Support for assistance if this has not been completed yet.

#. Coordinate with the FTA and A/V to ensure that all game sounds play correctly. You can use the “Test Sound” buttons within the Audience Display configuration panel, or use the continuous sound player in the Audience Display jump menu (right-click the Audience Display icon in the task bar).
#. Verify the printer is working correctly.

   * Locate and stage additional paper for easy access
   * If toner begins to run low (such as streaking or gaps on printed pages) open the printer and shake the cartridge, then re-install and attempt to print again. This often results in additional pages before swapping the toner.
   * When toner is replaced, place the old toner back in the box and clearly label is "USED" in Case 07. Be sure to ask your FTA to note this in their event report.

#. Complete the Practice Team Selection step in the Event Wizard. Check with Event Management to make any necessary changes (add/delete) to the list of participating teams.

   .. important::
      Verify with the FTA before making any changes.

#. Generate Practice Match schedules (be sure to use the Lunch checkbox if applicable) and activate the Practice schedule (Steps 3 through 6 in the Event Wizard) and print out sufficient copies to distribute to teams (from the “Reports” button at the top of the application). In some venues, the Pit Admin may only need a single copy of the schedule and they’ll go and make copies. Work with the Event Manager and the FTA to ensure that the Practice Match schedule works within the overall timeframe of the practice portion of the event.
#. Work with the FTA to determine if you need to print the Announcer’s Report for practice matches. Often this is not necessary.
#. Work with the FTA to ensure that the WPA Kiosk(s) have been set up. The WPA key file can be imported to the kiosk via the FMS network or exported from the “Practice Team Selection” step from the Event Wizard. Most FTAs will prefer to import the key file over the network.
#. Ensure the Backup Configuration settings have been set.

   * Select "Settings", click on the "Backup" tab, and click "Browse" to set a backup location.
   * This MUST be on a thumbdrive or other external storage.

#. For events that move directly from Setup to Practice, go on to Practice. For all others, determine when you will be leaving for the evening.

   * When you leave for the evening, please put the field lighting into "Night Mode". You can access "Night Mode" from within the "Settings" page, the button marked "Night Mode" is under the button marked "Awards Mode" in the center top of the application.

Network Troubleshooting
------------------------

Please consult with your FTA or seek advice from FRC Engineer via Slack if Network Troubleshooting is needed.
