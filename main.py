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
	for i in interests:
		events.append({"Name": i, "Location": "Edinburgh"})
	for i in data:
		pass #todo

	return json.dumps(events)

@server.route('/addEvent', methods=["POST"])
def add_event():
	#database.addEvent(request.form)
	return "success - added: "+request.form["name"]

@server.route('/debug')
def debug():
	database.addEvent({"name":"swimming", "city":"Edinburgh", "location":"new swimming pool", "description":"fun event", "organiser":"swimming centre company", "time":"1445686930", "interests":["bowling", "swimming"]})
	return "done"