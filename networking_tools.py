#Imports
from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess
import socket

#Imported files
from system_tools import ipInfo

#--------------------------


def ping(host):
    result = subprocess.run(
        ['ping', '-c', '1', host],
        capture_output=True,
        text=True 
    )

    if result.returncode == 0:

        return True
    else:
        return False 


def dnsLookup(host):
    try:
        dns = socket.gethostbyname(host)
    except socket.gaierror:
        return 'Could not resolve host'

    return dns 

def portCheck(host, port):
        try: 
            port = int(port)
        except ValueError:
            return 'Port must be a number'
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)

        returnCode = s.connect_ex((host, port))

        s.close()

        if returnCode == 0: 
            return True
        else:
            return False

def networkScan():
    ip = ipInfo()
    semiIps = ip.split('.')
    validIps = []

    ips = []

    for lastOctet in range(1, 255): 
            full_ip = f'{semiIps[0]}.{semiIps[1]}.{semiIps[2]}.{lastOctet}'
            ips.append(full_ip)

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(ping, ip): ip for ip in ips}

        completed = 0

        for future in as_completed(futures):
            ip = futures[future]
            result = future.result()

            completed += 1

            print(f'Scanning {completed}/254', end='\r')

            if result:
                validIps.append(ip)

        print()
        return validIps

def trace(host):
    result = subprocess.run(
        ["traceroute", host],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return f'Could not find the trace route to {host}'

    lines = result.stdout.splitlines()

    hops = lines[1:]

    output = [f"Route to {host}:"]

    for hop in hops: 
        output.append(hop.strip())

    return "\n".join(output)

def returnDNS(ip):
    try:
        result =  socket.gethostbyaddr(ip)
        hostname = result[0]

        return f"IP: {ip}\nHostname: {hostname}"

    except socket.herror:
        return f"No hostname found for {ip}"