.. _pit-display-index:

Pit Display
===========

The Pit Display is a single page app that shows current rankings and tournament information to
spectators in the Pit at the venue. It is available on the local fieldside network and from the FRC Events web site.

Any recent computer running Chrome is supported for the Pit Display.  Connect the computer via ethernet, either to the
fieldside network via the Score Switch or to the internet. Whenever possible, use a wired Ethernet connection.
Using a wireless connection is not recommended.

Using the fieldside network is generally preferred to using the internet, as the fieldside version is not dependent
on FMS data sync to the cloud.

Loading the Pit Display
=======================

When on the fieldside network, navigate to the Field Server at http://10.0.100.5 and select the Pit Display option.

When on the internet, go to https://frc-events.firstinspires.org, navigate to the event rankings page, and append "/live" to the URL.
For example, for the 2026 PAPHI1 event, the URL is https://frc-events.firstinspires.org/2026/PAPHI1/rankings/live

The Pit Display is active during Qualification and Playoffs.  During Qualification rounds, it shows the current team rankings.  During the Playoffs, it shows the current
state of the Playoff bracket.

At any other time (for example during Practice matches, or before the Qualification schedule is activated) the Pit Display shows only the season background. It switches to the
rankings or the bracket on its own when the tournament level changes.

Languages
=========

When loaded from the Field Server, the Pit Display can be shown in one of seven languages:

* English
* Spanish
* French
* Portuguese
* Turkish
* Chinese (Simplified)
* Chinese (Traditional)

Choose the language when opening the display, either from the Pit Display dropdown in the Field Server navigation bar or from the language buttons in the Pit Display row of
the Field Server home page.

The language is part of the page address, so a display can also be opened or bookmarked directly in a language. For example, http://10.0.100.5/PitDisplay/Spanish opens the
display in Spanish. The language names used in the address are English, Spanish, French, Portuguese, Turkish, ChineseSimplified and ChineseTraditional, and must be typed
exactly as shown, including the capital letters. The address http://10.0.100.5/PitDisplay with no language opens the display in English.

The language is chosen separately on each screen, so different Pit Displays at the same event can use different languages. Changing the language on one display does not affect
any other display.