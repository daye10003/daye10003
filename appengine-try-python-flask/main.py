from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import pusher
app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'alexjennifer'

p = pusher.Pusher(
	app_id = '83084',
	key = '5722854db044eae6e0f1',
	secret = '107b29d50c086f7aa05e'
	)

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def index():
	if 'username' in session:
		return render_template('index.html')
	else:
		return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method=='POST':
		session['username'] = request.form['username']
		p['syg'].trigger('notification',{"username":session['username']})
		return redirect(url_for('index'))
	else:
		return render_template('login.html')

@app.route('/chatting', methods=['GET','POST'])
def chatting():
	if request.method=='POST':
		contents = str(session['username'] + ':' + request.form['text'])
		p['syg'].trigger('chatting', contents)
		return redirect(url_for('chatting.html'))
	else:
		return render_template('chatting.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
