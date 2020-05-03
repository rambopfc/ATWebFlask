class Contact:
    def __init__(self, companycontact):
        if 'AddressLine' in companycontact:
            self.Address = companycontact['AddressLine']
        else:
            self.Address = ""

        if 'AddressLine1' in companycontact:
            self.Address1 = companycontact['AddressLine1']
        else:
            self.Address1 = ""

        if 'AccountID' in companycontact:
            self.AccountID = companycontact['AccountID']
        else:
            raise Exception("Account ID cannot be blank!")

        if 'City' in companycontact:
            self.City = companycontact['City']
        else:
            self.City = ""

        if 'EMailAddress' in companycontact:
            self.Email = companycontact['EMailAddress']
        else:
            raise Exception("Email address cannot be blank!")

        if 'EMailAddress2' in companycontact:
            self.Email2 = companycontact['EMailAddress2']
        else:
            self.Email2 = ""

        if 'FirstName' in companycontact:
            self.FirstName = companycontact['FirstName']
        else:
            raise Exception("First name cannot be blank!")

        if 'LastName' in companycontact:
            self.LastName = companycontact['LastName']
        else:
            raise Exception("Last name cannot be blank!")

        if 'id' in companycontact:
            self.ID = companycontact['id']
        else:
            raise Exception("ID cannot be blank!")

        if 'MobilePhone' in companycontact:
            self.CellPhone = companycontact['MobilePhone']
        else:
            self.CellPhone = ""

        if 'Phone' in companycontact:
            self.Phone = companycontact['Phone']
        else:
            self.Phone = ""

        if 'PrimaryContact' in companycontact:
            self.isPrimary = companycontact['PrimaryContact']
        else:
            self.isPrimary = False

        if 'State' in companycontact:
            self.State = companycontact['State']
        else:
            self.State = ""

        if 'ZipCode' in companycontact:
            self.ZipCode = companycontact['ZipCode']
        else:
            self.ZipCode = ""

        if 'Title' in companycontact:
            self.Title = companycontact['Title']
        else:
            self.Title = ""

