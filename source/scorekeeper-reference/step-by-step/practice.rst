.. _scorekeeper-practice:

Practice (Day 1)
======================

During Practice, teams will come to the Practice Field and run their robots according to a set Practice Schedule. The actual schedule isn’t “set in stone”, and different event types (Regional vs District) will run Practice differently. It’s recommended to run all Practice matches within a Practice schedule to allow the FMS to log match data and robot data so that FTAs and HQ can examine robot and/or field problems through the match logs.

Practice Process
--------------------

#. Check in with the FTA.
#. Launch the FMS Event Manager software (if not already loaded).

   * Check with HQ Support to determine if any FMS updates or other software updates/maintenance is required.

#. On the Audience Display Toughbook, load the Audience Display software (if not already loaded).

   * If an FMS update was required, you will also need to update the Audience Display. This can be done using the “Check for Updates” button within the Audience Display configuration panel.
   * If the Audience Display application is not already on the computer, connect to the FMS Network and navigate to http://10.0.100.5/FRCDownloads where you can download the current Audience Display installer.
   * A/V or Webcast may need to run their own Audience Display. They can follow the same process to get an up-to-date version of the Audience Display
   * Once the Audience Display software has been launched, configure the display(s) using the following hotkey combinations.

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

#. Run a Test Match to confirm all field components operate correctly. This process should be coordinated with the FTA. This may be an abbreviated version of the test conducted during Setup depending on the time available and FTA preferences.
#. Check with Event Registration and make any necessary changes (add/delete) to the list of participating teams.

   * Regenerate the Practice Match schedule if there are any additions to the team list.
   * Deletions do not require a regenerated schedule for Practice Matches.

   .. important::
      Verify with the FTA before making any changes.

#. Ensure the Practice Schedule is Activated in the Event Wizard (Step 6).
#. Lunch Break
#. Practice Matches
#. Generate a Qualification Match schedule using steps 7-10 in the Event Wizard.

   .. important::
      Verify the FMS Server is set to the correct timezone. FMS will warn you in the event of timezone irregularities, do not click through. If there is a timezone mismatch issue, contact FRC Support immediately.

   * Be sure to use the Lunch checkbox in the Schedule Break during the Lunch period!
   * Print out sufficient copies of the Qualification Schedule Report to distribute to teams. In some venues, the Pit Admin may only need a single copy of the schedule and they’ll go and make copies.
   * Work with the Event Manager and FTA to ensure that the Qualification Match schedule works within the overall timeframe of the event (start/end times, lunch period, etc.).
   * If you activated the Qualification Schedule as part of this process, but have not yet completed Practice Matches, return to the Event Manager and re-activate the practice match schedule. This is necessary in order to continue playing through the Practice schedule.

#. End of Practice

   * In the “Settings” view, using the “Backup Config” tab, use the “Force Event Backup” button to force a full event backup for the end of practice matches.
   * Check with the FTA to determine if power will remain on or will be shut off overnight. If power to the field will be turned off, shutdown the Scorpion server with direction from the FTA. Otherwise, put the field in Night Mode.
