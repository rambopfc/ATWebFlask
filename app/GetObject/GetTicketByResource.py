import atws
import atws.monkeypatch.attributes
from app.Classes import ticketsclass
from app.GetObject.GetTicketBySecondaryResource import get_ticketbysecondary


def get_ticketbyresource(resourceid, atconnect):
    query = atws.Query('Ticket')
    query.WHERE('AssignedResourceID', query.Equals, resourceid)
    query.WHERE('Status', query.NotEqual, 5)  # not complete
    query.WHERE('QueueID', query.NotEqual, 29683354)  # reoccurring queue
    query.close_bracket()
    tickets = atconnect.query(query).fetch_all()
    ticketlist = []

    for ticket in tickets:
        x = ticketsclass.Ticket(ticket, atconnect)
        ticketlist.append(x)

    secondarylist = get_ticketbysecondary(resourceid,atconnect)
    mergedlist = [*ticketlist, *secondarylist]

    return mergedlist
