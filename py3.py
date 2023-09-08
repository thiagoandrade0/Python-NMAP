import nmap

def scriptnmap(pc):
    scan_nmap = nmap.PortScanner()
    scan_nmap.scan(pc, arguments='-p-')

    for host in scan_nmap.all_hosts():
        print(f"Escaneando portas do {host}:")
        for proto in scan_nmap[host].all_protocols():
            ports = scan_nmap[host][proto].keys()
            for port in ports:
                service = scan_nmap[host][proto][port]['name']
                print(f"Porta {port}/{proto} Aberta | Servico {service}")

if __name__ == "__main__":
    pc = input("Digite o IP: ")
    scriptnmap(pc)
