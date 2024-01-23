import streamlit as st
from Src.data_loading import load_file
def main():
    st.title("Streamlit Data Loading Example")

    file_path = 'Data/dataset.csv'
    df= load_file(file_path)
    st.write(df.head(50)) 

if __name__ == "__main__":
    main()
