import csv
import uuid
import time
from sanitizeDescription import escape_string

def generate_xml_from_csv(csv_file, output_file, options):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Überspringt die Header-Zeile

        #firewall_number = options.get('firewallNr', 1)  # Wenn firewallNr nicht angegeben ist, verwenden wir 1 als Standardwert
        
        with open(output_file, 'w') as outfile:
            for row in reader:
                vlan_nr = row[0].strip()
                random_uuid = str(uuid.uuid4())
                description = row[2].strip()


                username = str(f'top{vlan_nr}') 
                password =  escape_string(description)

                outfile.write(f'        <user uuid="{random_uuid}">\n')
                outfile.write(f'          <enabled>1</enabled>\n')
                outfile.write(f'          <username>{username}</username>\n')
                outfile.write(f'          <password>{password}</password>\n')
                outfile.write(f'          <description>{description}</description>\n')
                outfile.write(f'          <ip/>\n')
                outfile.write(f'          <subnet/>\n')
                outfile.write(f'          <route/>\n')
                outfile.write(f'          <ip6/>\n')
                outfile.write(f'          <vlan>{vlan_nr}</vlan>\n')
                outfile.write(f'          <logintime/>\n')
                outfile.write(f'          <simuse/>\n')
                outfile.write(f'          <exos_vlan_untagged/>\n')
                outfile.write(f'          <exos_vlan_tagged/>\n')
                outfile.write(f'          <exos_policy/>\n')
                outfile.write(f'          <wispr_bw_min_up/>\n')
                outfile.write(f'          <wispr_bw_max_up/>\n')
                outfile.write(f'          <wispr_bw_min_down/>\n')
                outfile.write(f'          <wispr_bw_max_down/>\n')
                outfile.write(f'          <chillispot_bw_max_up/>\n')
                outfile.write(f'          <chillispot_bw_max_down/>\n')
                outfile.write(f'          <mikrotik_vlan_id_number/>\n')
                outfile.write(f'          <mikrotik_vlan_id_type/>\n')
                outfile.write(f'          <sessionlimit_max_session_limit/>\n')
                outfile.write(f'          <servicetype/>\n')
                outfile.write(f'          <linkedAVPair/>\n')
                outfile.write(f'        </user>\n')


                #opt_counter += 1


if __name__ == "__main__":
    csv_file = "config.csv"
    output_file = "part_RadiusUsers.xml"
    generate_xml_from_csv(csv_file, output_file, {})
