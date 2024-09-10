from dataclasses import dataclass
from model.aeroporto import Aeroporto
@dataclass
class Rotta:
    a1: Aeroporto
    a2: Aeroporto
    dist_tot: float
    nVoli: int

    def __post_init__(self):
        self.avgDistance = float(self.dist_tot / self.nVoli)

    @property
    def a1(self):
        return self._a1

    @a1.setter
    def a1(self, value):
        self._a1 = value

    @property
    def a2(self):
        return self._a2

    @a2.setter
    def a2(self, value):
        self._a2 = value

    @property
    def dist_tot(self):
        return self._dist_tot

    @dist_tot.setter
    def dist_tot(self, value):
        self._dist_tot = value

    @property
    def nVoli(self):
        return self._nVoli

    @nVoli.setter
    def nVoli(self, value):
        self._nVoli = value

    @property
    def avgDistance(self):
        return self._avgDistance

    @avgDistance.setter
    def avgDistance(self, value):
        self._avgDistance = value

    def __eq__(self, other):
        return ((self.a1 == other.a2) and (self.a2 == other.a1))

    def __hash__(self):
        return hash(self.a1, self.a2)