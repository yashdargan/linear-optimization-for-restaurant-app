import pandas as pd
import streamlit as st
from ortools.sat.python import cp_model


def optimization(data_dict):
    # Check if data_dict is a dictionary
    if not isinstance(data_dict, dict):
        st.write("Input is not a dictionary")
        return

    # Access individual components from data_dict
    hourly_partner_df = data_dict["hourly_partner"]
    data_df = data_dict["data"]
    order_store_df = data_dict["order_store"]
    total_days = data_dict["total_day"]

    # Initialize DataFrame for employee shifts
    shifts = pd.DataFrame(columns=["store_id", "shift", "employee_id", "busy"])

    # Create a CP model
    model = cp_model.CpModel()

    # Optimization process
    for index, row in data_df.iterrows():
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
