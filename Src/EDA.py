import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from Src.timestamp import categorize_shift 

def EDA(df):
    df['actual_delivery_time'] = pd.to_datetime(df['actual_delivery_time'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    total_days = (df['created_at'].max() - df['created_at'].min()).days + 1

    df['delivery_time'] = (df['actual_delivery_time'] - df['created_at']).dt.total_seconds() / 60
    df['hour'] = (df['created_at'].dt.hour) + 1 
    df['day'] = (df['created_at'].dt.dayofweek) + 1
    df['shift'] = df['created_at'].apply(categorize_shift)

    shift_partner_count = df.groupby('shift')['total_onshift_partners'].max().reset_index()

# Plotting the bar chart
    fig, ax = plt.subplots()
    ax.plot(shift_partner_count['shift'], shift_partner_count['total_onshift_partners'], marker='o', linestyle='-')
    ax.set_ylabel('Total On-Shift Partners')
    ax.set_xlabel('Shift')
    ax.set_title('Total On-Shift Partners for Each Shift')
    st.pyplot(fig)
    

