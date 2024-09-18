import load_graph

# BFS implementation
def bfs_path(graph, start, goal):
    """
    Perform Breadth-First Search (BFS) to find the shortest path
    from the start node to the goal node in an unweighted graph.

    :param graph: A dictionary representing the adjacency list of the graph.
    :param start: The starting node for the BFS.
    :param goal: The goal node we want to reach.
    :return: A list representing the path from start to goal if exists, otherwise None.
    """
    visited = set()  # Set to keep track of visited nodes
    queue = [(start, [start])]  # Queue for BFS: (current_node, path_to_current_node)
    
    while queue:
        # Get the first node and path from the queue
        (node, path) = queue.pop(0)
        
        # Check if we have visited this node
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            
            # Explore neighbors
            for neighbor in graph.get(node, []):
                # If the neighbor is the goal, return the path
                if neighbor == goal:
                    return path + [neighbor]
                else:
                    # Otherwise, add the neighbor to the queue
                    queue.append((neighbor, path + [neighbor]))
    
    # Return None if no path is found
    return None


def estimate_path_with_bfs (start_node, goal_node, node_id):
    edge_list_path = 'data/TestCase_{}_EdgeList.txt'.format(node_id)
    node_id_path = 'data/TestCase_{}_NodeID.csv'.format(node_id)     
    graph, _ = load_graph.load_unweighted_graph(edge_list_path, node_id_path)

    # Find path using BFS
    path = bfs_path(graph, start_node, goal_node)
    path_string = ""
    # Output the path
    if path:
        for p in path: 
            if p in path[:-1]:
                path_string += p + " => "
            else: 
                path_string += p
        print("Robot Path found Using BFS Algorithm: in test case {}".format(node_id), path_string)
        return path , path_string
    else:
        print("No Robot path found between {} and {} for test case {} using BFS algorithm".format(start_node, goal_node, node_id))
        return None
    

estimate_path_with_bfs("N_0", "N_24", "01")

estimate_path_with_bfs("N_0", "N_99", "02")

estimate_path_with_bfs("N_0", "N_999", "03")