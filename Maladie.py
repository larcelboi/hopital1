from Hopital import Hopital

class Maladie:
    """
    classe Maladie
    """
    def __init__(self, nom_maladie : str, description : str, soins_efficaces : list):
        self.nom_maladie = nom_maladie
        self.description = description
        self.soins_efficaces = soins_efficaces

    @property
    def nom_maladie(self):
        return self._nom_maladie

    @nom_maladie.setter
    def nom_maladie(self, nom_maladie):
        self._nom_maladie = nom_maladie

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def soins_efficaces(self):
        return self._soins_efficaces

    @soins_efficaces.setter
    def soins_efficaces(self, soins_efficaces):
        self._soins_efficaces = soins_efficaces
