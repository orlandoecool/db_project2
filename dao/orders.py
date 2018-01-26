from config.dbconfig import pg_config
import psycopg2

class OrdersDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllOrders(self):
        cursor = self.conn.cursor()
        query = "select * from orders;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchOrdersByArguments(self, args):
        cursor = self.conn.cursor()
        arguments = ""
        values = list(args.values())
        for arg in args:
            arguments = arguments + arg + "= %s" + " and "
        arguments = arguments[:-5]  # Remove the last ' and '
        query = "select * from orders where " + arguments
        cursor.execute(query, values)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchOrdersWithSorting(self, orderby):
        cursor = self.conn.cursor()
        query = "select * from orders order by " + orderby
        cursor.execute(query)
        print(cursor.query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchOrdersByArgumentsWithSorting(self, args):
        cursor = self.conn.cursor()
        arguments = ""
        values = list(args.values())
        values.remove(args.get('orderby'))
        for arg in args:
            if arg != 'orderby':
                arguments = arguments + arg + "= %s" + " and "
        arguments = arguments[:-5]  # Remove the last ' and '
        query = "select * from orders where " + arguments + " order by " + args.get('orderby')
        cursor.execute(query, values)
        print(cursor.query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertPurchase(self, reqID, invID, ordQty, ordPrice):
        cursor = self.conn.cursor()
        query = "insert into orders(reqid, invid, ordqty, orddate, ordexpdate, ordtype, ordprice) values (%s, %s, %s, current_timestamp, NULL , 'Purchase', %s);"
        cursor.execute(query, (reqID, invID, ordQty, ordPrice,))
        self.conn.commit()

    def insertReserve(self, reqID, invID, ordQty, ordPrice):
        cursor = self.conn.cursor()
        query = "insert into orders(reqid, invid, ordqty, orddate, ordexpdate, ordtype, ordprice) values (%s, %s, %s, current_timestamp, current_timestamp + interval '7 day', 'Reserve', %s);"
        cursor.execute(query, (reqID, invID, ordQty, ordPrice,))
        self.conn.commit()

    def getDateByIds(self, reqID, invID):
        cursor = self.conn.cursor()
        query = "select ordDate from orders where reqID = %s and invID = %s"
        cursor.execute(query, (reqID, invID,))
        result = cursor.fetchone()
        return result

    def getExpDateByIds(self, reqID, invID):
        cursor = self.conn.cursor()
        query = "select ordExpDate from orders where reqID = %s and invID = %s"
        cursor.execute(query, (reqID, invID,))
        result = cursor.fetchone()
        return result

