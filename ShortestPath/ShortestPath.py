# Task: Find the length of the shortest path that visits every node in an undirected, connected graph.
# The graph is represented by an array where each element contains a list of nodes connected to a specific node.
# It is allowed to start and stop at any node, revisit nodes multiple times, and reuse edges.

# Example 1:
# Input: graph = [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: A possible path is [1,0,2,0,3]

# Example 2:
# Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: A possible path is [0,1,4,2,3]

# Constraints:
# - n is the number of nodes, and 1 <= n <= 12.
# - graph[i] is a list of nodes connected to node i.
# - graph[i] does not contain i.
# - If graph[a] contains b, then graph[b] contains a.
# - The input graph is always connected.


def shortestPathLength(graph):
    # Get the number of nodes in the proposed graph
    n = len(graph)
    
    # Calculate the final state where all nodes are visited
    final_state = (1 << n) - 1
    
    # Initialize the queue as a list, each element is a tuple (node, state, length)
    queue = []
    
    # Use a set to keep track of visited nodes and their states
    visited = set()

    # Initialize the queue with starting states for each node
    for i in range(n):
        queue.append((i, 1 << i, 0))

    # BFS 
    while queue:
        # Pop the front of the queue to get the current node, state, and length
        node, state, length = queue.pop(0)

        # Check if the current state is the final state (all nodes visited)
        if state == final_state:
            return length

        # Check if the current node and state have been visited before
        if (node, state) in visited:
            continue
        # Mark the current node and state as visited
        visited.add((node, state))

        # Explore neighbors of the current node
        for neighbor in graph[node]:
            # Update the state by setting the bit corresponding to the neighbor to 1
            new_state = state | (1 << neighbor)
            # Add the neighbor, new state, and updated length to the queue for further exploration
            queue.append((neighbor, new_state, length + 1))

    # If the loop completes without finding a path that visits all nodes, return -1
    return -1

# Example 1
graph1 = [[1,2,3],[0],[0],[0]]
print(shortestPathLength(graph1))  # Output: 4

# Example 2
graph2 = [[1],[0,2,4],[1,3,4],[2],[1,2]]
print(shortestPathLength(graph2))  # Output: 4
