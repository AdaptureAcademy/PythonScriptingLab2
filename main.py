import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv('API_TOKEN')

# Define headers for the API requests, including the Authorization token and the content type.
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}


# Function to fetch user details from Cloudflare's API
def fetch_user_details():
    # Define the URL for the user details endpoint
    url = 'https://api.cloudflare.com/client/v4/user'
    # Send a GET request to the specified URL, with the defined headers
    response = requests.get(url, headers=headers)
    # Check if the response status code is 200 (OK)
    if response.ok:
        # Parse the JSON response and print it
        data = response.json()
        print(data)
    else:
        # If the response status code is not 200, print the error status code and response text
        print(f'Error: {response.status_code}')
        print(response.text)


def create_dns_record(zone_id, dns_record_data):
    # Define the URL for the DNS record creation endpoint, including the specified zone ID
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
    # Send a POST request to the specified URL, with the defined headers and JSON payload
    response = requests.post(url, headers=headers, json=dns_record_data)
    # Check if the response status code is 200 (OK)
    if response.ok:
        # Parse the JSON response and print it
        data = response.json()
        print(data)
    else:
        # If the response status code is not 200, print the error status code and response text
        print(f'Error: {response.status_code}')
        print(response.text)


def fetch_dns_records(zone_id):
    # TODO: 
    # Define the URL based on the provided zone_id
    # Send a GET request to the URL with the appropriate headers
    # Handle the response, outputting the result if successful, or the error if it fails
    pass


def edit_dns_record(zone_id, record_id, record_data):
    # TODO:
    # Define the URL based on the provided zone_id and record_id
    # Send a PUT request to the URL with the appropriate headers and the updated record_data as JSON
    # Handle the response, outputting the result if successful, or the error if it fails
    pass


def delete_dns_record(zone_id, record_id):
    # TODO:
    # Define the URL based on the provided zone_id and record_id
    # Send a DELETE request to the URL with the appropriate headers
    # Handle the response, outputting the result if successful, or the error if it fails
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # TODO: Call all the above functions here
    pass
