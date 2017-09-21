from flask import Flask, jsonify, make_response, request
import dao.PersonsDao as personDao
from model.person import Person
import json
from util.MysqlUtil import MysqlUtil

app = Flask(__name__)
ip = "localhost"
user = "root"
pwd = ""
database = "momapp"
table = "Persons"
conn = ""
mysqlUtil = MysqlUtil(ip, user, pwd, database, table, conn)


@app.route('/momApp/person/detail')
def get_person_detail():
    id_p = request.args.get('id')
    person = personDao.get_person(id_p)
    response = make_response(jsonify(person=person))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/momApp/persons')
def get_person_list():
    # rows = personDao.get_person_list()

    # response.headers['Access-Control-Allow-Methods'] = 'POST'
    # response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    # person = Person('shuai', 'su', 'china', 'shanghai')
    # NewPerson = person.to_string()
    persons = personDao.get_person_list()
    response = make_response(jsonify(person=persons))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/momApp/addPerson', methods=['GET', 'POST'])
def add_person():
    # response.headers['Access-Control-Allow-Methods'] = 'POST'
    # response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    if request.method == 'POST':
        data = request.data
        person = json.loads(data)  # load将字符串解析成json
        mysqlUtil.mysql_connect()
        print("person_data", person)
        personList = [person['id'], person['firstname'], person['lastname'], person['address'],
                      person['city'], person['create_date'], person['telephone']]
        print(type(personList))
        result = mysqlUtil.mysql_insert_common(personList)
        response = make_response(jsonify(result={"result": result}))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
