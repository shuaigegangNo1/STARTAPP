class Person:
    # constructor
    def __init__(self, lastname, firstname, address, city):
        self.LastName = lastname
        self.FirstName = firstname
        self.Address = address
        self.City = city

    def to_string(self):
        newPerson = {}
        newPerson['LastName'] = self.LastName
        newPerson['FirstName'] = self.FirstName
        newPerson['Address'] = self.Address
        newPerson['City'] = self.City
        # return '{'+'LastName:' + self.LastName + ',' + 'FirstName:' + self.FirstName + \
        #         ',' + 'Address:' + self.Address + ',' + 'City:' + self.City + '}'
        # return "'" + str(newPerson) + "'"
        return newPerson
