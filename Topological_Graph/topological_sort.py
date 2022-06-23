from collections import deque


def topological_sort(vertices, edges):
    sortedorder = []
    if vertices<=0:
        return sortedorder

    # initialize graph
    inDegree = {i:0 for i in range(vertices)}
    graph = {i:[] for i in range(vertices)}

    

    # build graph
    for edge in edges:
        parent , child = edge[0], edge[1]
        graph[parent].append(child)
        inDegree[child]+=1 # increment child's indegree


    # print("inDegress",inDegree)
    # print("Graph",graph)
    # c. Find all sources i.e., all vertices with 0 in-degrees

    sources = deque()
    for key in inDegree:
        if inDegree[key]==0:
            sources.append(key)
    # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue

    while sources:
        vertex = sources.popleft()
        sortedorder.append(vertex)
        for child in graph[vertex]:
            inDegree[child]-=1
            if inDegree[child]==0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sortedorder)!= vertices:
        return []


    
    return sortedorder



def main():
    print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()



# Time Complexity :- O(V+E)
# Space Complexity - O(V+E) , where V is the vertices and E is the edge of the graph.