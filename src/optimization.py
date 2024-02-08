import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np 

import pandas as pd
from src.location import visualization_map


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

def optimize_route(filtered_df, location_customer):
    # Extracting restaurant locations from filtered_df
    restaurant_locations = [(row['Latitude'], row['Longitude']) for index, row in filtered_df.iterrows()]

    # Extracting customer location from location_customer
    customer_location = location_customer['Mean']

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(restaurant_locations) + 1, 1, 0)

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create distance callback.
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        if from_node == 0:  # The depot is at index 0
            return 0
        return distance_between_points(restaurant_locations[from_node - 1], restaurant_locations[to_node - 1])

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Set 1 vehicle for the routing problem.
    routing.AddDimension(transit_callback_index, 0, 3000, True, 'Distance')

    # Setting the customer location as the end location
    customer_node = manager.NodeToIndex(0)

    # Setting first node (customer location) as the start location
    routing.SetDepotNodeIndex(0)

    # Solve the problem.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    solution = routing.SolveWithParameters(search_parameters)

    # Output optimal route
    if solution:
        route_indices = get_route_indices(solution, manager)
        optimal_route = [restaurant_locations[i] for i in route_indices]
        return optimal_route
    else:
        return None

def distance_between_points(point1, point2):
    # Calculate the Euclidean distance between two points
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def get_route_indices(solution, manager):
    # Get the indices of the optimal route
    index = routing.Start(0)
    route_indices = []
    while not routing.IsEnd(index):
        route_indices.append(manager.IndexToNode(index))
        index = solution.Value(routing.NextVar(index))
    return route_indices
