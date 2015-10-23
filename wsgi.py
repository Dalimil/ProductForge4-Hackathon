#!/usr/bin/env python
import os

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

from main import server as application

virtenv = os.path.join(os.environ.get('OPENSHIFT_PYTHON_DIR','.'), 'virtenv')

#
# Below for testing only
#
if __name__ == '__main__':
    application.run(port=8080, debug=True)
