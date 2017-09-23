class Person:
    # constructor
    def __init__(self, id, lastname, firstname, address, city, telephone):
        self.id = id
        self.LastName = lastname
        self.FirstName = firstname
        self.Address = address
        self.City = city
        self.telephone = telephone

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
