.. _event-wizard-software-updates:

Software Updates
======================

The Software Updates step is the first step of the Event Wizard. It is used to confirm that FMS is up to date before an event is selected.

This step does not appear in the Off-Season version of the software, which has no built in update capability. There, the Event Wizard begins with Data Download.

The step displays:

* The version of FMS that is installed, in large text above the label "Current FMS Version"
* "Latest available version:" - the newest version found the last time FMS checked. "Unknown" is shown until a check has succeeded.
* "Status:" - "Current" when the installed version is the latest, "Update required" when a newer version is available, or "Never checked" when FMS has not yet completed a check.
  "Checking for updates" is shown while a check is running.
* "Last checked:" - the date and time of the last successful check, or "Never"

Checking for Updates
####################

Click the "Check for Updates" button at the bottom of the step. The server must be connected to the internet. This is the same check that is made by
the "Check For Updates" button on the :ref:`About <about-tab>` tab.

* If FMS is up to date, an "Update Status" message reports "You are currently running the latest version."
* If a newer version is available, an "FMS Update Available" message gives the version number and asks "Would you like to update to the latest version?"
  Choose "No" to stay on the installed version for now. Choose "Yes" to download the update; download progress is displayed, and then FMS closes and the installer starts automatically.

* If the check cannot be completed, an "Error checking for update" message is shown.

Once the check finishes, the information on the step is refreshed.

.. note::
    FMS closes in order to install an update. At official events, check with FRC Engineering before updating FMS.

If FMS knows that a newer version is available, or has not checked for more than 3 days, a reminder is shown when the :ref:`Event Selection <event-wizard-event-selection>` step is opened.
