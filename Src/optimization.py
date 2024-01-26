from ortools.sat.python import cp_model
import pandas as pd
from Src.data_processing import preprocessing
import streamlit as st 

def optimization(df):
    store_employee = pd.DataFrame(df['hourly_partner'])
    total_order = pd.DataFrame(df['order_store'])
    unique_store = store_employee['store_id'].unique()
    df1 = pd.DataFrame(df['data'])
    unique_shift = pd.DataFrame(['Night-Morning Shift', 'Morning Shift', 'Noon Shift', 'Afternoon Shift', 'Evening Shift', 'Night Shift']) 

    # Model
    model = cp_model.CpModel()
    
    shifts = []

    for store_id in (unique_store):
        store_employees_data = store_employee[store_employee['store_id'] == store_id]
        total_onshift_partners = store_employees_data['total_onshift_partners'].values[0]
        store_shift = store_employees_data['shift'].values[0]
        for employee_number in range(int(total_onshift_partners)):
            employee_id = f'{store_id}${employee_number}'
            shift_entry = {
                'store_id': store_id,
                'shift': store_shift,
                'employee_id': employee_id,
                'busy': 'on-shift'
            }
            shifts.append(shift_entry)

# Convert the list of dictionaries to a DataFrame
    shifts_df = pd.DataFrame(shifts)

# Display the DataFrame
    st.write(shifts_df)
    # Assume df1 is the DataFrame containing the data
    for index, row in df1.iterrows():
        store_id = row['store_id']
        shift = row['shift']
    
    # Filter the shifts DataFrame for the current store_id and shift
        filtered_shifts = shifts_df[(shifts_df['store_id'] == store_id) & (shifts_df['shift'] == shift)]
    # Find available employees
        available_employees = filtered_shifts[filtered_shifts['busy'] == 'on-shift']
    
    # Check if any available employees are found
        if not available_employees.empty:
        # Mark the first available employee as busy
            employee_id = available_employees.iloc[0]['employee_id']
            shifts_df.loc[shifts_df['employee_id'] == employee_id, 'busy'] = 'busy'
        else:
            shifts_df.loc[shifts_df['employee_id'] == employee_id, 'busy'] = 'free'
            print(f"No available employee found for store {store_id} during shift {shift}")

# Display the updated shifts DataFrame
    st.write(shifts_df)
 
 




    