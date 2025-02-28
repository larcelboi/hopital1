from Patient import Patient
from Maladie import Maladie

class Hopital:
    """
    classes Hopital
    """
    def __init__(self, nom : str, adresse : str, patient : list[Patient], type_soins_offert : list):
        self.nom = nom
        self.adresse = adresse
        self.patient = patient
        self.type = type_soins_offert

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
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, patient):
        self._patient = patient

    @property
    def type_soins_offert(self):
        return self._type_soins_offert

    @type_soins_offert.setter
    def type(self, type_soins_offer):
        if type_soins_offer in ["urgent", "moins urgent", "normal", "enfant"]:
            self._type_soins_offert = type_soins_offer


def verifier_besoins(self, patient: Patient):
    """
    Vérifier  les besoins du patient et l'envoyer à l'hopital approprié.
    :param self: Hospital
    :param patient: Patient donner
    :return: soins necessaire
    """
    maladie_p : list = patient.maladies
    age_p : int = patient.age



