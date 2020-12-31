Team Selection
==============

.. _wpa_kiosk:

View and Add Registrations
##########################

.. image:: images/team-selection-1.png


Team Selection displays the downloaded list of registered FRC teams, with those registered for the event pre-checked. This list should be used to verify all the teams registered are actually present at the venue.

[Red] Checkboxes indicate the registration status of a particular team at a particular event. If the box is checked, the team on that row is set as "competing" for the event. Unchecked teams are not listed as competitors.

[Green] The count of competing teams is shown (number of checked teams) along with the ability to filter the team list. Radio buttons can also be used to switch the view list from all FRC Teams (All) to just those that are checked (Competing Only)

[Blue] The "new" and "edit" buttons can be used to add unofficial teams for Off-Season use. These are disabled at official events.

Note that having any teams that were manually added (using "New") checked as competing teams (red column) will prevent data from being sent to FIRST (scores, results, etc) and therefore is not available in-season.

Adding Off-Season Teams (Optional)
##################################

.. image:: images/team-selection-2.png

If additional teams are needed at an off-season event, the "new" button (blue box above) can be used to create a custom team. The team number (red arrow) must be unique. Make sure the team is checked as competing once created. Only teams added manually can be edited, those downloaded from FIRST are protected from edits.

Events with custom teams cannot sync with FIRST servers.

NOTE: Teams 9985 to 9999 are "pre-loaded" Teams that, while not "official teams" in FRC, can be used during the Off-Season at an event without disabling the ability to Sync with FIRST servers.


Generate Security Keys
######################

.. image:: images/team-selection-3.png

Once the teams competing at the event have all been selected, and proper number is displayed under "Total Competing Teams", security keys should be generated for use by the field. This is done using the "Generate Security Keys" (black arrow) button. Once keys are generated, a success message will be displayed and (green arrow) the "Key Generated" column will display the new status of "True".

If additional teams are added later, the same button can be used to generate keys for those new teams- teams with existing keys will remain untouched.

Once the keys are generated, the FTA should use the WPA Kiosk program on the WPA Laptop to download keys from FMS to the kiosk program. This download process will require FTA authentication.

As a backup, if the automatic download is unavailable, Select Export Keys (blue arrow) to save the key file needed to program the keys into the Radio Kiosk used by teams to program their robot radios. This should only be used by the FTA, as it requires their password to complete.

* After WPA security keys have been distributed to the teams, it is important to not require these codes to be redistributed and reprogrammed. 
  Teams that already have a key do not receive a new one when the Generate Security Keys button is pressed.
  The Qualification and Playoff schedule generation steps assume that all teams will use the same security keys throughout the event; as a result, performing Keys steps is not necessary to repeat on those steps of the Wizard.	

If necessary, the Clear All Keys button (red arrow) can be used to return all teams to their default, keyless, state. This should only be used carefully, as any programmed radios would need to be re-done. This action requires the FTA password.

WPA Kiosk Key Download
######################

As noted above, once security keys have been generated, they can be downloaded to the WPA Kiosk before beginning to program team radios. To do this, attach the radio kiosk computer to the field network (using the scoring table switch or the switch in the SCC) and launch the WPA Kiosk program. Repeat this process for each computer that will be used to program team radios.

Note: downloading keys will require FTA Authentication. At an off-season event, use the code "0000" to bypass the FTA Authentication.

For information on the WPA Kiosk, please see this :ref:`wpa-kiosk-setup`.