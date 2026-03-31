import pandas as pd

# Load the CSV file
df = pd.read_csv("1experience.csv")

# Display dataset
print("Dataset:\n", df)

# Central Tendencies
mean_val = df['YearsExperience'].mean()
median_val = df['YearsExperience'].median()
mode_val = df['YearsExperience'].mode()[0]

# Dispersion Measures
min_val = df['YearsExperience'].min()
max_val = df['YearsExperience'].max()
range_val = max_val - min_val
variance_val = df['YearsExperience'].var()
std_dev_val = df['YearsExperience'].std()

# Display results
print("\n--- Central Tendencies ---")
print("Mean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)

print("\n--- Dispersion Measures ---")
print("Minimum:", min_val)
print("Maximum:", max_val)
print("Range:", range_val)
print("Variance:", variance_val)
print("Standard Deviation:", std_dev_val)

# Full statistical summary
print("\n--- Summary Statistics ---")
print(df.describe())
