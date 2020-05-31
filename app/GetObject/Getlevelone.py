import atws
import atws.monkeypatch.attributes
from app.Classes import ticketsclass


def get_levelone(atconnect):
    query = atws.Query('Ticket')
    query.WHERE('QueueID', query.Equals, 29682833)  # level 1 queue
    query.WHERE('Status', query.NotEqual, 5)  # not completed
    query.close_bracket()
    level1tickets = atconnect.query(query).fetch_all()
    ticketlist = []

    for ticket in level1tickets:
        x = ticketsclass.Ticket(ticket, atconnect)
        ticketlist.append(x)

    return ticketlist