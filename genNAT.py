import csv
import uuid
import time

def generate_xml_from_csv(csv_file, output_file, options):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Überspringt die Header-Zeile

        # adjust op_counter to match first free Opt Interface (depending on init_Interface.xml)
        opt_counter = options.get("opt_counter", 1)

        with open(output_file, 'w') as outfile:
            for row in reader:
                vlan_nr = row[0].strip()
                description = row[2].strip()
                wan = row[3].strip()
                random_uuid = str(uuid.uuid4())

                timestamp = time.time()
                formatted_timestamp = "{:.4f}".format(timestamp)

                wan_ip =""
                match wan:
                    case "1": 
                        wan_ip = options.get("wan1", "80.200.10.11")
                    case "2": 
                        wan_ip = options.get("wan2", "80.200.10.12")
                    case "3": 
                        wan_ip = options.get("wan3", "80.200.10.13")
                
                outfile.write(f'<rule>\n')
                outfile.write(f'  <source>\n')
                outfile.write(f'    <network>opt{opt_counter}</network>\n')
                outfile.write(f'  </source>\n')
                outfile.write(f'  <destination>\n')
                outfile.write(f'    <any>1</any>\n')
                outfile.write(f'  </destination>\n')
                outfile.write(f'  <descr>{description}</descr>\n')
                outfile.write(f'  <category/>\n')
                outfile.write(f'  <interface>wan</interface>\n')
                outfile.write(f'  <tag/>\n')
                outfile.write(f'  <tagged/>\n')
                outfile.write(f'  <poolopts/>\n')
                outfile.write(f'  <poolopts_sourcehashkey/>\n')
                outfile.write(f'  <ipprotocol>inet</ipprotocol>\n')
                outfile.write(f'  <created>\n')
                outfile.write(f'    <username>root@10.1.1.1</username>\n')
                outfile.write(f'    <time>{formatted_timestamp}</time>\n')
                outfile.write(f'    <description>genNAT.py made changes</description>\n')
                outfile.write(f'  </created>\n')
                outfile.write(f'  <target>{wan_ip}</target>\n')
                outfile.write(f'  <sourceport/>\n')
                outfile.write(f'  <updated>\n')
                outfile.write(f'    <username>root@10.1.1.1</username>\n')
                outfile.write(f'    <time>{formatted_timestamp}</time>\n')
                outfile.write(f'    <description>genNAT.py made changes</description>\n')
                outfile.write(f'  </updated>\n')
                outfile.write(f'</rule>\n')

                opt_counter += 1


if __name__ == "__main__":
    csv_file = "config.csv"
    output_file = "part3_NAT.xml"
    generate_xml_from_csv(csv_file, output_file)
