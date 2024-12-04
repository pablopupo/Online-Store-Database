import pandas as pd

CSVFILEPATH = "generated_data.csv"

def save_data_to_csv(data):
    """
    Saves the data (a pandas DataFrame) to a CSV file.
    """
    data.to_csv(CSVFILEPATH, index=False)

def load_data_from_csv():
    """
    Loads data from the CSV file and returns it as a pandas DataFrame.
    If the file doesn't exist, returns None.
    """
    try:
        data = pd.read_csv(CSVFILEPATH)
        return data
    except FileNotFoundError:
        return None