import math
import heapq
import load_graph


# A* search algorithm implementation using heuristic functions
def a_star_search(graph, node_coordinates, start_node, goal_node, heuristic_function):
    """
    Perform A* search to find the shortest path from the start node to the goal node in a weighted graph.

    :param graph: A dictionary representing the adjacency list of the graph.
    :param node_coordinates: A dictionary of node coordinates for heuristic calculation.
    :param start_node: The starting node for the A* search.
    :param goal_node: The goal node we want to reach.
    :param heuristic_function: The heuristic function to estimate cost from a node to the goal.
    :return: A list representing the path from start to goal if exists, otherwise None.
    """
    # Priority queue to store nodes to explore
    open_set = []
    heapq.heappush(open_set, (0, start_node))
    
    # Dictionaries to store the cost and goal path
    goal_costs = {start_node: 0}
    came_from = {start_node: None}
    
    while open_set:
        # Get the node with the lowest cost estimate
        _, current = heapq.heappop(open_set)
        
        # If we reached the goal node
        if current == goal_node:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Return reversed path
        
        # Explore neighbors
        for neighbor, weight in graph.get(current, []):
            tentative_goal_cost = goal_costs[current] + weight
            
            if neighbor not in goal_costs or tentative_goal_cost < goal_costs[neighbor]:
                goal_costs[neighbor] = tentative_goal_cost
                # add heuristic cost(cost from current node to goal node) to the tentative cost (from start node to current node)
                full_cost = tentative_goal_cost + heuristic_function(node_coordinates, neighbor, goal_node)
                heapq.heappush(open_set, (full_cost, neighbor))
                came_from[neighbor] = current
    
    return None  # No path found

# Heuristic functions

# 1. Euclidean distance heuristic
def euclidean_heuristic(node_coordinates, node, goal):
    """
    Calculate the Euclidean distance between the current node and the goal.

    :param1 node_coordinates: A dictionary of node coordinates.
    :param2 node: The current node.
    :param3 goal: The goal node.
    :return: The Euclidean distance between the current node and the goal node.
    """
    x1, y1 = node_coordinates[node]
    x2, y2 = node_coordinates[goal]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 2. Manhattan distance heuristic
def manhattan_heuristic(node_coordinates, node, goal):
    """
    Calculate the Manhattan distance between the current node and the goal.

    :param1 node_coordinates: A dictionary of node coordinates.
    :param2 node: The current node.
    :param3 goal: The goal node.
    :return: The Manhattan distance between the current node and the goal.
    """
    x1, y1 = node_coordinates[node]
    x2, y2 = node_coordinates[goal]
    return abs(x2 - x1) + abs(y2 - y1)

# 3. Chebyshev distance heuristic
def chebyshev_heuristic(node_coordinates, node, goal):
    """
    Calculate the Chebyshev distance between the current node and the goal.

    :param1 node_coordinates: A dictionary of node coordinates.
    :param2 node: The current node.
    :param3 goal: The goal node.
    :return: The Chebyshev distance between the current node and the goal.
    """
    x1, y1 = node_coordinates[node]
    x2, y2 = node_coordinates[goal]
    return max(abs(x2 - x1), abs(y2 - y1))



def estimate_path_with_a_star (start_node ,goal_node, heuristic_function, test_case_id):
    edge_list_path = 'data/TestCase_{}_EdgeList.txt'.format(test_case_id)  
    node_id_path = 'data/TestCase_{}_NodeID.csv'.format(test_case_id) 
    graph, node_coordinates = load_graph.load_weighted_graph(edge_list_path, node_id_path)

    # Find path using A* with heuristic funcction passed to the estimate function
    path = a_star_search(graph, node_coordinates, start_node, goal_node,  heuristic_function)
    path_string ="" 

    # Returns the path as both a bordered arrow path and a list of nodes in a dictionary,
    if path:
        for p in path: 
            if p in path[:-1]:
                path_string += p + " => "
            else: 
                path_string += p

        # Print Path arrow string
        print(f"Robot path with A* and {heuristic_function.__name__.replace('_',' ')} from", start_node, "to", goal_node, ":",  path_string)
        return  path,  path_string
    else:
        print(f"No valid path found for Robot using A* search and {heuristic_function.__name__.replace('_', ' ')} between", start_node, "and", goal_node)
        return None
    


# TEST CASES

#===================================================================
#Test Case 01:
# for test case 01 with chebyshev heuristics
estimate_path_with_a_star("N_0", "N_24", chebyshev_heuristic, '01')

# for test case 01 with euclidean heuristics
estimate_path_with_a_star("N_0", "N_24", euclidean_heuristic, '01')

# for test case 01 with manhattan heuristics
estimate_path_with_a_star("N_0", "N_24", manhattan_heuristic, '01')

#===================================================================
# Test Case 02
# for test case 02 with chebyshev heuristics
estimate_path_with_a_star("N_0", "N_99", chebyshev_heuristic, '02')

# for test case 02 with euclidean heuristics
estimate_path_with_a_star("N_0", "N_99", euclidean_heuristic, '02')

# for test case 02 with manhattan heuristics
estimate_path_with_a_star("N_0", "N_99", manhattan_heuristic, '02')

#===================================================================
# Test Case 03
# for test case 03 with chebyshev heuristics
path_data_03_chebyshev = estimate_path_with_a_star("N_0", "N_999", chebyshev_heuristic, '03')

# for test case 03 with euclidean heuristics
path_data_03_chebyshev = estimate_path_with_a_star("N_0", "N_999", euclidean_heuristic, '03')

# for test case 03 with manhattan heuristics
estimate_path_with_a_star("N_0", "N_999", manhattan_heuristic, '03')