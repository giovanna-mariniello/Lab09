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
        filtrata = self.filtra_edges(self._edges)
        self._grafo.add_edges_from(filtrata)

    def riempi_idMap(self):
        for n in self._nodes:
            self._idMap[n.ID] = n

    def filtra_edges(self, lista_edges):
        filtrata = set()
        for e1 in lista_edges:
            for e2 in lista_edges:
                if e1 == e2:
                    filtrata.add(e1)

        return filtrata
