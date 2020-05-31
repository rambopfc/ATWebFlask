from requests import Response
from app import app
from flask import render_template, jsonify, abort, json
import atws.monkeypatch.attributes
import os
from app.GetObject.GetCompany import get_companyinfo
from app.GetObject.GetCompanyContacts import get_companycontacts
from app.GetObject.GetResourceID import get_resourceID
from app.GetObject.GetSingleContact import get_singlecontact
from app.GetObject.GetStatus import get_status
from app.GetObject.GetSingleTicket import get_singleticket
from app.GetObject.GetTicketNotes import get_ticketnotes
from app.GetObject.GetTicketByResource import get_ticketbyresource
from app.GetObject.Getlevelone import get_levelone

at = atws.connect(username=os.environ.get('AT_USER'), password=os.environ.get('AT_PW'), apiversion=1.6,
                  integrationcode=os.environ.get('AT_CODE'))


@app.route('/')
@app.route('/index')
def index():
    abort(401)


#WORKING
@app.route('/getcompany/<int:company_id>', methods=['GET'])
def returncompany(company_id):
    comp = get_companyinfo(company_id, at)
    return jsonify({'Company': comp.__dict__})


# WORKING
@app.route('/getticketnotes/<int:ticket_id>', methods=['GET'])
def returnnotes(ticket_id):
    notes = get_ticketnotes(ticket_id, at)
    json_string = jsonify([note.__dict__ for note in notes])
    return json_string


# Working
@app.route('/getticket/<int:ticket_id>', methods=['GET'])
def singleticket(ticket_id):
    ticket = get_singleticket(ticket_id, at)
    return jsonify({'Ticket': ticket.__dict__})
    # return json.loads(json.dumps(ticket, default=lambda o: o.__dict__))

# Working
@app.route('/gettickets/<string:email>', methods=['GET'])
def gettickets(email):
    resourceid = get_resourceID(email, at)
    tickets = get_ticketbyresource(resourceid, at)
    # jsontickets = jsonify({'Ticket': ticket.__dict__ for ticket in tickets})
    jsontickets = ""
    for ticket in tickets:
        jsontickets += json.dumps(ticket, default=lambda o: o.__dict__)

    return jsontickets


@app.route('/getlevelone')
def getlvlone():
    tickets = get_levelone(at)
    jsontickets = ""
    for ticket in tickets:
        jsontickets += json.dumps(ticket, default=lambda o: o.__dict__)

    return jsontickets

