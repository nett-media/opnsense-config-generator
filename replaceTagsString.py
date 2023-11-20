import xml.etree.ElementTree as ET

def find_tag_position(input_xml, tag_to_find):
    with open(input_xml, 'r') as file:
        content = file.read()

    start_tag_start_pos = content.find("<{}".format(tag_to_find))
    start_tag_end_pos = content.find(">", start_tag_start_pos) + 1  # Das Ende des Start-Tags
    end_tag_start_pos = content.find("</{}".format(tag_to_find))  # Der Anfang des End-Tags

    return start_tag_end_pos, end_tag_start_pos

def insert_content_to_tag(input_xml, tag_to_insert, replacement_content):
    with open(input_xml, 'r') as file:
        content = file.read()

    start_pos, end_pos = find_tag_position(input_xml, tag_to_insert)
    content = content[:start_pos] + "\n" + replacement_content + content[end_pos:]

    with open(input_xml, 'w') as file:
        file.write(content)

input_xml_file = "config-firewall1.dhw.xml"
tag_name = "vlans"
replacement_content_file = "part_VLAN.xml"

with open(replacement_content_file, 'r') as file:
    content = file.read()

insert_content_to_tag(input_xml_file, tag_name, content)
