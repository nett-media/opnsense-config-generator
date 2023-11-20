import csv
import uuid

def generate_xml_from_csv(csv_file, output_file, options):

 with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Überspringt die Header-Zeile

        # adjust op_counter to match first free Opt Interface (depending on init_Interface.xml)
        opt_counter = options.get("opt_counter", 1)

        with open(output_file, 'w') as outfile:
            for row in reader:
                vlan_nr = row[0].strip()
                vlan_uuid = str(uuid.uuid4())
                descr = row[2].strip()

                outfile.write(f'    <vlan uuid="{vlan_uuid}">\n')
                outfile.write(f'      <if>lagg0</if>\n')
                outfile.write(f'      <tag>{vlan_nr}</tag>\n')
                outfile.write(f'      <pcp>0</pcp>\n')
                outfile.write(f'      <proto/>\n')
                outfile.write(f'      <descr>{descr}</descr>\n')
                outfile.write(f'      <vlanif>vlan0{vlan_nr}</vlanif>\n')
                outfile.write(f'    </vlan>\n')

if __name__ == "__main__":
    csv_file = "config.csv"
    output_file = "part_VLAN.xml"
    generate_xml_from_csv(csv_file, output_file)