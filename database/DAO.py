from database.DB_connect import DBConnect
from model.aeroporto import Aeroporto
from model.rotta import Rotta


class DAO():

    @staticmethod
    def get_all_aeroporti():
        cnx = DBConnect.get_connection()
        result = []

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * FROM airports a"""

        cursor.execute(query)

        for row in cursor:
            result.append(Aeroporto(**row))

        cursor.close()
        cnx.close()

        return result

    @staticmethod
    def get_all_rotte():
        cnx = DBConnect.get_connection()
        result = []

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT f.ORIGIN_AIRPORT_ID as a1, f.DESTINATION_AIRPORT_ID as a2, SUM(f.DISTANCE) as dist_tot, COUNT(*) as nVoli
                    FROM flights f
                    GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID"""

        cursor.execute(query)

        for row in cursor:
            result.append(Rotta(**row))

        cursor.close()
        cnx.close()
        return result
