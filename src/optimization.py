import pandas as pd
import streamlit as st
from ortools.sat.python import cp_model


def optimization(df):
    # Check if df is a dictionary
    if not isinstance(df, pd.DataFrame):
        st.write("Input is not a DataFrame")
        return

    # Initialize DataFrame for employee shifts
    shifts = pd.DataFrame(columns=["store_id", "shift", "employee_id", "busy"])

    # Create a CP model
    model = cp_model.CpModel()

    # Assume df1 is the DataFrame containing the data
    for index, row in df.iterrows():
        store_id = row["store_id"]
        shift = row["shift"]

        # Filter the shifts DataFrame for the current store_id and shift
        filtered_shifts = shifts[
            (shifts["store_id"] == store_id) & (shifts["shift"] == shift)
        ]

        # Find available employees
        available_employees = filtered_shifts[
            filtered_shifts["busy"] == "on-shift"
        ]

        # Check if any available employees are found
        if not available_employees.empty:
            # Mark the first available employee as busy
            employee_id = available_employees.iloc[0]["employee_id"]
            shifts.loc[shifts["employee_id"] == employee_id, "busy"] = "busy"
        else:
            # Handle case when no available employees are found
            st.write(
                f"No available employee found for store {store_id} during shift {shift}"
            )

    # Objective: Minimize the number of unfilled shifts
    unfilled_shifts = model.NewIntVar(0, 1000, "unfilled_shifts")
    model.Add(unfilled_shifts == shifts[shifts["busy"] == "free"].shape[0])

    # Create a solver and solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        st.write("Optimal Solution Found!")
        st.write(f"Number of Unfilled Shifts: {solver.Value(unfilled_shifts)}")
    else:
        st.write("No Optimal Solution Found.")

    # Display the final shifts DataFrame
    st.write(shifts)
