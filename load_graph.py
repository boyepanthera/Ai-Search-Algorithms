import csv

def load_unweighted_graph(edge_list_path, node_id_path):
    """
    Load the graph data from an edge list file and a node ID file.
    The edge list file contains edges in the format (n1, n2, w).
    The node ID file contains nodes with their coordinates (node, x, y).

    :param edge_list_path: Path to the edge list text file.
    :param node_id_path: Path to the node ID CSV file.
    :return: A tuple containing the graph (adjacency list) and node coordinates.
    """
    graph = {}
    
    # Load edge list to construct the graph
    with open(edge_list_path, 'r') as edge_file:
        for line in edge_file:
            # Split each line into nodes and weight (node_i, node_j, _)
            node_i, node_j, _ = line.strip().split(',')
            
            # Add edges to the graph (undirected)
            if node_i not in graph:
                graph[node_i] = []
            if node_j not in graph:
                graph[node_j] = []
            graph[node_i].append(node_j)
            graph[node_j].append(node_i)  # Assuming an undirected graph
            
    # Load node coordinates (optional if needed)
    node_coordinates = {}
    with open(node_id_path, 'r') as node_id_file:
        reader = csv.reader(node_id_file)
        for row in reader:
            # Read node and its coordinates
            node, x, y = row
            node_coordinates[node] = (float(x), float(y))
    
    return graph, node_coordinates


# Function to load graph from edge list and node ID files
def load_weighted_graph(edge_list_path, node_id_path):
    """
    Load the graph data from an edge list file and a node ID file.
    The edge list file contains edges in the format (n1, n2, w).
    The node ID file contains nodes with their coordinates (node, x, y).

    :param edge_list_path: Path to the edge list text file.
    :param node_id_path: Path to the node ID CSV file.
    :return: A tuple containing the graph (adjacency list) and node coordinates.
    """
    graph = {}
    
    # Load edge list to construct the graph
    with open(edge_list_path, 'r') as edge_file:
        for line in edge_file:
            # Split each line into nodes and weight (node_i, node_j, weight)
            node_i, node_j, weight = line.strip().split(',')
            weight = float(weight)  # Convert weight to float
            
            # Add edges to the graph (undirected with weight)
            if node_i not in graph:
                graph[node_i] = []
            if node_j not in graph:
                graph[node_j] = []
            graph[node_i].append((node_j, weight))
            graph[node_j].append((node_i, weight))  # Assuming an undirected graph
            
    # Load node coordinates (optional if needed for heuristics)
    node_coordinates = {}
    with open(node_id_path, 'r') as node_id_file:
        reader = csv.reader(node_id_file)
        for row in reader:
            # Read node and its coordinates
            node, x, y = row
            node_coordinates[node] = (float(x), float(y))
    
    return graph, node_coordinates
