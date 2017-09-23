from model.person import Person
from dao.PersonsDao import get_person
import json

# person = Person('shuai', 'su', 'china', 'shanghai')
# print(person.to_string())

# newPerson = json.dumps(person.to_string())
# newPerson = person.to_string()
# lname = newPerson.get('FirstName')
# print(lname)
# # newPerson1 = json.loads(person.to_string())
# print(type(newPerson.get('LastName')))
# for attr in newPerson:
#     print(attr
# persons = ['2', 'hh', '233', 'suzhou', 'china']
sql = ""
person_dic = {'id': '15', 'first_name': 'xin', 'last_name': 'su', 'address': 'china', 'city': 'suzhou',
              'telephone': '13424566', 'create_date': '2017-09-20'}
# persons = [person_dic['id'], person_dic['first_name'], person_dic['last_name'], person_dic['address'], person_dic['city'],
#            person_dic['create_date'], person_dic['telephone']]
# for i in range(persons.__len__()):
#     if i == 0:
#         sql += "'" + persons[i] + "'"
#         print(persons[i])
#     elif i == persons.__len__() - 1:
#         sql += "," + "'" + persons[i] + "'" + ")"
#         print(persons[i])
#     else:
#         sql += "," + "'" + persons[i] + "'"
#         print(persons[i])
# print(sql)
person = get_person('3')
# n_person = Person(person[0][0], person[0][1], person[0][2], person[0][3], person[0][4], person[0][6])
# print(n_person.to_string())
print(person)