import sys
from collections import defaultdict

PATHS = []

def traverse(node, node_map, path):
    global PATHS
    new_path = path.copy()
    new_path.append(node)
    if node == 'end':
        PATHS.append(new_path)
        return

    for next_node in node_map[node]:
        if next_node.isupper() or (next_node not in path):
            traverse(next_node, node_map, new_path)

def main():
    global PATHS
    with open(sys.argv[1]) as f:
        edges = [line.strip().split('-') for line in f.readlines()]

    nodes = set()
    for edge in edges:
        nodes.update(edge)

    node_map = defaultdict(list)
    for node0, node1 in edges:
        if node1 != 'start' and node0 != 'end':
            node_map[node0].append(node1)
        if node0 != 'start' and node1 != 'end':
            node_map[node1].append(node0)

    traverse('start', node_map, [])

    print(len(PATHS))


main()
