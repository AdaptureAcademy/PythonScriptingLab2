import requests
import json


# Delete a DNS Record on Cloudflare 
def delete_cloudflare_dns_record(api_key, email, zone_id, record_id):
    # Set the Cloudflare API endpoint for the specific DNS record
    dns_endpoint = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"

    headers = {
        "X-Auth-Email": email,
        "X-Auth-Key": api_key,
        "Content-Type": "application/json",
    }

    # Send a DELETE request to delete the DNS record
    response = requests.delete(dns_endpoint, headers=headers)

    if response.status_code == 200:
        print("DNS record deleted successfully.")
    else:
        print("Error deleting DNS record. Status Code:", response.status_code)
        print("Response:", response.text)


def create_cloudflare_dns_record(api_key, email, zone_id, dns_record_data):
    # Set the Cloudflare API endpoint for DNS records
    dns_endpoint = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"

    

    headers = {
        "X-Auth-Email": email,
        "X-Auth-Key": api_key,
        "Content-Type": "application/json",
    }

    # Send a POST request to create the DNS record
    response = requests.post(dns_endpoint, data=json.dumps(dns_record_data), headers=headers)

    if response.status_code == 200:
        print("DNS record created successfully.")
    else:
        print("Error creating DNS record. Status Code:", response.status_code)
        print("Response:", response.text)





def fetch_cloudflare_dns_records(api_key, email, zone_id):
    # Set the Cloudflare API endpoint for DNS records
    dns_endpoint = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"

    headers = {      
    "X-Auth-Email": email,
    "X-Auth-Key": api_key,
}
    

# Send a GET request to fetch DNS records
    response = requests.get(dns_endpoint, headers=headers)

    if response.status_code == 200:
        return response.json()
    
    else:
        print("Error fetching DNS records. Status Code:", response.status_code)
        return None


# Update DNS Records on Cloudflare
def update_cloudflare_dns_record(api_key, email, zone_id, record_id, updated_data):
    # Set the Cloudflare API endpoint for the specific DNS record
    dns_endpoint = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"

    headers = {
        "X-Auth-Email": email,
        "X-Auth-Key": api_key,
        "Content-Type": "application/json",
    }

    # Send a PUT request to update the DNS record
    response = requests.put(dns_endpoint, data=json.dumps(updated_data), headers=headers)

    if response.status_code == 200:
        print("DNS record updated successfully.")
    else:
        print("Error updating DNS record. Status Code:", response.status_code)
        print("Response:", response.text)
