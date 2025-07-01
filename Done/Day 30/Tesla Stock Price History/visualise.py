import matplotlib.pyplot as plt

# Test inputs (from your evaluate_api.py)
test_cases = [
    {"input": [1.5, 3.2, 0.9, 2.1], "true": 2.4, "pred": 2.31},
    {"input": [2.2, 4.1, 1.0, 1.9], "true": 3.1, "pred": 2.66},
    {"input": [1.1, 2.9, 0.8, 2.3], "true": 2.0, "pred": 2.24},
    {"input": [2.5, 4.8, 1.2, 1.5], "true": 3.3, "pred": 3.2},
    {"input": [1.9, 3.5, 1.0, 2.0], "true": 2.8, "pred": 2.38}
]

# Extract for plotting
true_prices = [case["true"] for case in test_cases]
pred_prices = [case["pred"] for case in test_cases]
labels = [f'Test {i+1}' for i in range(len(test_cases))]

# Plotting
x = range(len(test_cases))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x, true_prices, width=width, label='True Price', color='skyblue')
plt.bar([i + width for i in x], pred_prices, width=width, label='Predicted Price', color='orange')

plt.xlabel('Test Case')
plt.ylabel('Stock Close Price')
plt.title('True vs Predicted Stock Prices (Post-Deployment)')
plt.xticks([i + width / 2 for i in x], labels)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
