from flask import Flask, render_template, url_for, request, jsonify

# TODO remove once database works
from tempdata import dataFunction

from flask_sqlalchemy import SQLAlchemy
import time
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import dbcode

dbcode.create_table()

app = Flask(__name__)
# Secret key used for wtforms' login.
app.config['SECRET_KEY'] = 'ImNotGivingASecretToAMachine!'
# Establishes database location.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database.sqlite'
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

loggedIn = False

# # TODO - Export class to py file:
# class User(UserMixin, db.Model):
#     # __tablename__ = "notusers"
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     firstname = db.Column(db.String(50))
#     lastname = db.Column(db.String(75))
#     # TODO add some encryption or something for password
#     password = db.Column(db.String(80))
#     points = db.Column(db.Integer)
#     createdate = db.Column(db.Integer)

    # def __init__(self, username, firstname, lastname, password):
    #     self.username = username
    #     self.firstname = firstname
    #     self.lastname = lastname
    #     self.password = password
    #     self.points = 0
    #     self.createdate = int(time.time())
    #
    # def __repr__(self):
    #     return '<User %r>' % self.username

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=5, max=15)])
    # TODO increase password min once done testing/developing
    password = PasswordField('password', validators=[InputRequired(), Length(min=1, max=80)])

class SignupForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=5, max=15)])
    firstname = StringField('firstname', validators=[InputRequired(), Length(min=2, max=15)])
    lastname = StringField('lastname', validators=[InputRequired(), Length(min=2, max=15)])
    # TODO increase password min once done testing/developing
    password = PasswordField('password', validators=[InputRequired(), Length(min=1, max=80)])


@app.route('/')
def home():
    return render_template('homebase.html', loggedIn=loggedIn)


@app.route('/newtask', methods=['POST'])
def new_task():
    return render_template('newtask.html')


@app.route('/viewtasks', methods=['POST'])
def view_tasks():
    data = dbcode.select_all_db()
    return render_template('viewtasks.html', tasks=data)


@app.route('/task/<string:id>/')
def showTasks(id):
# TODO design and create
    return render_template('task.html', id=id)


@app.route('/madeit', methods=['POST'])
def madeTask():
# TODO move time and other stuff out of methods and add here
    taskname = request.form['tasknameInput']
    descript = request.form['descriptInput']

# TODO switch out with username eventually
    seller = 'Dave'

    fare = request.form['fareInput']
    duration = request.form['durationInput']
    dbcode.add_task_db(taskname, descript, seller, fare, duration)
    madeatask = dbcode.select_taskname_db(taskname)
    return render_template('madenewtask.html', task=madeatask)


@app.route('/soulsold', methods=['GET', 'POST'])
def sellSoul():
    data = request.form.getlist("cbox")
    # dataString = ""
    # for i in data:
    #     dataString += i + ","
    # dataString = dataString[:-1]
    # print(dataString)
# TODO figure out easier way:
    for i in data:
        dbcode.close_task_db(i)
    return render_template('receipt.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        print('login validate passed')
        # user = User.query.filter_by(username=loginform.username.data).first()
        # if user:
        #     if check_password_hash(user.password, loginform.password.data):
        #         login_user(user)
        #         loggedIn = True
        #         return render_template('homebase.html', loggedIn=loggedIn, name=user.username)

    return render_template('login.html', form=loginform)
    # if request.method == 'GET':
    #
    #     return render_template('login.html', form=loginform)
    # elif request.method == 'POST':
    #     username = request.form['usernameLogin']
    #     password = request.form['passwordLogin']
    #     # TODO check database for credentials
    #     loggedIn = True
    #     return render_template('homebase.html', loggedIn=loggedIn)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signupform = SignupForm()
    if signupform.validate_on_submit():
        print('signup validate success')
        # hashed_password = generate_password_hash(signupform.password.data, method='sha256')
        # new_user = User(username=signupform.username.data,
        #                 firstname=signupform.firstname.data,
        #                 lastname=signupform.lastname.data,
        #                 password=hashed_password)
        # db.session.add(new_user)
        # db.session.commit()
        # print("new user created! score!")
        # return render_template('homebase.html', loggedIn=loggedIn, name=new_user.username)
    return render_template('signup.html', form=signupform)
    # if request.method == 'GET':
    #
    #     return render_template('signup.html', form=signupform)
    # elif request.method == 'POST':
    #     username = request.form['usernameSignup']
    #     firstname = request.form['firstname']
    #     lastname = request.form['lastname']
    #     password = request.form['passwordSignup']
    #     # TODO add to database
    #     loggedIn = True
    #     return render_template('homebase.html', loggedIn=loggedIn)

@app.route('/logout')
def logout():
    logout_user()
    return render_template('homebase.html', loggedIn=loggedIn, name='Guest')


if __name__ == '__main__':
    app.run(debug=True)




# references:
    # button redirects - https://stackoverflow.com/questions/19794695/flask-python-buttons
    # tasks table outline - https://datatables.net/examples/basic_init/scroll_y.html
    # some SQLAlchemy setup - https://www.youtube.com/watch?v=PJK950Gp780
    # unix time - http://avilpage.com/2014/11/python-unix-timestamp-utc-and-their.html
    # database setup - https://www.youtube.com/watch?v=xTumGVC90_0
    # database setup - https://www.youtube.com/watch?v=qfGu0fBfNBs
    # amazing login and database setup - https://www.youtube.com/watch?v=8aTnmsDMldY
    # row_factory - https://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query
    # request.form.getlist - https://stackoverflow.com/questions/7996075/iterate-through-checkboxes-in-flask
    #