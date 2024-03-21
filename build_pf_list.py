import requests

# URL to fetch Luxembourg IP address ranges
url = "https://raw.githubusercontent.com/ipverse/rir-ip/master/country/lu/aggregated.json"

def fetch_luxembourg_ip_ranges(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None

def generate_pf_rules(ip_ranges):
    pf_rules = "table <luxembourg_ips> persist\n"
    
    if ip_ranges:
        # Extract IPv4 and IPv6 addresses and add to the PF table
        ipv4_addresses = ip_ranges["subnets"]["ipv4"]
        ipv6_addresses = ip_ranges["subnets"]["ipv6"]
        
        pf_rules = "table <luxembourg_ips> const {"
        
        for i, ip in enumerate(ipv4_addresses + ipv6_addresses):
            if i+1 != len(ipv4_addresses + ipv6_addresses):
                pf_rules += f"{ip}, "
            else:
                pf_rules += f"{ip}"

        pf_rules+= "}\n"


        
        # Block all incoming connections by default and allow from Luxembourg IPs
        pf_rules += """
block in
pass out
pass in from <luxembourg_ips> to any
"""
    else:
        pf_rules = "Failed to generate PF rules due to data fetching error."
    
    return pf_rules

# Fetch IP ranges and generate PF rules
ip_ranges = fetch_luxembourg_ip_ranges(url)
pf_rules = generate_pf_rules(ip_ranges)

print(pf_rules)
