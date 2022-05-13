from crypt import methods
from flask import Flask, render_template, request
import werkzeug

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/tikee/<int:tikee_id>', methods=['POST'])
def tikee_page(tikee_id):
    print(request.form['text1'])
    # return render_template('tikee.html', tikee_id=tikee_id)


@app.route('/project/<int:project_id>')
def project_page(project_id):
    return render_template('project.html', project_id=project_id)


@app.route('/enlaps')
def enlaps_page():
    return render_template('enlaps.html')


@app.errorhandler(werkzeug.exceptions.HTTPException)
def bad_request(e):
    return render_template('error.html', e=e)


if __name__ == '__main__':
    app.run(debug=True)