.. _event-wizard-regional-advancement:

Regional Advancement
======================

.. note::
    **Screenshot needed** — ``images/regional-advancement-1.png``: the whole step shortly after entering it,
    with the team list populated and the full row of buttons along the bottom visible.

At regional events, a number of Championship invitations are earned at the event itself. The Regional Advancement
step ranks every team at the event by regional points, works out which teams earn an invitation here, reveals
them to the audience, and publishes the result to *FIRST*.

This step is normally run at the very end of the event, after the playoff tournament and the awards ceremony.

.. note::
    Regional advancement applies only to regional events, in seasons where regional ranking is in use. FMS will
    refuse to calculate rankings for an event that is not a regional, or for a season that does not use the
    regional advancement model.

Before You Start
################

Advancement cannot be determined until the event is **complete**. FMS considers the event complete once the
Regional Winners, Regional Finalists, and *FIRST* Impact Award have all been assigned in
:ref:`event-wizard-award-assignment`.

Until then the "Determine Advancement", "Reveal Advancers", and "Publish Regional Advancement" buttons stay
disabled. "Recalculate Rankings" is available throughout, so the standings can be inspected at any point during
the event.

The Team List
#############

.. note::
    **Screenshot needed** — ``images/regional-advancement-2.png``: a close crop of the team list showing several
    ranked rows, ideally including at least one team with a qualifying status and one without.

Every team at the event is listed in rank order.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Column
     - Meaning
   * - Rank
     - The team's position at this event by total regional points.
   * - Team # / Team Name
     - The competing team.
   * - Total Points
     - The sum of the five point columns that follow, and what the rank is based on.
   * - Qualification
     - Points earned from the team's qualification ranking at this event.
   * - Alliance
     - Points earned for playoff alliance selection.
   * - Playoff
     - Points earned for the alliance's finish in the playoff tournament.
   * - Award
     - Points earned from awards won at this event.
   * - Team Age
     - Points based on how long the team has been competing.
   * - Status
     - Whether — and how — the team has qualified. See below.

The formula behind each point category is set by *FIRST* for the season; consult the season's advancement
documentation rather than inferring it from the totals shown here.

Status Values
#############

The Status column is blank (``None``) for every team until Determine Advancement has been run.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Status
     - Meaning
   * - ``PrequalifiedTeam``
     - The team already held a Championship invitation before this event.
   * - ``PriorEventQualifiedByRanking``
     - The team earned an invitation by regional points ranking at an earlier event.
   * - ``PriorEventQualifiedByAward``
     - The team earned an invitation by award at an earlier event.
   * - ``RegionalPoolQualified``
     - The team qualified from the regional points pool.
   * - ``EventQualifiedByRanking``
     - The team earned an invitation at this event by its regional points ranking.
   * - ``EventQualifiedByAward``
     - The team earned an invitation at this event by winning a qualifying award.
   * - ``NotEventQualified``
     - The team did not earn an invitation at this event.

.. note::
    **Draft — please confirm.** The status descriptions above are written from the values FMS displays. They
    should be checked against the season's advancement policy before this page is published, particularly the
    distinction between the pool and event-qualified statuses.

Running the Step
################

The buttons along the bottom of the screen are used roughly left to right, but the order that matters is
**Determine, then Reveal, then Publish**.

Recalculate Rankings
********************

Recalculates every team's regional points from current event data and refreshes the list. Use it whenever
results or awards have changed — it does not decide anything, so it is safe to run as often as needed.

This button is disabled once advancement has been published.

Determine Advancement
*********************

Recalculates the rankings and then works out which teams earn a Championship invitation at this event, filling
in the Status column for every team.

.. note::
    **Screenshot needed** — ``images/regional-advancement-3.png``: the "Regional Advancement Determined!"
    confirmation.

Determine Advancement can be run more than once — if an award or result is corrected, recalculate and determine
again. It is disabled once advancement has been published.

Reveal Advancers
****************

Switches the Audience Display to the advancing teams. FMS asks for confirmation first, because this is the moment
the teams find out:

.. note::
    **Screenshot needed** — ``images/regional-advancement-4.png``: the "Reveal Advancers?" confirmation dialog.

.. warning::
    Confirm the results are correct **before** revealing. Check with the FTA or event support staff if anything
    on the list looks wrong — once the audience has seen it, a correction is a very public one.

Publish Regional Advancement
****************************

Marks the results public, takes a full backup of the event database, and uploads the event data to *FIRST*, where
the advancement results become publicly visible.

.. note::
    **Screenshot needed** — ``images/regional-advancement-5.png``: the "Publish Regional Advancement?"
    confirmation dialog.

.. warning::
    Publishing is the point of no return for this step. Once the results are public, both "Recalculate Rankings"
    and "Determine Advancement" are disabled, so any correction after this point has to be handled by *FIRST* HQ.

If the event is not syncing with the cloud, FMS still marks the results public locally and takes the backup, but
nothing is uploaded until syncing is restored.

Audience Display Controls
#########################

Three buttons drive what the audience sees during the advancement portion of the ceremony:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Button
     - Shows
   * - Show Audience Background Screen
     - The standard event background, for use between segments.
   * - Show Audience Video Only Screen
     - The video feed with no FMS overlay.
   * - Show Previously Qualified Teams
     - Teams at this event that already held an invitation coming in.

"Show Previously Qualified Teams" is normally shown before the reveal, so the audience understands why some
high-ranked teams do not appear among the advancers.

.. note::
    **Screenshot needed** — ``images/regional-advancement-6.png``: the audience display showing the previously
    qualified teams.

.. note::
    **Screenshot needed** — ``images/regional-advancement-7.png``: the audience display showing the revealed
    advancing teams.

.. note::
    FMS Off-Season does not publish regional advancement. The button has no effect in an off-season build.
