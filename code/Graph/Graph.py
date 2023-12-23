class Graph:
    def __init__(self, vertices):
        # number of vertices in the graph
        self.vertices = vertices
        # create a list which can take all the linked list of the vertices
        self.array = []
        # create linked list of each vertices
        for i in range(vertices):
            self.array.append(Linked_List())
            
