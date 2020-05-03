import atws.monkeypatch.attributes
import os
from Classes import companyclass
from Classes import ticketsclass
from GetObject import GetCompany
from GetObject.GetCompany import get_companyinfo
from GetObject.GetCompanyContacts import get_companycontacts
from GetObject.GetSingleTicket import get_singleticket
from GetObject.GetTicketNotes import get_ticketnotes

at = atws.connect(username=os.environ.get('AT_USER'), password=os.environ.get('AT_PW'), apiversion=1.6,
                  integrationcode=os.environ.get('AT_CODE'))
# print(at.kwargs)

# query = atws.Query('Ticket')
# query.WHERE('id', query.Equals, '265647')
#
# query.close_bracket()
#
# tickets = at.query(query).fetch_all()
#
# for ticket in tickets
#     ti

tests = get_ticketnotes(267586, at)

for test in tests:
    print("__________________________________________________")
    print(test.TicketID)
    print(test.Title)
    print(test.Date)
    print(test.ID)
    print(test.Publish)
    print(test.PublishID)
    print(test.NoteType)
    print(test.Description)
    print(test.NoteTypeID)
    print("____________________________________________________")





