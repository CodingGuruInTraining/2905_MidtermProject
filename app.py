from flask import Flask, render_template, url_for, request
# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
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
@app.route('/viewtasks', methods=['POST'])
def task():
    if request.form['taskButton'] == 'NEW TASK':
        return render_template('newtask.html')
    elif request.form['taskButton'] == 'VIEW TASKS':
        return render_template('viewtasks.html')

@app.route('/task/<string:id>/')
def showTasks(id):
    return render_template('task.html', id = id)

if __name__ == '__main__':
    app.run(debug=True)




# references:
    # button redirects - https://stackoverflow.com/questions/19794695/flask-python-buttons
