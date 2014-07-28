import os
import sqlite3
import json
import re
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

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

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

def get_db():
	# Opens a new database connection if there is none yet for the
	# current application context.
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
	#Closes the database again at the end of the requestself.
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

@app.route('/')
def show_entries():
	db = get_db()
	cur = db.execute('select title, text from entries order by id desc')
	entries = cur.fetchall()
	return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)
	db = get_db()
	db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
	db.commit()
	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET','POST'])
def login():
	users = []
	error = None 
	notmatch=True
	if request.method=="POST":
		if os.path.isfile('user.txt'):
			info=open('user.txt', 'r')
			data=info.read()
			if not data=="":
				users = json.loads(data)
			info.close()
			for i in users:
				if (request.form['email'] == i["email"]) and (request.form['password'] == i["password"]):
					session['logged_in'] = True
					session['email'] = request.form['email']
					session['admin'] = i['admin']
					flash('You were logged in')
					return redirect(url_for('show_entries'))
					notmatch=False
		if notmatch:
			error='Invalid'
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('email', None)
	session.pop('admin', None)
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	message = None 
	check_admin = None
	if request.method == 'POST':
		if os.path.isfile('user.txt')==False:
			with open('user.txt', "w") as user:
				pass
		# if 'admin' not in request.form:
		# 	check_admin = False
		# if 'admin' in request.form:
		# 	check_admin = True
		check_admin = 'admin' in request.form
		
		if request.form['email']=="":
			message = 'Email is empty.'
		if bool(re.match("^[A-Za-z0-9\._]+@[A-Za-z0-9-]+\.[(com)|(ac.kr)|(net)]*$", request.form['email']))==False:
			message = 'Invalid email.'
		elif request.form['password'] == '':
			message = 'password is empty.'
		elif bool(re.match("^.*(?=.{8,20})(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&+=]).*$", request.form['password']))==False:
			message = 'Invalid password.'
		elif request.form['password_check'] == '':
			message = 'password is empty.'
		elif request.form['password_check'] != request.form['password']:
			message = 'password does not match.'
		else:
			message = 'Sign up successful'
			users = []
			information = {
				"email" : request.form['email'],
				"password" : request.form['password'],
				"admin" : check_admin
			}
			info=open('user.txt', 'r')
			data=info.read()
			if not data=="":
				users = json.loads(data)
			info.close()
			check=True
			for i in users:
					if request.form['email'] == i["email"]:
						message = 'Not available'
						check=False
			if check:
				users.append(information)
				info=open("user.txt", 'w')
				info.write(json.dumps(users))
				info.close()
		
	return render_template('signup.html', message=message)

@app.route('/show_admin')
def show_admin():
	return render_template('show_admin.html')

@app.route('/userpage')
def userpage():
	f = file('user.txt', 'r')
	accounts = []
	text = f.read()
	if text == "" :
		accounts = []
	else :
		accounts = json.loads(text)
	return render_template('userpage.html', accounts = accounts)

@app.route('/email_check', methods= ['POST'])
def email_check():
	info=open('user.txt', 'r')
	users = []
	data=info.read()
	if not data=="":
		users = json.loads(data)
	email = request.form['email']
	result = {}
	for key in users:
		if key['email'] == email:
			result['message'] = "Not available."
	info.close()
	return json.dumps(result)

if __name__ == '__main__':
	init_db()
	app.run()