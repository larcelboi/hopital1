from Hopital import Hopital
from Maladie import Maladie

class Patient:
    """
    Classe Patient
    """
    def __init__(self, prenom : str, nom : str, age : int, carte_AM : str, maladies : list[Maladie]):
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.carte_AM = carte_AM
        self.maladies = maladies

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, prenom):
        self._prenom = prenom

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def carte_AM(self):
        return self._carte_AM

    @carte_AM.setter
    def carte_AM(self, carte_AM):
        self._carte_AM = carte_AM

    @property
    def maladies(self):
        return self._maladies

    @maladies.setter
    def maladies(self, maladies):
        self._maladies = maladies