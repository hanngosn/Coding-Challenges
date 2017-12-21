#Graph Implementation

class Vertex:
	def __init__(self,key):
		self.id = key
		self.connectedTo = {}			#key: other vertexes, dic[key]: weight 

	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr] = weight

	def __str__(self):
		return str(self.id) + " connected to: " + str([x.id for x in self.connectedTo])  

	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self, nbr):
		return self.connectedTo[nbr]

class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self, key):
		self.numVertices += 1
		vert = Vertex(key)
		self.vertList[key] = vert
		return vert

	def getVertex(self, key):	#key (number) to find the vertex as object 
		if key in self.vertList:
			return self.vertList[key]
		else:
			return None 

	def __contains__(self, key):
		return key in self.vertList

	def addEdge(self, a, b, cost = 0): #one-way not transitive I guess
		if a not in self.vertList:
			nv = self.addVertex(a)
		if b not in self.vertList:
			nv = self.addVertex(b)
		self.vertList[a].addNeighbor(self.vertList[b], cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):	#iterate through all vertex objects in the graph
		return iter(self.vertList.values())

g = Graph()
g.addVertex(i for i in range(7))
g.addEdge(1,2,5)
g.addEdge(2,3,6)
g.addEdge(3,4,7)
g.addEdge(4,5,8)
g.addEdge(4,6,9)
g.addEdge(5,6,9)
g.addEdge(6,0,10)		
# print(g.getVertices())
print(g.getVertex(4))
for v in g:
	for w in v.getConnections():
		print("{} - {} (weight: {})".format(v.getId(), w.getId(), v.getWeight(w)))

##################### Word Ladder Problem ####################
