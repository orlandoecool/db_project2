from config.dbconfig import pg_config
import psycopg2

class ClothingsDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllClothings(self):
        cursor = self.conn.cursor()
        query = "select * from clothings;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothingById(self, clothID):
        cursor = self.conn.cursor()
        query = "select * from clothings where clothID = %s;"
        cursor.execute(query, (clothID,))
        result = cursor.fetchone()
        return result