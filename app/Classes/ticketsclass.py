from GetObject.GetCompany import get_companyinfo
from GetObject.GetCompanyContacts import get_companycontacts
from GetObject.GetSingleContact import get_singlecontact
from GetObject.GetStatus import getstatus


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

        companyinfo = get_companyinfo(tickets['AccountID'], at)
        self.Company = companyinfo

        contact = get_singlecontact(tickets['ContactID'], at)
        self.Contact = contact

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
            self.Status = getstatus(tickets['Status'])
        else:
            self.Status = ""

        if 'Status' in tickets:
            self.StatusID = tickets['Status']
        else:
            self.Status = ""