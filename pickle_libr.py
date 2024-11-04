"""
import pickle

# Sample data to pickle
data = {
    'name': 'Alice',
    'age': 30,
    'hobbies': ['reading', 'traveling', 'swimming']
}

# Pickling the data
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Unpickling the data
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
"""
#pickle lib saving in a file
#with is a statement
#python dont have built in support in constants
#constant variables are written in uppercase indicate should not change PI=3.14

"""
import requests

# Replace with the actual endpoint
url = ('http://www.google.com/intl/en/privacy.')

# Replace with your actual API key or token
headers = {
    'Authorization': 'Bearer YOUR_API_KEY'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises an error for HTTP error codes

    # Parse the JSON response
    data = response.json()  # Assuming the response is in JSON format
    print(data)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # Example: 404 Not Found
except Exception as err:
    print(f"An error occurred: {err}")  # Catch all other exceptions
"""

import os

def rename_files_in_directory(directory):
    for count, filename in enumerate(os.listdir(directory)):
        src = f"{directory}/{filename}"
        dst = f"{directory}/automatefiles_{count}.txt"
        os.rename(src, dst)

# Usage
rename_files_in_directory('/Users/bo20531398/Documents/rajendra_practice')

