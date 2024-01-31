import matplotlib.pyplot as plt
import pandas as pd

from src.data_loading import load_file
from src.data_processing import preprocessing
from src.layout import layout
from src.optimization import optimization


def main():
    file_path = "Data/dataset.csv"
    df = load_file(file_path)
    layout(df)

    # df1 = preprocessing(df)
    # df1 = pd.DataFrame(df1)
    # optimization(df1)


if __name__ == "__main__":
    main()
