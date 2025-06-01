from database.corso_DAO import DAO as DAO1
from database.studente_DAO import DAO as DAO2


class Model:
    def __init__(self):
        pass

    def getCorsi(self):
        return DAO1.getAllCorsi()

    def getIscrittiCorsi(self,codins):
        return DAO2.getAllStudentiCorso(codins)

    def getStudente(self,matricola):
        return DAO2.getStudente(matricola)

    def getCorsiperStudente(self,matricola):
        return DAO2.getAllCorsiperStudente(matricola)