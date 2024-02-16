
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

### `fetch_nearby_restaurants(latitude, longitude)`

- Description: Fetches nearby restaurants using OpenStreetMap API.
- Parameters:
  - `latitude`: Latitude coordinate of the location.
  - `longitude`: Longitude coordinate of the location.
- Returns: JSON data containing nearby restaurants.

### `visualization_map(filtered_df, location, cat)`

- Description: Visualizes nearby restaurants on a Folium map.
- Parameters:
  - `filtered_df`: DataFrame containing restaurant data.
  - `location`: Location to center the map (e.g., "Mean", "Random", "Outer").
  - `cat`: Category of restaurants to display ("All", "North Indian", "South Indian", "Beverages", "Chinese").
- Returns: Filtered DataFrame with latitude and longitude columns.

### `optimize_restaurant(filtered_df, latitude, longitude)`

- Description: Optimizes restaurant selection based on the customer's location.
- Parameters:
  - `filtered_df`: DataFrame containing restaurant data.
  - `latitude`: Latitude coordinate of the customer's location.
  - `longitude`: Longitude coordinate of the customer's location.
- Returns: DataFrame with the optimized restaurant.

### `main()`

- Description: Main function to run the Streamlit app.
- Usage: Run the Streamlit app using `streamlit run main.py`.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

