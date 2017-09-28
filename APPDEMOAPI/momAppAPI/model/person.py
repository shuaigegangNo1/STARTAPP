class Person:
    # constructor
    # def __init__(self, id, lastname, firstname, address, city, telephone):
    #     self.id = id
    #     self.LastName = lastname
    #     self.FirstName = firstname
    #     self.Address = address
    #     self.City = city
    #     self.telephone = telephone
    def __init__(self):
        self.id = None
        self.id = None
        self.LastName = None
        self.FirstName = None
        self.Address = None
        self.City = None
        self.telephone = None

    def to_string(self):
        new_person = {}
        new_person['id'] = self.id
        new_person['lastname'] = self.LastName
        new_person['firstname'] = self.FirstName
        new_person['address'] = self.Address
        new_person['city'] = self.City
        new_person['telephone'] = self.telephone
        # return '{'+'LastName:' + self.LastName + ',' + 'FirstName:' + self.FirstName + \
        #         ',' + 'Address:' + self.Address + ',' + 'City:' + self.City + '}'
        # return "'" + str(newPerson) + "'"
        return new_person

    def get_persons_json_array(self, rows):
        persons_key = ["id_p", "firstname", "lastname", "address", "city", "create_date", "telephone"]
        persons_data = []
        for row in rows:
            row_data = {}
            for k, v in zip(persons_key, row):
                row_data[k] = v
            persons_data.append(row_data)
        return persons_data
