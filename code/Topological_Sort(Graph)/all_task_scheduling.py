from collections import deque

def find_order(tasks,prerequisites):
    sortedOrder = []
    if tasks<=0:
        return sortedOrder
    # initialize the graph
    inDegree = {i:0 for i in range(tasks)}
    graph = {i:[] for i in range(tasks)}
    # build the graph
    for prerequisite in prerequisites:
        parent, child = prerequisite[0], prerequisite[1]
        graph[parent].append(child)
        inDegree[child]+=1
    # find all sources
    sources = deque()
    for key in inDegree:
        if inDegree[key]==0:
            sources.append(key)
    # for each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    find_all_order(graph,inDegree,sources,sortedOrder)


def find_all_order(graph,inDegree,sources,sortedOrder):
    if sources:
        for vertex in sources:
            sortedOrder.append(vertex)
            for child in graph[vertex]:
                inDegree[child]-=1
                if inDegree[child]==0:
                    sources.append(child)
            sources.popleft()
            find_all_order(graph,inDegree,sources,sortedOrder)
            sortedOrder.remove(vertex)
            for child in graph[vertex]:
                inDegree[child]+=1
            sources.appendleft(vertex)
    if len(sortedOrder)==len(inDegree):
        print(sortedOrder)

def main():
    find_all_order({0:[1,2],1:[3],2:[3],3:[]},{0:0,1:1,2:1,3:2},deque([0]),[])
    find_all_order({0:[1,2],1:[3],2:[3],3:[]},{0:0,1:1,2:1,3:2},deque([0]),[])
    find_all_order({0:[1,2],1:[3],2:[3],3:[]},{0:0,1:1,2:1,3:2},deque([0]),[])

main()
            