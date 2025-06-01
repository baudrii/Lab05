from database.DB_connect import DBConnect

from model.corso import Corso
class DAO():

    @staticmethod
    def getAllCorsi():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                from corso c """

        cursor.execute(query)

        for row in cursor:
            results.append(Corso(**row))

        cursor.close()
        conn.close()
        return results