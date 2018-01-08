from config.dbconfig import pg_config
import psycopg2

class BatteriesDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllBatteries(self):
        cursor = self.conn.cursor()
        query = "select * from batteries;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryById(self, bID):
        cursor = self.conn.cursor()
        query = "select * from batteries where bID = %s;"
        cursor.execute(query, (bID,))
        result = cursor.fetchone()
        return result

    def getBatteryByResourceId(self, resID):
        cursor = self.conn.cursor()
        query = "select * from batteries where resID = %s;"
        cursor.execute(query, (resID,))
        result = cursor.fetchone()
        return result

    def getBatteryByCategoryId(self, catID):
        cursor = self.conn.cursor()
        query = "select * from batteries where catID = %s;"
        cursor.execute(query, (catID,))
        result = cursor.fetchone()
        return result

    def getBatteryByType(self, bType):
        cursor = self.conn.cursor()
        query = "select * from batteries where bType = %s;"
        cursor.execute(query, (bType,))
        result = cursor.fetchone()
        return result

    def getBatteryByBrand(self, bBrand):
        cursor = self.conn.cursor()
        query = "select * from batteries where bBrand = %s;"
        cursor.execute(query, (bBrand,))
        result = cursor.fetchone()
        return result