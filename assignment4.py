import nmap

def port_scanner():
   p=nmap.PortScanner();
   p.scan(ports,'21-1000');
   for host_names in p.all_hosts():
       ports=p[host_names].get('tcp');
       write_to_file(ports);
   return ports;
def write_to_file(contents):
   m=open('write_to_file','My_File');
   m.write(str(contents));
 pass

def main():
    sites[
    'google.com','yahoo.com','salamdl.info'
    ]
    for s in sites:
        port_scanner(s);

main()