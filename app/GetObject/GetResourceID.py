import atws
import atws.monkeypatch.attributes


def get_resourceID(emailaddress, atconnect):
    query = atws.Query('Resource')
    query.WHERE('email', query.Equals, emailaddress)
    query.close_bracket()
    name = atconnect.query(query)

    for people in name:
        return people['id']
