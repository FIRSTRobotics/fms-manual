.. include:: <isonum.txt>
.. _off-season-default:

Default Settings
======================

This article describes the default values of various settings in the FRC Offseason Simple image for the Linksys WRT1900 ACS AP.

Network
-------

Yellow "Internet" port: This port is configured with an IP of 192.168.1.1 (Note: The FRC Offseason Simple image is not intended to allow connectivity to the Internet from the field network by plugging an Internet connection into this port.). This port is intended as a maintenance connection in case any added firewall rules or network settings prevent access from the other interface.

4 "Ethernet" ports: These ports are bridged together and configured with an IP of 10.0.100.2

5GHz wireless: This network is bridged with the "Ethernet" network and accessible at the same 10.0.100.2 address

2.4GHz wireless: If enabled, this network is bridged with the "Ethernet" network and accessible at the same 10.0.100.2 address

DHCP
----

Yellow "Internet" port: DHCP disabled

4 "Ethernet" ports: DHCP enabled, will serve addresses on the 10.0.0.* subnet with a subnet mask of 255.0.0.0

5GHz wireless: same as "Ethernet"

Wireless
--------

5GHz Wireless

SSID: OffseasonFMS

Encryption: WPA2 AES

Key: DefaultKey

Channel: Auto

Width: 20MHz

Hidden SSID: No

2.4GHz Wireless

DISABLED BY DEFAULT

SSID: OffseasonFMS24

Encryption: WPA2 AES

Key: DefaultKey

Channel: Auto

Width: 20MHz

Hidden SSID: No

Firewall
--------

Firewall enabled by default with a default deny policy for traffic passing through. Allowed ports are the ports specified in the Game Manual, the network management ports allowed in the regular season firewall (e.g. ICMP, DHCP, etc.), plus the following additional ports:

* UDP 1110 - Used for DS->Robot traffic when not connected to FMS. This allows the AP to be used for non-FMS offseason scenarios

The default policy for traffic into/out of the AP (i.e. not through) is to allow. This allows you to connect to the AP webpage, SSH into the AP, etc.

This firewall policy means that many services will be blocked between the robot and DS such as SSH, code deploys, FMS controlling a DS connected wirelessly, etc.
