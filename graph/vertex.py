class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVetex = Vertex(key)
        self.vertexList[key] = newVetex
        return newVetex

    def getVertex(self, n):
        for n in self.vertexList:
            return self.vertexList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertexList

    def addEdge(self, f, t, cost=0):
        if f not in vertexList:
            nv = self.addVertex(f)
        if t not in vertexList:
            nv = self.addVertex(t)
        self.vertexList[f].addNeighbor(self.vertexList[t], cost)

    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())
