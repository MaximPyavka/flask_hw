from app.db_utils.create_db import connect_db

class User:
    col_names = ['CustomerId', 'FirstName', 'LastName',
                 'Company', 'Address', 'City', 'State',
                 'Country', 'PostalCode', 'Phone',
                 'Fax', 'Email', 'SupportRepId'
                 ]

    def __init__(self, tab):
        self.CustomerId = tab[0]
        self.FirstName = tab[1]
        self.LastName = tab[2]
        self.Company = tab[3]
        self.Address = tab[4]
        self.City = tab[5]
        self.State = tab[6]
        self.Country = tab[7]
        self.PostalCode = tab[8]
        self.Phone = tab[9]
        self.Fax = tab[10]
        self.Email = tab[11]
        self.SupportRepId = tab[12]

    def get_dict(self):
         return self.__dict__

