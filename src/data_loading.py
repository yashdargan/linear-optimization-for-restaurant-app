import pandas as pd


def load_file(file):
    try:
        df = pd.read_csv(file)
        print("Data loaded Sucessfully")
        return df
    except FileNotFoundError:
        print("File not Found. Please Check the file path")
        return None
    except pd.errors.EmptyDataError:
        print("file is empty")
        return None
    except Exception as e:
        print("An unexception error occurred: {e}")
        return None
