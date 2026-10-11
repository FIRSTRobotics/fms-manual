.. _event-wizard-alliance-selection:

Alliance Selection
======================

.. image:: images/alliance-selection-1.png

[**Green Box**] Settings for the Alliance Selection and Playoff Tournament. At all official FRC Events the 8-alliance tournament is used, 
but smaller Off-Season events may elect other formats. The current settings (as picked/downloaded on the Event Selection step) are displayed.

[**Blue Box**] Timing controls for the Alliance Selection "Pick Timer" - outlined in more detail below

[**Yellow Box**] The list of available teams for selection is shown and can be viewed sorted by Rank (default) or by team number (the "Teams by Team Number" tab), along with an "Accept" or "Decline" button on each team.

[**Red Box**] Use the Audience Video Control panel to manipulate the Audience Display(s)

The Scorekeeper populates the team numbers into the table on the center of the page by clicking the "Accept" button on the team to be populated. The current alliance spot that will be populated by clicking the "Accept" button is highlighted in blue. In the screenshot above, the current alliance spot to be filled is Alliance 1 Captain.

.. note::
    The "Accept" button on a team should only be clicked once they are guaranteed into that position (either because they accepted an invitation or because they're the captain of the alliance making the next selection).
    This means that at the beginning of the Alliance Selection process, only the Alliance #1 captain should be entered.

.. image:: images/alliance-selection-2.png
    :align: center

| 
| If a team declines a pick into an alliance, click the "Decline" button on that team. The team will then have a strikethrough on the Audience Display, unless they are a potential captain. The Accept and Decline buttons will go away for that team, replaced with red text saying "Declined" and a blue undo button. Clicking the blue undo button will undo the decline for that team and they will become available to be picked again.

.. note::
    If you click decline on a team that will then need to be put into a captain slot later, FMS will automatically undo the decline when they become the highest ranked available team and the next slot to fill is captain to allow you to click "Accept" and put them in that captain slot.

.. image:: images/alliance-selection-3.png
    :align: center

| 
| On all alliance member spots except for Captain, there will be a blue "Skip" button in addition to the blue box when that spot is the current spot to be filled. In the case of an alliance not making a pick in time, that alliance smember slot must be skipped until the end of the current round. In order to do this, click the "Skip" button on the alliance member slot.

.. note::
    If a mistake was made (wrong team accepted into an alliance or alliance member slot skipped when it shouldn't be), click the "Undo Last Selection" button on the bottom right side of the screen. This will undo the last team accepted into an alliance or the last alliance member slot that was skipped, in reverse order of how they ocurred.

Once the selection process is complete, click "Save Alliances" and move on to the next step of the Wizard.

Pick Timer
#################################

.. warning::
    The official timing and rules for the "Pick Timer" in Alliance Selection is outlined in the Tournament section (section 10) of the official Game Manual.

By default the Pick Timer is controlled by the FTA via the Head Referee panel (shown below), in which case the software controls will be disabled (shown on the left). 
In off-season events or when the hardware is unavailable, selecting "FMS" Timer Control will enable the software control buttons. 

.. image:: images/alliance-selection-4.png
    :align: center
    :width: 450

| 
| The buttons in the Head Referee panel directly mirror the FMS interface:

* The green "Play" button is the "Timer Start" button
* The red "Pause" button is the "Timer Pause" button
* The purple "Reset" button is the "Reset Pick Timer" button in the top of the green box
    
.. image:: images/alliance-selection-5.png
    :align: center
    :width: 500

The Reset button will automatically reset to the correct time based on which round of selections are in progress. 
Under normal operation, the Scorekeeper focuses on entering the Captain and selected team numbers into FMS while the 
FTA (or their designee) focuses on managing the Pick Timer.

The Scorekeeper starts and stops the timer during the scheduled breaks, which happen between the last Qualification match and the 
start of the Alliance Selection process as well as between each "round" of Alliance Selection. The can be started using the 2:00
and 8:00 buttons in the interface.

Editing Alliance Names and Members
##################################

Two red buttons above "Undo Last Selection" allow the alliances to be corrected by hand. Each requires :ref:`HQ approval <hq-approval>`, and both are disabled
once the Build Playoff Schedule step has been completed.

* "Edit Alliance Names" unlocks the name box of every alliance so that the names can be typed over. The new names are saved, and the boxes locked again, when "Save Alliances" is clicked.
* "Edit Alliance Members" replaces the team numbers in the alliance table with boxes that team numbers can be typed into directly. A valid team number is saved
  as soon as it is entered; there is no separate save step. A box is highlighted red when the number in it cannot be used, for example because the same team has
  been entered on another alliance. Click "Edit Alliance Members" again (approval is requested again) to return to the normal display.

"Undo Last Selection" remains the right tool for a mistake that has just been made. Use these buttons only at the direction of event support.

Set Field To Alliance Selection Mode
####################################

Each time the Alliance Selection step is opened, FMS puts the field into its Alliance Selection mode and sends the list of teams still available to the referee panels.
The "Set Field To Alliance Selection Mode" button does the same thing on demand. Use it if the field has been switched to another mode since the step was opened.
No password is required.

In the Off-Season version of the software the button is present but has no effect.

Fill Out BYE Alliances
######################

When an event has fewer alliances than the playoff bracket has places, the empty places can be filled with BYE alliances. Select all of the real alliances first,
then click "Fill Out BYE Alliances". The button is enabled only while at least one alliance has no captain and no playoff schedule has been generated.

A "Fill Out BYE Alliances?" message lists the alliance numbers that will become BYE alliances. Choose "Create BYEs" to continue. For each alliance that has no captain, FMS:

* Renames the alliance "BYE - " followed by its alliance number
* Fills it with placeholder teams taken from the Off-Season Demo Teams that have not been used in the Practice or Qualification schedule
* Marks those teams as competing, and gives them a WPA key if they do not have one

A "BYE Alliances Created" message then lists the placeholder teams placed on each alliance.

If an alliance without a captain already has a team in one of its other positions, or there are not enough unused Off-Season Demo Teams, FMS reports
"Unable to create BYE alliances", with the reason, and changes nothing.

Once the playoff schedule has been generated and activated, FMS offers to advance the real alliance automatically whenever a match against a BYE alliance comes up in :ref:`Match Play <match-play>`.
