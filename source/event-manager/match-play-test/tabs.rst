Tabs
====

For detailed information within the Match Play and Match Test Interfaces

Tabs
----

.. image:: images/tabs-0.png

The bottom of the Match Play interface has a display window with a number of tabs:

* *Schedule -* displays the currently active schedule
* *Score -* displays the counts for various scoring elements as they are entered by referees or collected from automated scoring components on the field ( `details found here <../../eventmanager/l/608605-score-tab>`_ )
* *Game Details* - displays detailed information specific to the game (if applicable, `details found here <../../eventmanager/l/847060-game-detail-tab>`_ )
* *Status -* displays connection information on all the robots current on the playing field ( `details found here <../../eventmanager/l/608692-status-tab>`_ )
* *Video Switch -* manual interface used to control the Audience Display
* *Message -* display messages on the Background of the Audience Display
* *Options -* configuration options


Many of these tabs are described below. Status and Score tabs are not described in this article but rather in later articles.

Schedule
--------

.. image:: images/tabs-1.png

Currently active tournament level schedule, in match number order. To play a Match, click on it in the list (the list is disabled once Pre-Start is complete). The FCUI will automatically advance to the next unplayed Match at the conclusion of each Match (no need to "re-click" each time). To replay a Match, manually select it from the list and Pre-start.

The field are as follows:

* Time - Date/time the Match is scheduled to begin
* Field - Field on which the Match is scheduled to be played
* Match - Number of the Match
* Status - Match Status of one of the following values: Played - Match Complete In Progress - Match Running (on any field) Aborted - Match was canceled or E-stopped (Blank) - Match not yet played

   * Played - Match Complete
   * In Progress - Match Running (on any field)
   * Aborted - Match was canceled or E-stopped
   * (Blank) - Match not yet played


* Description - Short summary of the Match type
* Blue Alliance / Red Alliance: Score - Alliance score (once Match is complete) 1/2/3 - Team numbers in their matching stations

   * Score - Alliance score (once Match is complete)
   * 1/2/3 - Team numbers in their matching stations




Video Switch
------------

.. image:: images/tabs-2.png

Located on the Video Switch tab are the options to select what is displayed on the Audience Screen. See `Audience Display <../../audience/c/177350>`_ Screens for more details on each option.

This interface allows the user to select, via the radio buttons, which screen to show to the Audience (i.e. which screen is active in the Audience program.) It also informs which screen is currently being shown.

Several options are not controllable through this interface, but serve to inform the user when these are the current active screens (such as Match Results, which must be triggered through the FCUI or Match Review).

Note: Selecting a display here will make all instances of the Audience Display change!

Message
-------

.. image:: images/tabs-3.png

Messages can be displayed on all Audience Display instances by entering them here and selecting the *Send Message* button. To remove the text from the Audience Display use the *Clear Message* button. Messages will be displayed on all instances of Audience Display running on the FMS Network.

Options
-------

.. image:: images/tabs-4.png

Match timing can be adjusted from this screen, for use in such things as test matches. Clicking *Restore Defaults* will return all three fields to their season-specific standards. After adjusting any times as necessary, select *Save* for the timing to take effect. These can only be changed prior to Pre-start.

On the right side of the display, there are options related to common actions that are more readily accessible:

* *Force Cleanup Lights On* - When not in-match, force the purple "cleanup" lights to illuminate and indicate field staff may begin clearing the field. Cannot be used once the green lights are on.
* *Force Field Lights On* - When not in-match, force the green field reset lights to illuminate and indicate "safe to enter" state
* *Force Event Database Backup* - As the name suggests, forces a copy of the event database to be made and written to the USB Drive specified in `Settings <../../eventmanager/l/607921-backup-config>`_
* *Re-calculate Current Rankings* - Runs all teams through the calculator for the given tournament phase (i.e. Qualifications, QuarterFinals, SemiFinals, etc)
* *Clear Access Point* - Remove the team programming from the AP (does not changed the 2.4 GHz radio). Useful in situations where a team needs to connect to their machine, but the AP is currently programmed to their team number (such as between finals matches)


