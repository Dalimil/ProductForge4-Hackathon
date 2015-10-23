from flask import Flask, render_template, request, redirect

server = Flask(__name__, static_url_path='')

cookie_name = "userID"

@server.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@server.route('/')
def main():
	return server.send_static_file('index.html')

@server.route('/list', methods=["GET"])
def list():
	interests = request.args.get('interests', '').split(";")
	res = ""
	for i in interests:
		res += i + "<br />"
	return "List of events:<br />" + res