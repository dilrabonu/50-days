import requests

# ✅ Step 1: Define known test cases: input features and true prices
test_data = [
    {'features': [1.5, 3.2, 0.9, 2.1], 'true_price': 2.4},
    {'features': [2.2, 4.1, 1.0, 1.9], 'true_price': 3.1},
    {'features': [1.1, 2.9, 0.8, 2.3], 'true_price': 2.0},
    {'features': [2.5, 4.8, 1.2, 1.5], 'true_price': 3.3},
    {'features': [1.9, 3.5, 1.0, 2.0], 'true_price': 2.8},
]

# ✅ Step 2: Endpoint
url = 'http://127.0.0.1:5000/predict'

# ✅ Step 3: Evaluate each test case
total_error = 0
for i, case in enumerate(test_data):
    input_data = {'features': case['features']}
    true_price = case['true_price']

    response = requests.post(url, json=input_data)
    prediction = response.json()['predicted_close_price']

    error = abs(true_price - prediction)
    percentage_error = round((error / true_price) * 100, 2)

    print(f"Test {i+1}")
    print(f"Input: {case['features']}")
    print(f"True Price: {true_price}")
    print(f"Predicted: {round(prediction, 2)}")
    print(f"Error: {round(error, 4)} | Percentage Error: {percentage_error}%")
    print("------")

    total_error += percentage_error

# ✅ Step 4: Print average percentage error
average_error = total_error / len(test_data)
print(f"\n✅ Average Percentage Error: {round(average_error, 2)}%")
