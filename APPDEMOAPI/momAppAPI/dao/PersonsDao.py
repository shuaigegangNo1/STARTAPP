from util.MysqlUtil import MysqlUtil

ip = "localhost"
user = "root"
pwd = ""
database = "momapp"
table = "Persons"
conn = ""
mysql_util = MysqlUtil(ip, user, pwd, database, table, conn)
mysql_util.mysql_connect()


def get_person_list():
    sql = "select id_p,firstname,lastname,address,city,telephone from Persons"
    rows = mysql_util.mysql_query(sql)
    return rows


def get_person(id_p):
    sql = "select * from Persons where id_p= " + "'" + id_p + "'"
    row = mysql_util.mysql_query(sql)
    return row
