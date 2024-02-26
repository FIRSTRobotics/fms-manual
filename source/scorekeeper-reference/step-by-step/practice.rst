.. _scorekeeper-practice:

Practice (Day 1)
======================

During Practice, teams will come to the Practice Field and run their robots according to a set Practice Schedule. The actual schedule isn’t “set in stone”, and different event types (Regional vs District) will run Practice differently. It’s recommended to run all Practice matches within a Practice schedule to allow the FMS to log match data and robot data so that FTAs and HQ can examine robot and/or field problems through the match logs.

Practice Process
--------------------

#. Check in with the FTA.
#. Launch the FMS Event Manager software (if not already loaded).

   * Check with HQ Support to determine if any FMS updates or other software updates/maintenance is required.

#. On the Audience Display Toughbook, load the Audience Display software (if not already loaded). For additional information about how to configure the Audience Display, see the corresponding section in the :ref:`the setup step <scorekeeper-setup>`
#. Run a Test Match to confirm all field components operate correctly. This process should be coordinated with the FTA. This may be an abbreviated version of the test conducted during Setup depending on the time available and FTA preferences.
#. Check with Event Registration and make any necessary changes (add/delete) to the list of participating teams.

   * Regenerate the Practice Match schedule if there are any additions to the team list.
   * Deletions do not require a regenerated schedule for Practice Matches.

   .. important::
      Verify with the FTA before making any changes.

#. Ensure the Practice Schedule is Activated in the Event Wizard.
#. Field Calibration: Teams will be given an amount of time where they can come and take measurements or calibrate their sensors. This process is overseen by the FTA, but Scorekeeper presence for safety is appreciated.

   * The FTA should be overseeing this and handling Q/A about this time. For situational awareness: robots may be turned on - but may not drive, extend outside frame perimeter, or interact with field elements/notes. [Rule T301] Not required, but is nice to NOT have the field in night mode - so it is lit more like it will be during matches for those doing camera calibrations.

#. Lunch Break
#. Practice Matches
#. Generate a Qualification Match schedule using the corresponding steps in the Event Wizard.

   .. important::
      Verify the FMS Server is set to the correct timezone. FMS will warn you in the event of timezone irregularities, do not click through. If there is a timezone mismatch issue contact FRC Support immediately.

   * Be sure to use the Lunch checkbox in the Schedule Break during the Lunch period!
   * Print out sufficient copies of the Qualification Schedule Report to distribute to teams. In some venues, the Pit Admin may only need a single copy of the schedule and they’ll go and make copies.
   * Print out any copies needed for queuing and field staff
   * Work with the Event Manager and FTA to ensure that the Qualification Match schedule works within the overall timeframe of the event (start/end times, lunch period, etc.).
   * If you activated the Qualification Schedule as part of this process, but have not yet completed Practice Matches, return to the Event Manager and re-activate the practice match schedule. This is necessary in order to continue playing through the Practice schedule.

#. End of Practice

   * In the "Settings" view, using the "Backup" tab, use the "Force Event Backup" button to force a full event backup for the end of practice matches.
   * Work with your FTA and Pit Admin to encourage teams who were unable to attend their practice matches to come to the Field for a connection test. These are often held after the published Practice schedule or right before Qualificaiton matches start. You can view teams who have not connected using the WPA Status report on the Reports tab.
   * If doing connection tests, note that the team will need to bring their DS and Robot, and the radio must be programmed for this event. They do not need to have passed inspection. You can perform their radio connection test using the Match Test interface.

#. End of Day
   * Check with the FTA to determine if power will remain on or will be shut off overnight. If power to the field will be turned off, shutdown the Scorpion server with direction from the FTA. Otherwise, put the field in Night Mode.
