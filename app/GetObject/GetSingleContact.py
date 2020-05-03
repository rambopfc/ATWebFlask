import atws
import atws.monkeypatch.attributes
from Classes import contactclass

# needs from GetObject.GetSingleContact import get_singlecontact
# use like name = get_singlecontact(1432, at)


def get_singlecontact(contactID, atconnect):
    query = atws.Query('Contact')
    query.WHERE('id', query.Equals, contactID)
    query.close_bracket()
    contacts = atconnect.query(query)

    for person in contacts:
        return contactclass.Contact(person)