from collections import deque
def topological_sort(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder
    # initialize the graph
    inDegree = {i:0 for i in range(vertices)}
    graph = {i:[] for i in range(vertices)}
    # build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        inDegree[child] += 1
    # find all sources
    sources = deque()
    for key in inDegree:
        if inDegree[key]==0:
            sources.append(key)
    # for each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            inDegree[child] -= 1
            if inDegree[child]==0:
                sources.append(child)
    # topological sort is not posible if the graph is cyclic
    if len(sortedOrder)!=vertices:
        return []
    return sortedOrder

def main():
    print("Topological sort: " +str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +str(topological_sort(5,[[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))

main()

# time complexity: O(V+E)
# space complexity: O(V+E)
gii[vefsota]

