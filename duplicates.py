import pandas as pd

def find_duplicates(csv_file):
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(csv_file, encoding='iso-8859-1')
    
    # Find duplicates based on all columns
    duplicates = data[data.duplicated()]
    
    # If you want to remove duplicates and keep only the first occurrence
    # data_without_duplicates = data.drop_duplicates()
    
    return duplicates

# Example usage
if __name__ == "__main__":
    csv_file = input("Enter the path to the CSV file: ")
    duplicates = find_duplicates(csv_file)
    
    if duplicates.empty:
        print("No duplicates found.")
    else:
        print("Duplicates found:")
        print(duplicates)
