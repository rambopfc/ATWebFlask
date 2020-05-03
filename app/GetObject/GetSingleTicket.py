import atws
import atws.monkeypatch.attributes
from Classes import ticketsclass


def get_singleticket(ticketid, atconnect):
    query = atws.Query('Ticket')
    query.WHERE('id', query.Equals, ticketid)
    query.close_bracket()
    tickets = atconnect.query(query).fetch_all()

    for ticket in tickets:
        return ticketsclass.Ticket(ticket, atconnect)