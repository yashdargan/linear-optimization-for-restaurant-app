import math

import numpy as np
import pandas as pd
import streamlit as st
from ortools.linear_solver import pywraplp


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def optimization(df, order_df):
    st.write("total_orders")
    st.write(order_df)
    # Assign weights
    weight_protocol = 0.4
    weight_distance = 0.3
    weight_price = 0.3

    solver = pywraplp.Solver.CreateSolver("SCIP")

    x = [solver.IntVar(0, 1, "x[{}]".format(i)) for i in range(len(order_df))]

    total_delivery_partners = df["total_onshift_partners"].sum()

    # Define objective function
    objective = solver.Objective()
    objective.SetMinimization()

    # Define variables for protocol, distance, and price
    protocol = order_df["order_protocol"].tolist()
    price = order_df["price"].tolist()

    # Add terms to the objective function
    for i in range(len(order_df)):
        objective.SetCoefficient(
            x[i],
            -1 * (weight_protocol * protocol[i] + weight_price * price[i]),
        )

    # Add constraints (only one order can be selected)
    constraint = solver.Constraint(1, total_delivery_partners)
    for i in range(len(order_df)):
        constraint.SetCoefficient(x[i], 1)

    # Solve the problem
    status = solver.Solve()
    selected_orders = []

    if status == pywraplp.Solver.OPTIMAL:
        print("Optimal solution found:")
        for i in range(len(order_df)):
            if x[i].solution_value() == 1:
                selected_order = order_df.iloc[i]
                selected_orders.append(selected_order)
                print("Optimal order {}:".format(i + 1), selected_order)
    selected_orders = pd.DataFrame(selected_orders)
    st.write("Selected orders:", selected_orders)

    return selected_orders
