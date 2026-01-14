.. include:: <isonum.txt>
.. _scorekeeper-non-standard-playoffs:

Non-Standard Playoffs
======================

Overview
--------

In some cases, an event may not have enough teams to fill 8 Alliances for playoffs while also having at least 1 team available to be called in as a backup. This page will go over the process for setting up FMS to handle that and executing the processes during playoffs.

Determine number of Alliances
-----------------------------

The recommendation from *FIRST* is that there should be at least one team in the backup pool for the start of playoffs. In order to meet that criteria, an event will need the following number of teams for each desired amount of alliances:

* 4 Alliances: At least 13 teams
* 5 Alliances: At least 16 teams
* 6 Alliances: At least 19 teams
* 7 Alliances: At least 22 teams
* 8 Alliances: At least 25 teams

Do I need to do anything before or during Qualification matches?
----------------------------------------------------------------

No. Set up and run through Qualification matches as you would in every other event. The entirety of this process is after Qualification matches are complete.

After completion of all Qualification matches
---------------------------------------------

* Open the Event Wizard, Qual Team Selection. 
* In the Team Number filter, type "99" and the team list should show teams 9975 - 9999 "Off-Season Demo Team". 
* Click the checkbox on the number of teams needed to get to 8 alliances, with 3 for each alliance.
* Click "Save Event Participants"
* These teams are now available to be placed into alliances during Alliance Selection to get to 8 alliances.

During Alliance Selection
-------------------------

Go through the normal Alliance Selection process, but when you get to the alliances that are "extra" fill those spots in with these Off-Season Demo Teams

.. note::
    The Off-Season Demo Teams will not have any ranking data, so they will only appear in the "Teams by Team Number" list.

During Playoffs
---------------

When you get to a match that includes one of these alliances with the Off-Season Demo Teams, follow the below process:

.. note::
    "Real" teams do not compete in these matches because they are bye matches. Do not have them queue up for these matches!

* Before Pre-Starting the match, go to the Options tab in Match Play.
* Change the Teleop Time to 5 seconds and click the Save button below.
* Pre-Start the match and Bypass all teams in the match.
* Once you get the all clear from the FTA, start the match and let it run out.
* Fill in "No" or the equivalent for all teams for auto and endgame (where applicable, season dependent) to fulfill the score validation on Commit.
* Use the "Adjust" field in the bottom right to increase the score by one point for the alliance with the "real" teams so that they win the match.
* Commit the match, then use the "Post Without Display" option in the Post Results dropdown menu.
* If the next match is a "real" match between 6 "real" teams, go back to the Options tab and click the "Restore Defaults" button.

This process will get through the bye matches quickly and "eliminate" the Off-Season Demo Team alliances after they each lose two matches.