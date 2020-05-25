from app import app
from flask import render_template, jsonify
import atws.monkeypatch.attributes
import os
from app.GetObject.GetCompany import get_companyinfo
from app.GetObject.GetCompanyContacts import get_companycontacts
from app.GetObject.GetResourceID import get_resourceID
from app.GetObject.GetSingleContact import get_singlecontact
from app.GetObject.GetStatus import get_status
from app.GetObject.GetSingleTicket import get_singleticket
from app.GetObject.GetTicketNotes import get_ticketnotes

at = atws.connect(username=os.environ.get('AT_USER'), password=os.environ.get('AT_PW'), apiversion=1.6,
                  integrationcode=os.environ.get('AT_CODE'))


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Home")

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

