import matplotlib.pyplot as plt
import pandas as pd

from src.data_loading import load_file
from src.data_processing import order_preprocessing, preprocessing
from src.layout import layout


def main():
    df = preprocessing()
    layout(df)


if __name__ == "__main__":
    main()
