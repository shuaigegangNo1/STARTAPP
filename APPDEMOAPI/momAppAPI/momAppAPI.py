from flask import Flask, jsonify, make_response, request
import dao.PersonsDao as personDao
import json

app = Flask(__name__)


def get_response(result):
    # response.headers['Access-Control-Allow-Methods'] = 'POST'
    # response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    response = make_response(jsonify(result=result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/momApp/person/detail')
def get_person_detail():
    id_p = request.args.get('id')
    person = personDao.get_person(id_p)
    response = get_response(person)
    return response


@app.route('/momApp/persons')
def get_person_list():
    persons = personDao.get_person_list()
    response = get_response(persons)
    return response


@app.route('/momApp/addPerson', methods=['GET', 'POST'])
def add_person():
    if request.method == 'POST':
        data = request.data
        person = json.loads(data)  # load将字符串解析成json
        mysqlUtil = personDao.open_connect_mysql()
        print("person_data", person)
        personList = [person['id'], person['firstname'], person['lastname'], person['address'],
                      person['city'], person['create_date'], person['telephone']]
        print(type(personList))
        result = mysqlUtil.mysql_insert_common(personList)
        response = get_response(result)
        personDao.close_connect_mysql(mysqlUtil)
        return response


@app.route('/momApp/updatePerson', methods=['GET', 'POST'])
def update_person():
    if request.method == 'POST':
        data = request.data
        person = json.loads(data)  # load将字符串解析成json
        mysqlUtil = personDao.open_connect_mysql()
        print("person_data", person)
        person_list = [person['lastname'], person['firstname'], person['address'],
                       person['city'], person['telephone'], person['id']]
        result = mysqlUtil.mysql_update_person(person_list)
        if result == 1:
            info = "更新成功"
        elif result == 0:
            info = "更新失败"
        response = get_response(info)
        personDao.close_connect_mysql(mysqlUtil)
        return response


@app.route('/momApp/deletePerson')
def delete_person():
    id_p = request.args.get('id')
    mysqlUtil = personDao.open_connect_mysql()
    result = mysqlUtil.mysql_delete(id_p)
    if result == 1:
        info = "删除成功"
    elif result == 0:
        info = "删除失败"
    personDao.close_connect_mysql(mysqlUtil)
    response = get_response(info)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
