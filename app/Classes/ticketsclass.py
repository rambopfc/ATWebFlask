from app.GetObject.GetCompany import get_companyinfo
from app.GetObject.GetCompanyContacts import get_companycontacts
from app.GetObject.GetSingleContact import get_singlecontact
from app.GetObject.GetStatus import get_status


class Ticket:

    def __init__(self, tickets, at):
        if 'Security PIN' in tickets:
            self.PIN = tickets['Security PIN']
        else:
            self.PIN = ""

        if 'N-Central Device Asset Tag' in tickets:
            self.Asset = tickets['N-Central Device Asset Tag']
        else:
            self.Asset = ""

        if 'id' in tickets:
            self.TicketID = tickets['id']
        else:
            raise Exception("Ticket ID cannot be blank!")

        # Really wanted to pass a class around here, but after moving to an API this was not really possible...
        companyinfo = get_companyinfo(tickets['AccountID'], at)
        self.CompanyID = companyinfo.ID
        self.CompanyName = companyinfo.Name
        self.CompanyLimitedPin = companyinfo.LimitedPin
        self.TopSecretPin = companyinfo.TopSecretPin
        self.CompanyAddress = companyinfo.Address
        self.CompanyAddress2 = companyinfo.Address2
        self.CompanyCity = companyinfo.City
        self.CompanyPostalCode = companyinfo.Zip
        self.CompanyPhone = companyinfo.Phone

        if 'ContactID' in tickets:
            # Same situation as above
            contact = get_singlecontact(tickets['ContactID'], at)
            self.ContactAddress = contact.Address
            self.ContactAddress2 = contact.Address1
            self.ContactAccountID = contact.ID
            self.ContactCity = contact.City
            self.ContactEmail = contact.Email
            self.ContactEmail2 = contact.Email2
            self.ContactFirst = contact.FirstName
            self.ContactLast = contact.LastName
            self.ContactID = contact.ID
            self.ContactCell = contact.CellPhone
            self.ContactPhone = contact.Phone
            self.ContactIsPrimary = contact.isPrimary
            self.ContactState = contact.State
            self.ContactZip = contact.ZipCode
            self.ContactTitle = contact.Title
        else:
            self.ContactAddress = ""
            self.ContactAddress2 = ""
            self.ContactAccountID = ""
            self.ContactCity = ""
            self.ContactEmail = ""
            self.ContactEmail2 = ""
            self.ContactFirst = ""
            self.ContactLast = ""
            self.ContactID = ""
            self.ContactCell = ""
            self.ContactPhone = ""
            self.ContactIsPrimary = ""
            self.ContactState = ""
            self.ContactZip = ""
            self.ContactTitle = ""

        if 'Priority' in tickets:
            self.Priority = tickets['Priority']
        else:
            self.Priority = ""

        if 'Title' in tickets:
            self.Title = tickets['Title']
        else:
            self.Title = ""

        if 'Description' in tickets:
            self.Description = tickets['Description']
        else:
            self.Description = ""

        if 'Status' in tickets:
            self.Status = get_status(tickets['Status'])
        else:
            self.Status = ""

        if 'Status' in tickets:
            self.StatusID = tickets['Status']
        else:
            self.StatusID = ""

        if 'QueueID' in tickets:
            self.QueueID = tickets['QueueID']
        else:
            self.QueueID = ""
