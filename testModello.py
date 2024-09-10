from model.model import Model
import networkx as nx

mymodel = Model()
mymodel.crea_grafo(309)
print(len(mymodel._edges))
print(mymodel.getNumEdges())
