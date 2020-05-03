import atws.monkeypatch.attributes
import os
from GetObject.GetResourceID import get_resourceID

at = atws.connect(username=os.environ.get('AT_USER'), password=os.environ.get('AT_PW'), apiversion=1.6, integrationcode=os.environ.get('AT_CODE'))
# print(at.kwargs)

query = atws.Query('Ticket')
query.WHERE('AssignedResourceID', query.Equals, get_resourceID('joe@thecomputerwarriors.com', at))
query.open_bracket('AND')
query.OR('Status', query.NotEqual, at.picklist['Ticket']['Status']['Complete'])

query.close_bracket()

tickets = at.query(query).fetch_all()
# enumerate them
# for ticket in tickets:
#     print(ticket)

for ticket in tickets:
    print(list(ticket))
    # test = ticketsclass.Ticket(ticket)
    # print(test.PIN)

# x = get_resourceID('joe@thecomputerwarriors.com', at)
# print(x)

