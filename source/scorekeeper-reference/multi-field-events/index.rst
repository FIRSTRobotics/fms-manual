.. _scorekeeper-multi-field-events:

Multi-field Events
==================

At some events, such as the *FIRST* Championship, one event is played on two fields at the same time. Each field has
its own FMS server and its own Scorekeeper, but the two servers run as a single event. This page explains how that
works and what each Scorekeeper can and cannot do.

Multi-field operation is set up by FRC Engineering. It is not available in Off-Season FMS, and the field type cannot
be changed without FRC Engineering authorization.

Field Types
-----------

Every FMS server has a field type, set on the :ref:`Multi-field Setup <settings-multi-field>` tab. The field type
belongs to the server, not to the event: it stays the same when a different event is made active.

**Primary**
   The default, and the only field type used at a single-field event. At a multi-field event, the Primary field holds
   the event and is the only server that can set it up and change it. FMS sometimes refers to it as *Field #1*.

**Secondary**
   The second competition field. It plays its share of the event's matches, but it gets all of its event data from
   the Primary field.

**Practice**
   A practice field that is not part of the event's schedule. It can run Match Test and Field Test, and it gets its
   data from the Primary field. It does not follow what the other fields are doing.

The field type is separate from Practice Field Mode on the Match Play Options tab, and from the Practice schedule.

How the Fields Work Together
----------------------------

One Event Database
~~~~~~~~~~~~~~~~~~

The Primary field holds the only copy of the event. When the Secondary or Practice field loads a schedule, commits a
match or edits a score, it reads from and writes to the Primary field's database over the network between the field
servers. The Secondary field has no event data of its own.

Most of the rules on this page follow from that: anything that changes how the event is set up happens on the Primary,
and the Secondary cannot work without a connection to the Primary.

Which Field Plays Which Match
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the Primary field generates a schedule, it alternates matches between the fields: match 1 is assigned to the
Primary field, match 2 to the Secondary, match 3 to the Primary, and so on. At the *FIRST* Championship, Final 2 and the
Final tiebreaker are always assigned to the Primary field.

Each field moves through only its own matches. When a match is committed, each field advances to the next unplayed
match *assigned to that field*, so the two fields show different "next" matches.

If you Prestart a match that is assigned to the other field, FMS asks *"Start Match on <field> field?"* and states which
field the match is scheduled for. Cancel unless the Head Referee and FTA have agreed to move the match to your field.

Tournament Level
~~~~~~~~~~~~~~~~

The Primary field sets the tournament level for the whole event. When the Scorekeeper on the Primary field activates a
schedule or changes the tournament level, the Secondary field follows: it reloads Match Play or Match Test at the new
level, even if the Secondary Scorekeeper did nothing. Coordinate level changes between the two Scorekeepers before
making them, and do not change the level while the Secondary field is running a match.

Each field shows the other field's match status changes in its Schedule tab.

Playoffs
~~~~~~~~

When a Playoff match is committed on the Secondary field, the Primary field updates the playoff bracket and sends the
updated schedule to both fields. Wait for the next match to appear on the schedule before you Prestart it.

Test Matches
~~~~~~~~~~~~

Each field type uses its own match number in :ref:`Match Test <match-play-test>`, so test matches on different fields
do not overwrite each other:

====================  ============
Field type            Test match
====================  ============
Primary               999
Secondary             998
Practice              997
====================  ============

What Each Field Can Do
----------------------

=============================================  =========  =========  =========
Function                                       Primary    Secondary  Practice
=============================================  =========  =========  =========
Event Wizard, including schedule generation    Yes        No         No
Reports                                        Yes        No         No
Match Play                                     Yes        Yes        No
Match Test                                     Yes        Yes        Yes
Match Review, including score edits            Yes        Yes        No
Field Test                                     Yes        Yes        Yes
Event database backups                         Yes        No         No
Upload of results to *FIRST*                   Yes        No         No
=============================================  =========  =========  =========

Functions that a field cannot use are unavailable in its menus. Anything in the left column marked *No* for your field
must be done by the Primary field's Scorekeeper.

Backups and Results Upload
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Primary field backs up the event database and uploads results to *FIRST* for **both** fields' matches. When the
Secondary field commits or posts a match, the Primary field receives a notification and does the backup and upload
itself.

If the Primary field's FMS is not running, the Secondary field's matches are not backed up or uploaded.
:ref:`Backups <settings-backup>` and :ref:`Data Sync <settings-data-sync>` are configured only on the Primary field.

Operational Constraints
-----------------------

Starting FMS
~~~~~~~~~~~~

The Secondary and Practice fields need the Primary field's server to be reachable. When FMS starts on either of them,
it pings the Primary field's address (``192.168.100.10``). If it gets no answer, it shows:

   *This server is configured as a secondary or practice field, but is unable to ping the primary field IP address
   (192.168.100.10). Press Yes to retry the ping or No to reset the field to primary.*

.. warning::
   Do not press *No* at an event. *No* changes this server's field type to Primary, which disconnects it from the
   event; setting it back requires FRC Engineering. Press *Yes* to retry, and contact the FTA if the Primary field
   still cannot be reached.

Start the Primary field's server first, and have it running with the multi-field event active, before starting FMS
on the other fields. The Primary field begins listening for the Secondary field's commits only once a multi-field event
is active.

Network Between Fields
~~~~~~~~~~~~~~~~~~~~~~

The field servers connect to each other over a separate inter-field network, apart from each field's own field
network:

====================  ====================
Field type            Address
====================  ====================
Primary               ``192.168.100.10``
Secondary             ``192.168.100.20``
Practice              ``192.168.100.30``
====================  ====================

Each field still runs its own field network and robots. Only event data and match notifications cross between the
servers.

If the Connection Is Lost
~~~~~~~~~~~~~~~~~~~~~~~~~

Because the Secondary field keeps no event data of its own, it cannot load the schedule, commit a match or edit a
score while it is disconnected from the Primary field. If the connection drops:

* Do not keep starting matches on the Secondary field. Hold the field and contact the FTA.
* If a match on the Secondary field ended but could not be committed, do not discard it. Once the connection is
  restored, commit it and confirm that it appears in the Primary field's schedule.
* After the connection is restored, confirm with the Primary field's Scorekeeper that the Secondary field's recent
  matches show as committed and posted on the Primary field.

Checking the Setup
------------------

On the Secondary or Practice field, the :ref:`Multi-field Setup <settings-multi-field>` tab has a *Test Connection*
button. It reports which multi-field event the Primary field has active, or that the Primary field does not have a
multi-field event active. Use it before the first match of each day to confirm that both fields are on the same event.
