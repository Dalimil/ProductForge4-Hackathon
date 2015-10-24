import sqlite3
import os

sqlite_file = "sqliteFile.db"
if('OPENSHIFT_DATA_DIR' in os.environ):
	sqlite_file = os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'sqliteFile.db')

if not os.path.isfile(sqlite_file):
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()
	c.execute("CREATE TABLE ....")

	conn.commit()
	conn.close()

def getEvents(ids):
	result = []
	for id in ids:
		if(len(id) > 0):
			eventsWithId = getEventsWithId(id)
			if(len(eventsWithId) > 0):
				result.extend(eventsWithId)

def getEventsWithId(id):
	# select all events that have a given id/tag (interest)
	return []