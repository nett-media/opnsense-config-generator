import csv
from sanitizeDescription import escape_string

def generate_xml_from_csv(csv_file, output_file, options):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Überspringt die Header-Zeile

         # adjust op_counter to match first free Opt Interface (depending on init_Interface.xml)
        opt_counter = options.get("opt_counter", 1)
        firewall_number = options.get('firewallNr', 1)  # Wenn firewallNr nicht angegeben ist, verwenden wir 1 als Standardwert
        ip_suffix = 250 + firewall_number  # z.B. firewallNr: 1 -> 251, firewallNr: 2 -> 252

        with open(output_file, 'w') as outfile:
            for row in reader:
                vlan_nr = row[0].strip()
                ip_address = row[1].strip().replace(".x", f".{ip_suffix}")
                description = escape_string(row[2].strip())

                outfile.write(f'<opt{opt_counter}>\n')
                outfile.write(f'  <if>vlan0{vlan_nr}</if>\n')
                outfile.write(f'  <descr>V{vlan_nr}_{description}</descr>\n')
                outfile.write(f'  <enable>1</enable>\n')
                outfile.write(f'  <spoofmac/>\n')
                outfile.write(f'  <ipaddr>{ip_address}</ipaddr>\n')
                outfile.write(f'  <subnet>24</subnet>\n')
                outfile.write(f'</opt{opt_counter}>\n')

                opt_counter += 1


if __name__ == "__main__":
    csv_file = "config.csv"
    output_file = "part_Interface.xml"
    options = {'firewallNr': 1}
    generate_xml_from_csv(csv_file, output_file, options)

