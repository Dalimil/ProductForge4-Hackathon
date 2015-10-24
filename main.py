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
		if(i != interests):
			z[i] = request.form[i]

	z["interests"] = ar
	database.addEvent(request.form)

	return "success - added: "+request.form["name"]

@server.route('/debug')
def debug():
	database.addEvent({"name":"Swimming", "city":"Edinburgh", "location":"new swimming pool", "description":"fun event", "organiser":"swimming centre company", "time":"15/30/27/10/2015", "interests":["bowling", "swimming"]})
	return "done"