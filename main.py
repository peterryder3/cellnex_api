import requests
import json
import pprint
import dotenv
import os

url = "https://api-gateway.smartbrain.cellnextelecom.com/t/smartbrain.cellnextelecom/smartbrain.cellnextelecom/ngsiext/v3/entities"


bearer_token =  os.getenv("BEARER") 


# Set the headers with the Authorization Bearer token
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json",  # Adjust content type if needed
}
# Make a GET request
response = requests.get(url,  headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    newDict =[]
    for i in data:
        if i['type'] == 'ParkingSpot':
            newDict.append(i)
        # if data[i]['type'] == 'ParkingSpot':
        #     data = data[0]['status']

    # Now 'data' contains the JSON response as a Python dictionary
    print(json.dumps(data, indent=2))  # Pretty print the JSON data
else:
    print(f"Error: {response.status_code}")
    print(response.text)  # Print the error message, if any


