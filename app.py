from flask import Flask, render_template, url_for, request

app = Flask(__name__)


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

if __name__ == '__main__':
    app.run(debug=True)




# references:
    # button redirects - https://stackoverflow.com/questions/19794695/flask-python-buttons
