import requests

# Step 1: Set your local endpoint
url = 'http://127.0.0.1:5000/predict'

# Step 2: Replace these values with correct input features your model expects
data = {
    'features': [1.5, 3.2, 0.9, 2.1]  # example dummy input
}

# Step 3: Send POST request
response = requests.post(url, json=data)

# Step 4: Print the result
print(response.json())
