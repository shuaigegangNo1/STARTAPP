import pymysql


class MysqlUtil(object):
    def __init__(self, host, user, password, database, table, conn):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table = table
        self.conn = conn

    def mysql_connect(self):
        try:
            self.conn = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8')
            self.cursor = self.conn.cursor()
            print("connect mysql succeed")
        except:
            print("connect mysql failed.")

    def mysql_query(self):
        try:
            sql = "select * from " + self.table + " limit 10"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            # print(rows)
        except:
            print(sql + "query failed")
        return rows

    def mysql_query(self, sql):
        try:
            # sql = "select * from " + self.table + " limit 10"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            # print(rows)
        except:
            print(sql + "query failed")
        return rows

    def mysql_query_one(self):
        try:
            sql = "select * from " + self.table + " order by rand()"
            self.cursor.execute(sql)
            rows = self.cursor.fetchone()
            # print(rows)
        except:
            print(sql + "query failed")
        return rows

    def mysql_insert(self, arg0, arg1, arg2, arg3, arg4, arg5):
        try:
            # sql = "insert into " + self.table + "  values(" +arg0+","+arg1+","+arg2+")"
            sql = "INSERT INTO " + self.table + " VALUES(" + arg0 + "," + "'" + arg1 + "'" + "," + "'" + arg2 + "'" + \
                  "," + "'" + arg3 + "'" + "," + "'" + arg4 + "'" + "," + "'" + arg5 + "'" + ")"
            self.cursor.execute(sql)
            self.conn.commit()
            print(sql + "insert succeed")
        except:
            self.conn.commit()
            print(sql + "insert failed")

    def mysql_insert_common(self, data_items=[]):
        try:
            result = True
            sql = "INSERT INTO " + self.table + " VALUES("
            print("data_items>>", data_items.__len__())
            for i in range(7):
                print(">>>enter range", data_items[i])
                if i == 0:
                    sql += "'" + data_items[i] + "'"
                elif i == data_items.__len__() - 1:
                    sql += "," + "'" + data_items[i] + "'" + ")"
                else:
                    sql += "," + "'" + data_items[i] + "'"
            self.cursor.execute(sql)
            self.conn.commit()
            print(sql + " insert succeed")
        except:
            self.conn.commit()
            result = False
            print(sql + " insert failed")
        return result

    def mysql_delete(self, arg0):
        try:
            sql = "DELETE FROM " + self.table + " WHERE ID_P= " + "'" + arg0 + "'"
            result = self.cursor.execute(sql)
            self.conn.commit()
            print(sql + " delete succeed")
        except:
            self.conn.commit()
            result = 0
            print(sql + " delete failed")
        return result

    def mysql_update(self, column1, arg0, column2, arg1):
        try:
            sql = "UPDATE " + self.table + " SET " + column1 + " = " + "'" + arg0 + "'" + \
                  " WHERE " + column2 + " = " + "'" + arg1 + "'"
            self.cursor.execute(sql)
            self.conn.commit()
            print(sql + " update succeed")
        except:
            self.conn.commit()
            print(sql + " update failed")

    def mysql_update_common(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            result = True
            print(sql + " update succeed")
        except:
            self.conn.commit()
            result = False
            print(sql + " update failed")
        return result

    '''
    return 1 means update succeed
    return 0 means update failed
    '''

    def mysql_update_person(self, params):
        try:
            sql = "update persons set lastname=%s, firstname=%s, address=%s, city=%s, telephone=%s where id_p=%s"
            result = self.cursor.execute(sql, (params[0], params[1], params[2], params[3], params[4], params[5]))
            self.conn.commit()
            print(sql + " update succeed")
        except:
            self.conn.commit()
            print(sql + " update failed")
        return result

    def mysql_close(self):
        self.cursor.close()
        self.conn.close()
