import csv
import uuid
import random
import string

def generate_random_password(length=32):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def generate_xml_from_csv(csv_file, output_file, options):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Überspringt die Header-Zeile

        with open(output_file, 'w') as out_file:

            opt_counter = options.get("opt_counter", 1)
            firewall_number = options.get('firewallNr', 1)  # Wenn firewallNr nicht angegeben ist, verwenden wir 1 als Standardwert
            advskew = "0" if firewall_number == 1 else "100"

            for row in reader:
                vlan_nr = row[0].strip()
                ip_range = row[1].strip().replace(".x", ".254")
                description = row[2].strip()
                random_uuid = str(uuid.uuid4())
                random_password = generate_random_password()

                out_file.write(f'  <vip uuid="{random_uuid}">\n')
                out_file.write(f'    <interface>opt{opt_counter}</interface>\n')
                out_file.write(f'    <mode>carp</mode>\n')
                out_file.write(f'    <subnet>{ip_range}</subnet>\n')
                out_file.write(f'    <subnet_bits>24</subnet_bits>\n')
                out_file.write(f'    <gateway/>\n')
                out_file.write(f'    <noexpand>0</noexpand>\n')
                out_file.write(f'    <nobind>0</nobind>\n')
                out_file.write(f'    <password>{random_password}</password>\n')
                out_file.write(f'    <vhid>{vlan_nr}</vhid>\n')
                out_file.write(f'    <advbase>1</advbase>\n')
                out_file.write(f'    <advskew>{advskew}</advskew>\n')
                out_file.write(f'    <descr>{description}</descr>\n')
                out_file.write(f'  </vip>\n')

                opt_counter += 1


if __name__ == "__main__":
    csv_file = "config.csv"
    output_file = "part_CARP.xml"
    generate_xml_from_csv(csv_file, output_file)