import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from Src.timestamp import categorize_shift
categorize_shift

def preprocessing(df):
    df['actual_delivery_time'] = pd.to_datetime(df['actual_delivery_time'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    total_days = (df['created_at'].max() - df['created_at'].min()).days + 1

    #df['delivery_time'] = (df['actual_delivery_time'] - df['created_at']).dt.total_seconds() / 60
    #df['hour'] = (df['created_at'].dt.hour) + 1 
    #Find the earlist date
    df 
    min_date = df['created_at'].min()
    df['day'] = (df['created_at'] - min_date).dt.days + 1
    df['shift'] = df['created_at'].apply(categorize_shift)

    df_day100 = df[(df['day']==1) & (df['store_id']=='fe73f687e5bc5280214e0486b273a5f9')]
    st.write(df_day100)
    #df = df.drop(columns=['market_id','created_at','actual_delivery_time','store_primary_category','order_protocol','total_item','subtotal','num_distinct_items','min_item_price','max_item_price'])
    store_partner = df.groupby(['store_id','shift'])['total_onshift_partners'].max().reset_index()
    store_partner.dropna(subset=['total_onshift_partners'],inplace=True)
    order_store = df.groupby(['store_id'])['total_items'].sum().reset_index()
    result = {
        'hourly_partner': store_partner,
        'data': df_day100,
        'order_store': order_store,
        'total_day': total_days,
     }
    return result