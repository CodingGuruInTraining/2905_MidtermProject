from flask import Flask, render_template, url_for, request, jsonify
# TODO remove once database works
from tempdata import dataFunction
# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# TODO remove once database works
alltasks = dataFunction()

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)
#
# # TODO - Export class to py file:
# class User(db.Model):
#     __tablename__ = "notusers"
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     firstname = db.Column(db.String(50))
#     lastname = db.Column(db.String(75))
#     points = db.Column(db.Integer)
#     createdate = db.Column(db.DateTime)
#
#     def __repr__(self):
#         return '<User %r>' % self.username

@app.route('/')
def home():
    return render_template('homebase.html')


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
# @app.route('/task/')
# def showTasks2():
#     id = 3
#     return "hi"

if __name__ == '__main__':
    app.run(debug=True)




# references:
    # button redirects - https://stackoverflow.com/questions/19794695/flask-python-buttons
    # tasks table outline - https://datatables.net/examples/basic_init/scroll_y.html