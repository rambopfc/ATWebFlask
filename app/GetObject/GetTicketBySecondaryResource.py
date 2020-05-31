import atws
import atws.monkeypatch.attributes
from app.Classes import secondaryresource
from app.Classes import ticketsclass


def get_ticketbysecondary(resourceid, atconnect):
    query = atws.Query('TicketSecondaryResource')
    query.WHERE('ResourceID', query.Equals, resourceid)
    query.close_bracket()
    resources = atconnect.query(query).fetch_all()
    resourcelist = []

    for resource in resources:
        x = secondaryresource.SecondaryResource(resource)
        resourcelist.append(x)

    query2 = atws.Query('Ticket')
    query2.WHERE('QueueID', query2.Equals, 29682833)  # level 1 queue
    query2.WHERE('Status', query2.NotEqual, 5)
    query2.close_bracket()
    level1tickets = atconnect.query(query2).fetch_all()
    ticketlist = []
    finallist = []

    for ticket in level1tickets:
        x = ticketsclass.Ticket(ticket, atconnect)
        ticketlist.append(x)

    for x in resourcelist:
        for y in ticketlist:
            if x.TicketID == y.TicketID:
                finallist.append(y)
    return finallist
