import atws
import atws.monkeypatch.attributes
from Classes import notesclass


def get_ticketnotes(ticketid, atconnect):
    query = atws.Query('TicketNote')
    query.WHERE('TicketID', query.Equals, ticketid)
    query.close_bracket()
    notes = atconnect.query(query)
    notelist = []

    for item in notes:
        x = notesclass.Notes(item)
        notelist.append(x)

    return notelist