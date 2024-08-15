import kaggle
import os
import pandas as pd

# Set Kaggle API credentials directory
os.environ['KAGGLE_CONFIG_DIR'] = 'C:\Users/Harsh Parmar/.kaggle'

# Specify the dataset identifier
dataset = 'piterfm/paris-2024-olympic-summer-games'

# Set the download path
download_path = 'D:/Data-Analysis/Paris Olympics/Data_source'

# Remove existing files in the folder to prevent duplicates or outdated files
for file in os.listdir(download_path):
    file_path = os.path.join(download_path, file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)  # Delete the file
            print(f"Deleted {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

# Download the dataset using the Kaggle API and unzip the files
kaggle.api.dataset_download_files(dataset, path=download_path, unzip=True)

# List of CSV files to be imported
csv_files = [
    'athletes.csv',
    'events.csv',
    'medallists.csv',
    'medals.csv',
    'medals_total.csv',
    'schedules.csv',
    'schedules_preliminary.csv',
    'teams.csv',
    'torch_route.csv',
    'venues.csv'
]

# Initialize a dictionary to hold DataFrames
dataframes = {}

# Iterate through each CSV file and load it into a DataFrame
for file in csv_files:
    # Construct the full path to the CSV file
    file_path = os.path.join(download_path, file)
    
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Add the DataFrame to the dictionary using the file name as the key
    table_name = file.split('.')[0]  # Remove the .csv extension
    dataframes[table_name] = df





# Import necessary libraries
import pandas as pd
import os

# Define the path to the downloaded CSV files
download_path = 'D:\Data-Analysis\Paris Olympics\Data_source'

# Load the data into DataFrames
athletes = pd.read_csv(os.path.join(download_path, 'athletes.csv'))
events = pd.read_csv(os.path.join(download_path, 'events.csv'))
medallists = pd.read_csv(os.path.join(download_path, 'medallists.csv'))
medals = pd.read_csv(os.path.join(download_path, 'medals.csv'))
medals_total = pd.read_csv(os.path.join(download_path, 'medals_total.csv'))
schedules = pd.read_csv(os.path.join(download_path, 'schedules.csv'))
schedules_preliminary = pd.read_csv(os.path.join(download_path, 'schedules_preliminary.csv'))
teams = pd.read_csv(os.path.join(download_path, 'teams.csv'))
torch_route = pd.read_csv(os.path.join(download_path, 'torch_route.csv'))
venues = pd.read_csv(os.path.join(download_path, 'venues.csv'))