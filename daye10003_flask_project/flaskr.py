import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort,
	render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'flaskr.db'),
	DEBUG=True,
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
def connect_db():
	rv=sqlite3.connect(app.config['DATABASE'])
	rv.row_factory=sqlite3.Row
	return rv
if __name__ == '__main__':
	app.run()

def get_db():
    # Opens a new database connection if there is none yet for the
    # current application context.
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    #Closes the database again at the end of the request.
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()