from Patient import Patient
from Maladie import Maladie

class Hopital:
    """
    classes Hopital
    """
    def __init__(self, nom : str, adresse : str, type_soins_offert : list):
        self.nom = nom
        self.adresse = adresse
        self.type_soins_offert = type_soins_offert

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def adresse(self):
        return self._adresse

    @adresse.setter
    def adresse(self, adresse):
        self._adresse = adresse

    @property
    def type_soins_offert(self):
        return self._type_soins_offert

    @type_soins_offert.setter
    def type_soins_offert(self, type_soins_offer):
        self._type_soins_offert = type_soins_offer


def verifier_besoins(self, patient: Patient):
    """
    Vérifier  les besoins du patient en verifiant la maladie est ressortant le soin necessaire.
    :param self: Hospital
    :param patient: Patient donner
    :return: soins necessaire
    """
    maladie_p : list = patient.maladies