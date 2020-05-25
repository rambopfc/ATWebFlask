import atws
import atws.monkeypatch.attributes
from app.Classes import companyclass

# needs from GetObject.GetCompany import get_companyinfo
# use like name = get_companyinfo(1432, at)


def get_companyinfo(id, atconnect):
    query = atws.Query('Account')
    query.WHERE('id', query.Equals, id)
    query.close_bracket()
    companys = atconnect.query(query)

    for company in companys:
        return companyclass.Company(company)
