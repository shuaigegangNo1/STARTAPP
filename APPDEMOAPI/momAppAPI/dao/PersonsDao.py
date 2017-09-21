from util.MysqlUtil import MysqlUtil

ip = "localhost"
user = "root"
pwd = ""
database = "momapp"
table = "Persons"
conn = ""
mysql_util = MysqlUtil(ip, user, pwd, database, table, conn)


def get_person_list():
    sql = "select firstname,lastname,address,city from Persons"
    mysql_util.mysql_connect()
    rows = mysql_util.mysql_query(sql)
    return rows
