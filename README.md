## Lab Task 2 - Intermediate

In this lab, you are tasked with extending the functionality of the `main.py` script by adding new functions to interact with DNS records on Cloudflare. Specifically, you will:

- Fetch all DNS entries.
- Edit DNS entries.
- Delete DNS entries.

Make a new branch with your name or fork this repository. Run `pip install -r requirements.txt` to install the required dependencies.

Add the following functions in your `main.py`:

### Fetch all DNS Records

Create a function to fetch all DNS records from a specific zone.

```python
def fetch_dns_records(zone_id):
    # TODO: 
    # Define the URL based on the provided zone_id
    # Send a GET request to the URL with the appropriate headers
    # Handle the response, outputting the result if successful, or the error if it fails
    pass
```

### Edit DNS Records

Create a function to edit a specific DNS record. 

```python
def edit_dns_record(zone_id, record_id, record_data):
    # TODO: 
    # Define the URL based on the provided zone_id and record_id
    # Send a PUT request to the URL with the appropriate headers and the updated record_data as JSON
    # Handle the response, outputting the result if successful, or the error if it fails
    pass
```

### Delete DNS Records

Create a function to delete a specific DNS record.

```python
def delete_dns_record(zone_id, record_id):
    # TODO: 
    # Define the URL based on the provided zone_id and record_id
    # Send a DELETE request to the URL with the appropriate headers
    # Handle the response, outputting the result if successful, or the error if it fails
    pass
```

---

## Guidelines

- For the header section, you can use either your `API_KEY` with the `EMAIL` or `API_TOKEN` to authenticate your requests.
- The `create_dns_record` function has been provided as an example. You can use it as a reference for the other functions.
- You can be as creative as you like however make sure that your script performs the above functionality.
- Use of wrapper libraries like `python-cloudflare` is prohibited. You must use the `requests` library to make HTTP requests.
- Make sure you understand the structure of the Cloudflare API endpoints. Refer to the [Cloudflare API Documentation](https://developers.cloudflare.com/api) for more details.
- Test each function meticulously to ensure they're working as expected. Handle different possible errors gracefully and output helpful error messages.
- Ensure that your code is well-commented to explain the logic and flow of your operations, making it easier for others (and yourself) to understand.

---

## Submission

Once you have completed the tasks, submit your `main.py` script with the completed functions. Ensure that you have tested all scenarios, and everything is working as expected.

Good luck! 🚀
