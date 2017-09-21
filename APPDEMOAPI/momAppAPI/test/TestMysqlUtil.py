from util.MysqlUtil import MysqlUtil
from dao.PersonsDao import get_person_list
from flaskext.mysql import MySQL
from flask import Flask
import datetime

if __name__ == "__main__":
    # 打开数据库连接
    # use pymysql to interact with mysql

    ip = "localhost"
    user = "root"
    pwd = ""
    database = "momapp"
    table = "Persons"
    conn = ""
    mysqlUtil = MysqlUtil(ip, user, pwd, database, table, conn)
    # sql = "select * from Persons"
    mysqlUtil.mysql_connect()
    # rows = mysqlUtil.mysql_query(sql)
    now = datetime.datetime.now()
    # datas = ['12', 'han', 'li', 'china', '盐城', str(now.strftime("%Y-%m-%d %H:%M:%S"))]
    person_dic = {'id': '15', 'first_name': 'xin', 'last_name': 'su', 'address': 'china', 'city': 'suzhou',
                  'telephone': '13424566', 'create_date': '2017-09-20'}
    persons = [person_dic['id'], person_dic['first_name'], person_dic['last_name'], person_dic['address'],
               person_dic['city'],
               person_dic['create_date'], person_dic['telephone']]
    mysqlUtil.mysql_insert_common(persons)

    # mysqlUtil.mysql_delete('2')
    # mysqlUtil.mysql_update('city', 'tijian', 'id_p', '6')
    # print(rows)
    # get_person_list()

    # use flask-mysql to interact with mysql

    # mysql = MySQL()
    # app = Flask(__name__)
    # app.config['MYSQL_DATABASE_USER'] = 'root'
    # app.config['MYSQL_DATABASE_PASSWORD'] = ''
    # app.config['MYSQL_DATABASE_DB'] = 'momapp'
    # app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    # mysql.init_app(app)
    # cursor = mysql.connect().cursor()
    # cursor.execute("SELECT * from persons")
    # data = cursor.fetchone()
    # print(data)
    persons = get_person_list()
    for person in persons:
        print(person[0])
