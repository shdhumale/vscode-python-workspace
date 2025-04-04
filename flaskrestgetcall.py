import requests

def consume_flask_api(url, method='GET', data=None, headers=None):
    """
    Consumes a Flask API endpoint.

    Args:
        url (str): The URL of the API endpoint.
        method (str): The HTTP method (GET, POST, PUT, DELETE, etc.). Defaults to 'GET'.
        data (dict): The data to send in the request body (for POST, PUT, etc.). Defaults to None.
        headers (dict): Custom headers to include in the request. Defaults to None.

    Returns:
        dict or None: The JSON response from the API, or None if an error occurs.
    """
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, json=data, headers=headers) # Send data as JSON
        elif method == 'PUT':
            response = requests.put(url, json=data, headers=headers)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        # Add other HTTP methods as needed

        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()  # Parse and return the JSON response

    except requests.exceptions.RequestException as e:
        print(f"Error consuming API: {e}")
        if response is not None:
            print(f"Response status code: {response.status_code}")
            try:
                print(f"Response text: {response.text}")
            except:
                print("Response text could not be obtained.")

        return None

# Example usage (assuming your Flask API is running at http://127.0.0.1:5000)

api_url = "http://127.0.0.1:5000/api/data"  # Replace with your API endpoint URL

# Example 1: GET request
result = consume_flask_api(api_url)
if result:
    print("GET Response:", result)

# Example 2: POST request (if your API supports POST)
post_data = {"key": "value", "another_key": 123} # example data
post_url = "http://127.0.0.1:5000/api/post_endpoint" #replace with your post endpoint
post_result = consume_flask_api(post_url, method='POST', data=post_data)

if post_result:
    print("POST Response:", post_result)

# Example 3: Adding Headers
headers = {"Content-Type": "application/json", "Authorization": "Bearer your_token_here"}

result_with_headers = consume_flask_api(api_url, headers=headers)

if result_with_headers:
    print("GET Response with Headers:", result_with_headers)