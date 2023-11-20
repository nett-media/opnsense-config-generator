import csv

def generate_xml_from_csv(csv_file, output_file, options):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Überspringt die Header-Zeile

        with open(output_file, 'w') as out_file:
            
            # adjust op_counter to match first free Opt Interface (depending on init_Interface.xml)
            opt_counter = options.get("opt_counter", 1)

            for row in reader:
                ip_range_base = row[1].strip().rsplit('.', 1)[0]  # IP-Adresse ohne letztes Oktett

                dhcp_from = f"{ip_range_base}.1"
                dhcp_to = f"{ip_range_base}.100"
                gateway = f"{ip_range_base}.254"
                dns_server = f"{ip_range_base}.254"
                failover_peer = f"{ip_range_base}.252"

                out_file.write(f'<opt{opt_counter}>\n')
                out_file.write(f'  <enable>1</enable>\n')
                out_file.write(f'  <failover_peerip>{failover_peer}</failover_peerip>\n')
                out_file.write(f'  <gateway>{gateway}</gateway>\n')
                out_file.write(f'  <ddnsdomainalgorithm>hmac-md5</ddnsdomainalgorithm>\n')
                out_file.write(f'  <numberoptions>\n    <item/>\n  </numberoptions>\n')
                out_file.write(f'  <range>\n    <from>{dhcp_from}</from>\n    <to>{dhcp_to}</to>\n  </range>\n')
                out_file.write(f'  <winsserver/>\n')
                out_file.write(f'  <dnsserver>{dns_server}</dnsserver>\n')
                out_file.write(f'  <ntpserver/>\n')
                out_file.write(f'</opt{opt_counter}>\n')
                
                opt_counter += 1


if __name__ == "__main__":
    csv_file = "config.csv"
    output_file = "part_DHCP.xml"
    generate_xml_from_csv(csv_file, output_file)