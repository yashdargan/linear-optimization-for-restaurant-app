import streamlit as st
import matplotlib.pyplot as plt
from Src.data_loading import load_file
from Src.optimization import optimization
from Src.data_processing import preprocessing
from Src.EDA import EDA
def main():
    st.title("Streamlit Data Loading Example")

    file_path = 'Data/dataset.csv'
    df= load_file(file_path)
    st.write(df.head(50))
    #EDA(df)
    df1=preprocessing(df)
    optimization(df1) 
   
if __name__ == "__main__":
    main()
