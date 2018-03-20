# cisco-prime-to-hospira-mednet-correlator
Hospira MedNet contains the ability for an IV pump to report the MAC address of the radio it has connected to.  This data is uploaded into MedNet and can be reported on through the software.  This can be helpful for trying to trace a pumps location within a facility so that someone looking for the pump knows a good vicinity of where to go.  

Issues:
 1. Cisco Prime reports only stores the base MAC address, not the incremental ones.  So an AP has a base of XX:XX:XX:XX:X0
 2. MedNet reports the incremental radio MAC address and not the base.  So a pump configured to connect to PumpNET reports the observed mac address as XX:XX:XX:XX:XY (Y being the controllers chosen incrementer for the specific SSID)
 3. Cisco Prime reports, even when modified, are not able to imported directly into Hospira MedNet to allow correlation
 
Solution:
 A script that can take a report from Cisco Prime and modify it in a way where it is ingestible by Hospira MedNet.  After importing, users of MedNet will see actual access point names instead of seemingly arbitrary mac addresses.
