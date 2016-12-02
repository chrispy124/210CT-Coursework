class node(object):

    def __init__(self,value):
        self.node = node
        self.a ={}

    def addOpposite(self, OppositeN): #Adds The Opposite Node
        self.a[OppositeN] = OppositeN

class unweightedGraph: #This creates the Graph to use
    def __init__(self):
        self.v = {}

    def addVertex(self,value): #Adds the vertex
        vertex = node(value)
        self.v[value] = vertex
        print ("Vertex Created " + str(value)) #This prints the vertex and name

    def addEdge(self, value, value2):
        self.v[value].addOpposite(self.v[value2]) #This adds the opposite vertex and connects it to the already connected vertex
        self.v[value2].addOpposite(self.v[value])

    def printGraph(self):
        List = []
        for key in self.v:
            List.append(key)
        for key in List:

            print(str(key))


graph = unweightedGraph()

graph.addVertex(1) 
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)

graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,4)

graph.printGraph()
