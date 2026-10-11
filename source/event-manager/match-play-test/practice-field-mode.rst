.. _match-play-practice-field-mode:

Practice Field Mode
===================

Practice Field Mode is for running matches where the score does not matter, such as a field that is only used for
practice or a demonstration. It removes the scoring steps that would otherwise slow down the Commit of each match, so
matches can be cycled quickly without referees or scoring input.

.. warning::
   Every match committed while Practice Field Mode is enabled is recorded with all score data for both alliances set
   to zero. Anything entered by the referees or counted by the field for that match is discarded. Do not enable it for
   matches that "count."

.. note::
   Practice Field Mode is not the same thing as a Practice match or the Practice schedule, and it is not required in
   order to play Practice matches. Practice matches at an event are normally played with Practice Field Mode disabled,
   as described in the :ref:`Practice step <scorekeeper-practice>` of the Scorekeeper reference. It is also separate
   from the field type selected in :ref:`Multi-field Setup <settings-multi-field>`.

Enabling and Disabling
----------------------

Practice Field Mode is a toggle on the :ref:`Options tab <match-play-options>` of Match Play and Match Test. Change
the toggle and select *Save* for it to take effect. Like the other settings on the Options tab, it cannot be changed
while a match is in progress.

Enabling Practice Field Mode requires an HQ password / intervention. Disabling it does not.

The setting is shared between Match Play and Match Test, and it stays enabled when FMS is closed and reopened. FMS
disables it automatically when:

* a Qualification or Playoff schedule is :ref:`activated <event-wizard-activate-schedule>`
* a different event is made the active event

Activating a Practice schedule leaves the setting as it is.

What Changes
------------

While Practice Field Mode is enabled:

* *Commit* does not validate the scores. Instead, all score data for both alliances is cleared and the match is
  committed with a score of zero for each alliance.
* *Commit* does not wait for the referees. The warning that referees have not yet submitted scores is not shown, and
  the Commit button is styled as the next step as soon as the match ends.
* *Prestart with last settings*, in the :ref:`Prestart dropdown <match-play>`, is always available. Normally it can
  only be used to repeat a Prestart that has not changed. This option resets the field for a match without
  reprogramming the field network hardware, so it does not put a new set of teams on the field network. Use the
  regular Prestart when the teams change and their robots need to connect through the field.

The rest of the match flow is unchanged: the match is still run from Prestart through Post Results.

Qualification and Playoff Matches
---------------------------------

Practice Field Mode is intended only for Practice matches and Match Test. Because activating a Qualification or
Playoff schedule disables it, it will not normally be on during those matches.

If it has been enabled again after one of those schedules was activated, Prestart of a Qualification or Playoff match
shows a *Prestart Non-Standard match* confirmation stating that scoring validation is disabled and that all score data
will be set to zero upon commit. Unless *FIRST* HQ has directed otherwise, do not continue: close the confirmation
without prestarting, disable Practice Field Mode on the Options tab, and Prestart again.
