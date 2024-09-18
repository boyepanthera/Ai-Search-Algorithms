import load_graph
# DFS path iterative implementation
def dfs_path(graph, start, goal):
    """
    Perform Depth-First Search (DFS) iteratively using a stack
    to find a path from the start node to the goal node in an unweighted graph.

    :param graph: A dictionary representing the adjacency list of the graph.
    :param start: The starting node for the DFS.
    :param goal: The goal node we want to reach.
    :return: A list representing the path from start to goal if exists, otherwise None.
    """
    visited = set()  # Set to keep track of visited nodes
    stack = [(start, [start])]  # Stack for DFS: (current_node, path_to_current_node)
    
    while stack:
        # Get the last node and path from the stack
        (node, path) = stack.pop()
        
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            
            # If we reached the goal node
            if node == goal:
                return path
            
            # Explore neighbors
            for neighbor in graph.get(node, []):
                stack.append((neighbor, path + [neighbor]))
    
    return None

def estimate_path_with_dfs (start_node, goal_node, node_id) :
    edge_list_path = 'data/TestCase_{}_EdgeList.txt'.format(node_id)  
    node_id_path = 'data/TestCase_{}_NodeID.csv'.format(node_id)
    graph, _ = load_graph.load_unweighted_graph(edge_list_path, node_id_path)

    # Find path using DFS (iterative)
    path = dfs_path(graph, start_node, goal_node)
    path_string = ""

    # Output the path
    if path:
        for p in path: 
            if p in path[:-1]:
                path_string += p + " => "
            else: 
                path_string += p
        print("Robot Path found Using DFS Algorithm: in test case {}".format(node_id), path_string)
        return path , path_string
    else:
        print("No Robot path found between {} and {} for test case {} using DFS algorithm".format(start_node, goal_node, node_id))
        return None


# TEST CASES

estimate_path_with_dfs("N_0", "N_24", "01")

estimate_path_with_dfs("N_0", "N_99", "02")

estimate_path_with_dfs("N_0", "N_999", "03")