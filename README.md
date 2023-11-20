## OPNsense Config Generation

Scripts and Snippets to batch create VLANs, Interfaces, DHCP Server, CARP IP, NAT, Firewall Rules and Radius User (if freeradius is installed) for OPNsense, based on a config.csv file.

In config.csv there are 3 rows: VLAN TAG, IP Range and Description.

For each line in the csv file, a config Part will be created (Vlan, Interface, DHCP Server, CARP IP, NAT, Firewall Rules and Radius User)

Despite the generated parts from the config.csv file, there is also the possibility to use predefined "init" configs for each part (look inside `init` folder), but these "init" config files are optional.

The `generateXMLConfig` script generates all parts and then inject them into a backup config file from the firewall.


## Steps:

* put OPNsense backup config.xml into root folder (aka here)
* create/modify config.csv (see config-example for reference) 
* create/modify init parts (in `init` folder)
* generate config.xmv by running `generateXMLConfig.py` script
* generated config.xml will be inside `export` folder along with all generated parts


## Example:

```
$ python generateXMLConfig.py                                                                                       ✔ 
generating export/part1_Interface.xml..
generating export/part2_DHCP.xml..
generating export/part3_NAT.xml..
generating export/part4_Rules.xml..
generating export/part5_CARP.xml..
generating export/part6_VLAN.xml..
generating export/part7_RadiusUser.xml..
inject ['init/init_Interface.xml', 'export/part1_Interface.xml'] into export/config-example.xml
inject ['init/init_DHCP.xml', 'export/part2_DHCP.xml'] into export/config-example.xml
inject ['init/init_NAT.xml', 'export/part3_NAT.xml'] into export/config-example.xml
inject ['init/init_Rules.xml', 'export/part4_Rules.xml'] into export/config-example.xml
inject ['init/init_CARP.xml', 'export/part5_CARP.xml'] into export/config-example.xml
inject ['init/init_VLAN.xml', 'export/part6_VLAN.xml'] into export/config-example.xml
inject ['export/part7_RadiusUser.xml'] into export/config-example.xml
done!
```