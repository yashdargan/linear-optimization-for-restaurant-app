
# Restaurant Finder App

## Overview

This Streamlit web application helps users find nearby restaurants in Delhi NCR and optimize their selection based on their location.

## Installation

1. Clone the repository:

    ```
    git clone <repository_url>
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

To run the Streamlit app, use the following command:


## Functions



### `visualization_map(filtered_df, location, cat)`

- Description: Visualizes nearby restaurants on a Folium map.
- Parameters:
  - `filtered_df`: DataFrame containing restaurant data.
  - `location`: Location to center the map (e.g., "Mean", "Random", "Outer").
  - `cat`: Category of restaurants to display ("All", "North Indian", "South Indian", "Beverages", "Chinese").
- Returns: Filtered DataFrame with latitude and longitude columns.

# Delivery Route Optimization

This Python script provides functionalities for optimizing delivery routes based on various factors such as protocol, distance, and price. It leverages mathematical calculations and linear optimization techniques to achieve efficient route planning.

## Features

### 1. Libraries Used
- `math`: Provides mathematical functions.
- `numpy`: Offers support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions.
- `pandas`: Enables data manipulation and analysis.
- `streamlit`: Facilitates the creation of interactive web applications.
- `ortools.linear_solver.pywraplp`: Part of Google's Operations Research Tools, used for solving linear optimization problems.

### 2. Functions
1. **`haversine(lon1, lat1, lon2, lat2)`**: Calculates the great circle distance between two points on Earth specified in decimal degrees using the Haversine formula.
2. **`optimization(df, order_df)`**: Performs optimization of delivery routes based on certain criteria. It defines and solves a linear programming problem where the objective is to minimize a combination of protocol and price for selected orders while ensuring that each delivery partner takes only one order. The function returns a DataFrame of selected orders based on the optimization results.

### 3. Functionality
- The optimization function defines optimization parameters such as weights for protocol, distance, and price.
- It creates binary decision variables for each order, indicating whether an order is selected or not.
- The objective function aims to minimize the combination of protocol and price for selected orders.
- Constraints ensure that each delivery partner takes only one order.
- The script utilizes Google's OR-Tools for solving the linear optimization problem.

### 4. User Interface (UI)
- The script likely has an interface built using Streamlit to interact with users, allowing them to input data and view optimization results interactively.

## Usage
- The code seems to be part of a larger application designed to optimize delivery routes for a logistics or delivery service company.

## Additional Notes
- For detailed explanations of each function and how to interact with the application, refer to the code comments and documentation.


### `main()`

- Description: Main function to run the Streamlit app.
- Usage: Run the Streamlit app using `streamlit run main.py`.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

