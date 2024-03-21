import requests
import click


def fetch_ip_ranges(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None

def generate_pf_rules(ip_ranges, country):
    pf_rules = "table <luxembourg_ips> persist\n"
    
    if ip_ranges:
        # Extract IPv4 and IPv6 addresses and add to the PF table
        ipv4_addresses = ip_ranges["subnets"]["ipv4"]
        ipv6_addresses = ip_ranges["subnets"]["ipv6"]
        
        pf_rules = f"table <{country}_ips> const {{"
        
        for i, ip in enumerate(ipv4_addresses + ipv6_addresses):
            if i+1 != len(ipv4_addresses + ipv6_addresses):
                pf_rules += f"{ip}, "
            else:
                pf_rules += f"{ip}"

        pf_rules+= "}\n"


        
        # Block all incoming connections by default and allow from Luxembourg IPs
        pf_rules += f"""
block in
pass out
pass in from <{country}_ips> to any
"""
    else:
        pf_rules = "Failed to generate PF rules due to data fetching error."
    
    return pf_rules


@click.command()
@click.option('--country', required=True, type=click.STRING , help='Specify the country codes for which you want to allow access.')
def cli(country):
    url = f"https://raw.githubusercontent.com/ipverse/rir-ip/master/country/{country}/aggregated.json"
    ip_ranges = fetch_ip_ranges(url)
    pf_rules = generate_pf_rules(ip_ranges, country)
    print(pf_rules)


if __name__ == '__main__':
    cli()
