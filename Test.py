rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"

rainfall_list = rainfall_mi.split(', ')

rainfall_floats = [float(value) for value in rainfall_list]

# Count the number of values greater than 3.0
num_rainy_months = sum(value > 3.0 for value in rainfall_floats)

print(num_rainy_months)
