class SecondaryResource:
    def __init__(self, resource):

        if 'id' in resource:
            self.ID = resource['id']
        else:
            raise Exception("ID cannot be blank!")

        if 'ResourceID' in resource:
            self.ResourceID = resource['ResourceID']
        else:
            raise Exception("Resource ID cannot be blank!")

        if 'RoleID ' in resource:
            self.RoleID = resource['RoleID']
        else:
            self.RoleID = ""

        if 'TicketID' in resource:
            self.TicketID = resource['TicketID']
        else:
            self.TicketID = ""
