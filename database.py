import sqlite3
import os

sqlite_file = "sqliteFile.db"
if('OPENSHIFT_DATA_DIR' in os.environ):
	sqlite_file = os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'sqliteFile.db')

if not os.path.isfile(sqlite_file):
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	c.execute("CREATE TABLE Events ( ID INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(255), Location VARCHAR(255), City VARCHAR(255), Description VARCHAR(255), Organiser VARCHAR(255), Time INTEGER );");
	c.execute("CREATE TABLE Interests ( ID INTEGER PRIMARY KEY AUTOINCREMENT, InterestID VARCHAR(255), EventID VARCHAR(255));")
	conn.commit()
	conn.close()

def getEvents(ids):
	result = []
	for id in ids:
		if(len(id) > 0):
			eventsWithId = getEventsWithId(id)
			if(len(eventsWithId) > 0):
				result.extend(eventsWithId)

	newlist = sorted(result, key=lambda k: k[1]) #sort by name
	result = []
	if(len(newlist) > 0):
		result.append(newlist[0])
	for i in range(1, len(newlist)):
		if(newlist[i-1][1] != newlist[i][1]): #remove duplicates
			result.append(newlist[i])

	return result

def getEventsWithId(id):
	# select all events that have a given id/tag (interest)
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	c.execute('SELECT * FROM Events, Interests WHERE Events.Name = Interests.InterestID AND Interests.EventID = "{}"'.format(id))
	res = c.fetchall()
	conn.commit()
	conn.close()
	return res

def addEvent(data):
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	c.execute('INSERT INTO Events (Name, Location, City, Description, Organiser, Time) VALUES ("{}", "{}", "{}", "{}", "{}", {})'.format(data["name"], data["location"], data["city"], data["description"], data["organiser"], data["time"]))
	for tag in data["interests"]:
		c.execute('INSERT INTO Interests (InterestID, EventID) VALUES ("{}", "{}")'.format(tag, data["name"]));
	conn.commit()
	conn.close()
