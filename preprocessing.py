import pandas as pd

# Read data from the CSV file into a pandas DataFrame
df = pd.read_csv('./spotify-2023.csv', encoding='iso-8859-1')

# Find missing values in the DataFrame
missing_values = df.isnull().sum()

# Determine if missing values should be filled with the average or most common value
fill_with_average = False  # Set to False if you want to fill with the most common value

# Fill missing values with the average or most common value
if fill_with_average:
    df.fillna(df.mean(), inplace=True)  # Fill missing values with column-wise average
else:
    df.fillna(df.mode().iloc[0], inplace=True)  # Fill missing values with most common value

# Save the updated DataFrame to a new CSV file
df.to_csv('updated-spotify-2023.csv', index=False)

# Print the updated DataFrame
print("Updated DataFrame with missing values filled:")
print(df)

# Print the columns with missing values and their corresponding counts
print("\nMissing values count per column:")
print(missing_values)
