import os
import importlib
import replaceTags
import shutil

MODULES = [
    {"order": 1, "part_name": "Interface",   "tag_path": "./interfaces"},
    {"order": 2, "part_name": "DHCP",        "tag_path": "./dhcpd"},
    {"order": 3, "part_name": "NAT",         "tag_path": "./nat/outbound"},
    {"order": 4, "part_name": "Rules",       "tag_path": "./filter"},
    {"order": 5, "part_name": "CARP",        "tag_path": "./virtualip"},
    {"order": 6, "part_name": "VLAN",        "tag_path": "./vlans"},
    {"order": 7, "part_name": "RadiusUser",  "tag_path": "./OPNsense/freeradius/user/users"},
    
]


def generateParts(csv_file):
    for module_info in MODULES:
        module_name = "gen" + module_info["part_name"]
        # eg. import genDHCP
        module = importlib.import_module(module_name)
        # eg. part2_DHCP.xml
        xml_file = f"export/part{module_info['order']}_{module_info['part_name']}.xml"
        print(f"generating {xml_file}..")
        module.generate_xml_from_csv(csv_file, xml_file, options)

def insertPartsToConfig(xml_config_file):
    generated_xml_file =  f"export/{xml_config_file}"
    shutil.copy2(xml_config_file, generated_xml_file)
    for module_info in MODULES:
        #file_names = [f"init/init_{module_info['part_name']}.xml", f"export/part{module_info['order']}_{module_info['part_name']}.xml"]
        #file_names = [ f"export/part{module_info['order']}_{module_info['part_name']}.xml"]
        init_file = f"init/init_{module_info['part_name']}.xml"
        export_file = f"export/part{module_info['order']}_{module_info['part_name']}.xml"
        file_names = [init_file, export_file] if os.path.exists(init_file) else [export_file]

        print(f"inject {file_names} into {generated_xml_file}")  
        
        replaceTags.modify_xml(generated_xml_file, module_info["tag_path"], file_names)

if __name__ == "__main__":
    # adjust according to your csv config file name
    csv_file = "config.csv" 
    # op_counter to match first free Opt Interface (depending on init_Interface.xml)
    # wan1-3 for manual nat
    options = { "firewallNr": 1, "opt_counter": 6, "wan1": "10.11.12.11", "wan2": "10.11.12.12", "wan3": "10.11.12.13"}
    generateParts(csv_file)

    # adjust according to your opnsense config file name
    xml_config_file = "config-example.xml"
    #xml_config_file = "config-firewall1.dhw.xml"
    insertPartsToConfig(xml_config_file)
    print("done!")
