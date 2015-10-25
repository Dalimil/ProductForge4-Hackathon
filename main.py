from flask import Flask, render_template, request, redirect
import json
import database

server = Flask(__name__, static_url_path='')

@server.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@server.route('/')
def main():
	return server.send_static_file('index.html')

@server.route('/list')
def list():
	return server.send_static_file('list.html')

@server.route('/admin')
def admin():
	return server.send_static_file('admin.html')

@server.route('/events')
def events():
	interests = request.args.get('interests', '').split(";")
	data = database.getEvents(interests)
	events = []
	for i in data:
		events.append({"Name": i[1], "Location": i[2], "City": i[3], "Description": i[4], "Organiser": i[5], "Time": i[6]})

	return json.dumps(events)

@server.route('/addEvent', methods=["POST"])
def add_event():
	interests = request.form["interests"].split(";")
	ar = []
	for i in interests:
		if(len(i) > 0):
			ar.append(i)

	z = {}
	for i in request.form:
		if(i != "interests"):
			z[i] = request.form[i]

	z["interests"] = ar
	database.addEvent(z)

	return "success - added: "+request.form["name"]

import os
import sqlite3
@server.route('/debug')
def debug():
	#database.addEvent({"name":"Swimming", "city":"Edinburgh", "location":"new swimming pool", "description":"fun event", "organiser":"swimming centre company", "time":"15/30/27/10/2015", "interests":["bowling", "swimming"]})
	sqlite_file = "sqliteFile.db"
	if('OPENSHIFT_DATA_DIR' in os.environ):
		sqlite_file = os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'sqliteFile.db')
	if not os.path.isfile(sqlite_file):
		return "no"
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	c.execute("select * from Events")
	res = c.fetchall()
	#c.execute("CREATE TABLE Events ( ID INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(255), Location VARCHAR(255), City VARCHAR(255), Description VARCHAR(255), Organiser VARCHAR(255), Time VARCHAR(255) );");
	#c.execute("CREATE TABLE Interests ( ID INTEGER PRIMARY KEY AUTOINCREMENT, InterestID VARCHAR(255), EventID VARCHAR(255));")
	conn.commit()
	conn.close()
	return "done"+sqlite_file