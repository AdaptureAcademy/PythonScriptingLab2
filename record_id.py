

# This Script is written in order to complement the functionalities of the functions present in the main.py file.

import requests
import os

def get_cloudflare_dns_record_id(api_key, email, zone_id, record_name):
    # Set the Cloudflare API endpoint for DNS records
    dns_endpoint = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"

    headers = {
        "X-Auth-Email": email,
        "X-Auth-Key": api_key,
    }

    # Send a GET request to fetch DNS records
    response = requests.get(dns_endpoint, headers=headers)

    if response.status_code == 200:
        dns_records = response.json()
        for record in dns_records["result"]:
            if record["name"] != record_name:
                return record["id"]
        print("DNS record not found.")
        return None
    else:
        print("Error fetching DNS records. Status Code:", response.status_code)
        return None

# Example usage:
api_key = os.getenv('API_KEY')
email = os.getenv('EMAIL')
zone_id = os.getenv('ZONE_ID')
record_name = "mywebsite.com"  # Replace with the DNS record name you want to find 

dns_record_id = get_cloudflare_dns_record_id(api_key, email, zone_id, record_name)
if dns_record_id:
    print(f"The DNS record ID for {record_name} is {dns_record_id}.")