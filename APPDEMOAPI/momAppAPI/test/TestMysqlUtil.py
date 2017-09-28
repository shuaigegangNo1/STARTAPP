from util.MysqlUtil import MysqlUtil
from dao.PersonsDao import get_person_list
from dao.PersonsDao import get_person_list_like
from flaskext.mysql import MySQL
from flask import Flask
import datetime
from model.person import Person

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
    # datas = ["12", "han", "li", "china", "盐城", str(now.strftime("%Y-%m-%d %H:%M:%S"))]
    # person_dic = {"id": "15", "first_name": "xin", "last_name": "su", "address": "china", "city": "suzhou",
    #               "telephone": "13424566", "create_date": "2017-09-20"}
    # persons = [person_dic["id"], person_dic["first_name"], person_dic["last_name"], person_dic["address"],
    #            person_dic["city"],
    #            person_dic["create_date"], person_dic["telephone"]]
    # mysqlUtil.mysql_insert_common(persons)

    # mysqlUtil.mysql_delete("2")
    # mysqlUtil.mysql_update("city", "tijian", "id_p", "6")
    # print(rows)
    # get_person_list()

    # use flask-mysql to interact with mysql

    # mysql = MySQL()
    # app = Flask(__name__)
    # app.config["MYSQL_DATABASE_USER"] = "root"
    # app.config["MYSQL_DATABASE_PASSWORD"] = ""
    # app.config["MYSQL_DATABASE_DB"] = "momapp"
    # app.config["MYSQL_DATABASE_HOST"] = "localhost"
    # mysql.init_app(app)
    # cursor = mysql.connect().cursor()
    # cursor.execute("SELECT * from persons")
    # data = cursor.fetchone()
    # print(data)
    # persons = get_person_list()
    # for person in persons:
    #     print(person[0])
    # parmas = ["shiguo", "xu", "china", "changzhou", "13262722816", "3"]
    # res = mysqlUtil.mysql_update_person(parmas)
    # print("res>>>", res)
    # rows66 =get_person_list();
    # print(rows66[0])
    # res = mysqlUtil.mysql_delete("7s")
    # res = mysqlUtil.mysql_query_like("firstname", "", "0", "2")
    # res = get_person_list("0", "2")
    # print(res)
    # # get item in dict
    # data = {"user": 1, "name": "Max", "three": 4}
    # is_admin = data.get("user", False)
    # print(is_admin)
    #
    # teams = ["Packers", "49ers", "Ravens", "Patriots"]
    # keys = ["111", "222", "333", "444"]
    # print({key: value for value, key in zip(teams, keys)})
    rows = get_person_list_like("", "0", "10")
    persons_key = ["id_p", "firstname", "lastname", "address", "city", "create_date", "telephone"]
    print(rows)
    # data = []

    # for row in rows:
    #     row_data = {}
    #     # for i in range(len(row)):
    #     #     row_data["name"] = row[1]
    #     for k, v in zip(persons_key, row):
    #         row_data[k] = v
    #     data.append(row_data)
    person = Person()
    data = person.get_persons_json_array(rows)
    print(data)
        # for r_v in row:
        #     print(r_v)
        # print(data)