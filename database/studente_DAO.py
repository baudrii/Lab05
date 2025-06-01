from database.DB_connect import DBConnect
from model.corso import Corso

from model.studente import Studente

class DAO():

    @staticmethod
    def getAllStudentiCorso(codins):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select s.matricola ,s.cognome, s.nome, s.CDS
    from studente s , iscrizione i
    where s.matricola=i.matricola and i.codins=%s """

        cursor.execute(query,(codins,))

        for row in cursor:
            results.append(Studente(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getStudente(matricola):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
        from studente s 
        where s.matricola=%s """

        cursor.execute(query, (matricola,))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row:
            return Studente(**row)
        else:
            return None

    def getAllCorsiperStudente(matricola):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select c.codins, c.crediti, c.nome, c.pd
             from studente s , iscrizione i, corso c
         where s.matricola=i.matricola and s.matricola=%s and i.codins=c.codins"""

        cursor.execute(query,(matricola,))

        for row in cursor:
            results.append(Corso(**row))

        cursor.close()
        conn.close()
        return results
