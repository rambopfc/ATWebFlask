import atws
import atws.monkeypatch.attributes
from app.Classes import contactclass

# needs from GetObject.GetCompanContacts import get_companycontacts
# use like name = get_companycontacts(1432, at)


def get_companycontacts(companyID, atconnect):
    query = atws.Query('Contact')
    query.WHERE('AccountID', query.Equals, companyID)
    query.close_bracket()
    contacts = atconnect.query(query)

    contactlist = []

    for person in contacts:
        x = contactclass.Contact(person)
        contactlist.append(x)

    return contactlist