from collections import deque

def find_order(tasks, prerequisites):
    sortedOrder = []
    if tasks <= 0:
        return sortedOrder
    # initialize the graph
    inDegree = {i:0 for i in range(tasks)}
    graph = {i:[] for i in range(tasks)}
    # build the graph
    for prerequisite in prerequisites:
        parent, child = prerequisite[0], prerequisite[1]
        graph[parent].append(child)
        inDegree[child] += 1
    # find all sources
    sources = deque()
    for key in inDegree:
        if inDegree[key]==0:
            sources.append(key)
    # for each source, add
    # it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            inDegree[child]-=1
            if inDegree[child]==0:
                sources.append(child)
    if len(sortedOrder)!= tasks:
        return []
    return sortedOrder


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
        str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
        str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))



main()

# Time complexity - O(V+E)
# Space complexity - O(V+E)