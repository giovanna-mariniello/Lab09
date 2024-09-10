import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._edges = None
        self._nodes = None
        self._grafo = nx.Graph()
        self._idMap = {}

    def crea_grafo(self, distanza_minima):
        self._grafo.clear()

        self._nodes = DAO.get_all_aeroporti()
        self.riempi_idMap()
        self._grafo.add_nodes_from(self._nodes)

        self._edges = DAO.get_all_rotte()

        for edge in self._edges:
            w = edge.avgDistance
            a1Obj = self._idMap[edge.a1]
            a2obj = self._idMap[edge.a2]
            if w > distanza_minima:
                self._grafo.add_edge(a1Obj, a2obj, weight=w)
                #print("Arco aggiunto: ", edge)

    def riempi_idMap(self):
        for n in self._nodes:
            self._idMap[n.ID] = n


    def getNumEdges(self):
        return self._grafo.number_of_edges()

    def getNumNodes(self):
        return self._grafo.number_of_nodes()

