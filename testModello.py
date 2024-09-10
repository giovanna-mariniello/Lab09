from model.model import Model
import networkx as nx

mymodel = Model()
mymodel.crea_grafo(120)
print(f"Numero nodi: {mymodel.getNumNodes()}")
print(f"Numero archi non filtrati: {len(mymodel._edges)}")
print(f"Numero archi filtrati: {mymodel.getNumEdges()}")
