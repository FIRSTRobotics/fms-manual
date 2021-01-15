.. include:: <isonum.txt>

Overview
========

The Wireless Acess Point used for 2017 FRC\ |reg| competitions was a Linksys 1900ACS running customized OpenWRT firmware. In an attempt to provide a tested AP that can be used with FMS Offseason, we are releasing a modified version of the firmware used during the season that teams or individuals could load on their own devices.

This page provides an overview of the images. For download and installation information, please see `Loading OpenWRT. <../../offseason/l/755140-loading-openwrt>`_

While we have not yet had any issues with a device that could not be recovered using the `Recovery Procedure <../../offseason/l/756905-recovery-procedure>`_ in the 80+ devices we have flashed this season, please note that loading new firmware on a device or modifying device settings always carries some level of risk. Additionally, loading non-manufacturer provided firmware onto the device may invalidate your warranty.

The OpenWRT build used during the FRC season contained a specific set of drivers (including a specific patch developed to address an issue that was seen when used with the OM5P-AC) and modules that was tested to work with the OpenMesh OM5P-AN and OM5P-AC radios. This build also contained a set of default settings such as usernames and passwords, network configurations, and firewall configuration, that matched the desired configuration for the 2017 FRC season.

For offseason use, we are releasing 2 modified versions of our image that have been customized for specific use cases.

Offseason Simple
----------------

The Offseason Simple image has been modified to be used either standalone, or with FMS Offseason.

This image contains the same software used in the 2017 season image, but with the following modifications:

* Username and Password have been reset to the default of root/root
* Network configuration has been modified to a simplified, non-VLAN configuration
* Network configuration "flipped" (management network moved to single port) to better accomodate offseason or multi-computer use cases using the built-in switch.
* Wireless network has been simplified to a single SSID on each frequency (compared to 1 SSID per robot which is reconfigured each match)
* Firewall has been modified to allow access to the AP webpage/ssh from the single network and to allow the Non-FMS DS->Robot Control traffic through.

If you are looking for an image to use the Linksys 1900ACS with FRC robots and aren't sure which one you need, you very likely want Offseason Simple.

Offseason VLAN
--------------

The Offseason VLAN image contains the same software used in the 2017 season image, but with the following modifications:

* Username and Password have been reset to the default of root/root
