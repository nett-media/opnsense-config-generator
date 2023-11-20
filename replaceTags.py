from lxml import etree

def modify_xml(input_xml, tag_path, file_names):
    # Haupt-XML-Datei einlesen
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(input_xml, parser)
    root = tree.getroot()

    # Finden Sie den ersten <tag_to_replace>-Tag im Hauptdokument
    #target_elem = root.find(f".//{tag_to_replace}")
    target_elem = root.find(f"{tag_path}")

    if target_elem is not None:

        # Alle Kinder von <tag_to_replace> entfernen
        for child in list(target_elem):
            target_elem.remove(child)

        # Einrückung nach dem Öffnungstag von <tag_to_replace>
        target_elem.text = "\n    "  

        for file_name in file_names:
            # Ersatz-XML einlesen
            with open(file_name, 'r') as f:
                replacement_content = f.read()

            # Ersatzinhalt als XML-Elemente hinzufügen
            replacement_elems = etree.fromstring(f"<root>{replacement_content}</root>")
            for elem in replacement_elems:
                target_elem.append(elem)

        # Änderungen in derselben XML-Datei speichern
        tree.write(input_xml, pretty_print=True, xml_declaration=True, encoding='utf-8')


if __name__ == "__main__":

    input_xml_file = "config-firewall1.xml"
    tag_path = "./vlans"
    part_name = "VLAN"
    part = 6
    file_names = [f"init_{part_name}.xml", f"part{part}_{part_name}.xml"]
    modify_xml(input_xml_file, tag_path, file_names)
