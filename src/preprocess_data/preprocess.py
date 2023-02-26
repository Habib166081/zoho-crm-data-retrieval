import os
from datetime import datetime
import pandas as pd



def json_to_dataframe(json_data):
    df = pd.DataFrame(json_data)
    return df


def save_dataframe_to_csv(df):
    # Create a directory for data files if it doesn't exist
    if not os.path.exists("files_data"):
        os.makedirs("files_data")

    # Get the current date and time to create a unique file name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"files_data/data_{timestamp}.csv"

    # Save the DataFrame to a CSV file
    df.to_csv(file_name, index=False)


