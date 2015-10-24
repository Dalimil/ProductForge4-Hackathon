import sqlite3
import os

sqlite_file = "sqliteFile.db"
if('OPENSHIFT_DATA_DIR' in os.environ):
	sqlite_file = os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'sqliteFile.db')

if not os.path.isfile(sqlite_file):
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	c.execute("CREATE TABLE Events ( ID INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(255), Location VARCHAR(255), City VARCHAR(255), Description VARCHAR(255), Organiser VARCHAR(255), Time INTEGER );");
	c.execute("CREATE TABLE Interests ( ID INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(255) );")
	c.execute("CREATE TABLE Matching ( ID INTEGER PRIMARY KEY AUTOINCREMENT, InterestID INTEGER, EventID INTEGER ); ")
	conn.commit()
	conn.close()

def getEvents(ids):
	result = []
	for id in ids:
		if(len(id) > 0):
			eventsWithId = getEventsWithId(id)
			if(len(eventsWithId) > 0):
				result.extend(eventsWithId)
	return result

def getEventsWithId(id):
	# select all events that have a given id/tag (interest)
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	#c.execute("SELECT * FROM")
	res = c.fetchall()
	conn.commit()
	conn.close()
	return []

def addEvent(data):
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	c.execute('INSERT INTO Events (Name, Location, City, Description, Organiser, Time) VALUES ("{}", "{}", "{}", "{}", "{}", {})'.format(data["name"], data["location"], data["city"], data["description"], data["organiser"], data["time"]))
	for tag in data["interests"]:
		c.execute('INSERT INTO Matching (InterestID, EventID) VALUES ("{}", "{}")'.format(3, 5);
	conn.commit()
	conn.close()
