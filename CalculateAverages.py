import json
import os

# Construct the file path
file_path = os.path.join(os.path.dirname(__file__), 'templates', 'numericalValues.json')

with open(file_path) as f:
    data = json.load(f)

# Extract the numerical values
numerical_values = data['numbers']

# Calculate the average of the numerical values
average = sum(numerical_values) / len(numerical_values)
mean = round(average, 2)
min_value = min(numerical_values)
max_value = max(numerical_values)

print(f"Average: {mean}")
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")