from util.MysqlUtil import MysqlUtil
from model.person import Person

ip = "localhost"
user = "root"
pwd = ""
database = "momapp"
table = "Persons"
conn = ""


def open_connect_mysql():
    mysql_util = MysqlUtil(ip, user, pwd, database, table, conn)
    mysql_util.mysql_connect()
    return mysql_util


def close_connect_mysql(mysql_util):
    mysql_util.mysql_close()


def get_person_list(start, pagesize):
    mysql_util = open_connect_mysql()
    sql = "select id_p,firstname,lastname,address,city,telephone from Persons limit " + start + "," + pagesize
    rows = mysql_util.mysql_query(sql)
    close_connect_mysql(mysql_util)
    return rows


def get_person(id_p):
    mysql_util = open_connect_mysql()
    sql = "select * from Persons where id_p= " + "'" + id_p + "'"
    person = mysql_util.mysql_query(sql)
    N_Person = Person(person[0][0], person[0][1], person[0][2], person[0][3], person[0][4], person[0][6])
    close_connect_mysql(mysql_util)
    return N_Person.to_string()


def update_person(update_person, id_p):
    mysql_util = open_connect_mysql()
    sql = "update Persons set "
    sql += "where id_p = " + "'" + id_p + "'"
    result = mysql_util.mysql_update_common(sql)
    close_connect_mysql(mysql_util)
    return result


def get_person_list_like(param, start, pagesize):
    mysql_util = open_connect_mysql()
    result = mysql_util.mysql_query_like('firstname', param, start, pagesize)
    close_connect_mysql(mysql_util)
    return result
