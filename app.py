from flask import Flask, render_template, url_for, request, jsonify
# TODO remove once database works
from tempdata import dataFunction
from flask_sqlalchemy import SQLAlchemy
import time

app = Flask(__name__)

# TODO remove once database works
alltasks = dataFunction()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/midtermapp.db'
db = SQLAlchemy(app)

loggedIn = False

# TODO - Export class to py file:
class User(db.Model):
    __tablename__ = "notusers"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(75))
    # TODO add some encryption or something for password
    password = db.Column(db.String(100))
    points = db.Column(db.Integer)
    createdate = db.Column(db.Integer)

    def __init__(self, username, firstname, lastname, password):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.points = 0
        self.createdate = int(time.time())

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def home():
    return render_template('homebase.html', loggedIn=loggedIn)


@app.route('/newtask', methods=['POST'])
def new_task():
    # if request.form['taskButton'] == 'NEW TASK':
        # TODO get next id number from database (probably when db starts up)
        # TODO replace static test id number with next id number
    return render_template('newtask.html', idd=42)


@app.route('/viewtasks', methods=['POST'])
def view_tasks():
    # if request.form['taskButton'] == 'VIEW TASKS':
    return render_template('viewtasks.html', tasks=alltasks)


@app.route('/task/<string:id>/')
def showTasks(id):
    inputvalues = request.get_data()
    return render_template('task.html', id=id)


@app.route('/madeit', methods=['POST'])
def madeTask():
    # TODO test data exchanged with pulled data:
    madeatask = {
        'id': 48,
        'taskname': 'steal candy from baby',
        'descript': '',
        'opened': '87 years',
        'seller': 'Alucard\nLevel 99',
        'fare': '12% of hall',
        'duration': '',
        'status': 'Active'
    }

    formData = request.get_json()

    madeatask = {
        'id': 44,
        'taskname': formData['tasknameInput'],
        'descript': formData['descriptInput'],
        'opened': 'insertdatedatahere',
        'seller': 'insertuserdatahere',
        'fare': formData['fareInput'],
        'duration': formData['durationInput'],
        'status': 'insertstatusdatahere'
    }

    print(request.get_data())
    return render_template('madenewtask.html', task=jsonify(madeatask))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['usernameLogin']
        password = request.form['passwordLogin']
        # TODO check database for credentials
        loggedIn = True
        return render_template('homebase.html', loggedIn=loggedIn)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        username = request.form['usernameSignup']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        password = request.form['passwordSignup']
        # TODO add to database
        loggedIn = True
        return render_template('homebase.html', loggedIn=loggedIn)

if __name__ == '__main__':
    app.run(debug=True)




# references:
    # button redirects - https://stackoverflow.com/questions/19794695/flask-python-buttons
    # tasks table outline - https://datatables.net/examples/basic_init/scroll_y.html
    # some SQLAlchemy setup - https://www.youtube.com/watch?v=PJK950Gp780
    # unix time - http://avilpage.com/2014/11/python-unix-timestamp-utc-and-their.html
