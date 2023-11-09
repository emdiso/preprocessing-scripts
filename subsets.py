import pandas as pd

def filter_columns(input_csv, output_csv, columns_to_keep):
    # Read data from the input CSV file into a pandas DataFrame
    df = pd.read_csv(input_csv)
    
    # Filter the DataFrame to keep only the specified columns
    filtered_df = df[columns_to_keep]
    
    # Save the filtered DataFrame to a new CSV file
    filtered_df.to_csv(output_csv, index=False)
    
    print(f"Subset of data saved to '{output_csv}' with columns: {', '.join(columns_to_keep)}")

# Example usage
if __name__ == "__main__":
    input_csv = input("Enter the path to the input CSV file: ")
    output_csv = input("Enter the path for the output CSV file: ")
    
    # Get a comma-separated list of column names to keep
    columns_to_keep = input("Enter the column names to keep (comma-separated): ").split(',')
    columns_to_keep = [col.strip() for col in columns_to_keep]  # Remove leading/trailing spaces
    
    filter_columns(input_csv, output_csv, columns_to_keep)
