from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('introduce.html')

@app.route('/idea.html')
def hello1():
    """Return a friendly HTTP greeting."""
    return render_template('idea.html')

@app.route('/idea1.html')
def hello2():
    """Return a friendly HTTP greeting."""
    return render_template('idea1.html')


@app.route('/idea2.html')
def hello3():
    """Return a friendly HTTP greeting."""
    return render_template('idea2.html')

@app.route('/idea3.html')
def hello4():
    """Return a friendly HTTP greeting."""
    return render_template('idea3.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
