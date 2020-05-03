class Company:
    def __init__(self, account):

        if 'id' in account:
            self.ID = account['id']
        else:
            raise Exception("ID cannot be blank!")

        if 'AccountName' in account:
            self.Name = account['AccountName']
        else:
            raise Exception("Company name cannot be blank!")

        if 'Security PIN (Limited)' in account:
            self.LimitedPin = account['Security PIN (Limited)']
        else:
            self.LimitedPin = ""

        if 'Security PIN (TopSecret)' in account:
            self.TopSecretPin = account['Security PIN (TopSecret)']
        else:
            self.TopSecretPin = ""

        if 'Address1' in account:
            self.Address = account['Address1']
        else:
            self.Address = ""

        if 'Address2' in account:
            self.Address2 = account['Address2']
        else:
            self.Address2 = ""

        if 'City' in account:
            self.City = account['City']
        else:
            self.City = ""

        if 'PostalCode' in account:
            self.Zip = account['PostalCode']
        else:
            self.Zip = ""

        if "Phone" in account:
            self.Phone = account['Phone']
        else:
            self.Phone = ""
