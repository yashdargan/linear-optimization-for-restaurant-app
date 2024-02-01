import matplotlib.pyplot as plt
import pandas as pd

from src.data_loading import load_file
from src.layout import layout


def main():
    file_path = "Data/dataset.csv"
    df = load_file(file_path)
    layout(df)


if __name__ == "__main__":
    main()
