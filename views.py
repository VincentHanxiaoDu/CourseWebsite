from flask import Blueprint, request, render_template, session, redirect, url_for, abort, jsonify
from login_handler import login_required
from jinja2.exceptions import TemplateNotFound
from database_utils import *

# Blueprint obj, register in app.py to add all views to the website
bp = Blueprint('views', __name__, template_folder='templates')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if "username" in session:
            # Already logged in, redirect to index
            return redirect(url_for('views.index'))
        else:
            return render_template('views/login.html')
    elif request.method == 'POST':
        # Authentication
        data = request.form
        type = data.get('logintype')
        if not type:
            return jsonify({'status': 'False', 'reason': 'Need account type'})
        username = data.get('username')
        password = data.get('password')
        if username and password:
            if type == 'student':
                user = getStudent(username, password)
            elif type == 'instructor':
                user = getInstructor(username, password)
            else:
                return jsonify({'status': 'False', 'reason': 'Incorrect login type'})
            if user:
                session['user'] = user
                return jsonify({'status': 'True'})
            else:
                return jsonify({'status': 'False', 'reason': 'Incorrect username or password'})
        else:
            return jsonify({'status': 'False', 'reason': 'Incorrect info'})

@bp.route('/logout')
def logout():
    if 'user' in session.keys():
        session.pop('user')
    return redirect(url_for('views.login'))


@bp.route('/register', methods=['POST'])
def register():
    data = request.form
    username = data.get('username')
    password = data.get('password')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    type = data.get('regtype')

    if username and password and firstname and lastname and type:
        if type == 'student':
            if registerUser('students', username, password, firstname, lastname):
                return jsonify({'status': 'True'})
            else:
                return jsonify({'status': 'False', 'reason': 'Username already exists'})
        elif type == 'instructor':
            if registerUser('instructors', username, password, firstname, lastname):
                return jsonify({'status': 'True'})
            else:
                return jsonify({'status': 'False', 'reason': 'Username already exists'})
        else:
            return jsonify({'status': 'False', 'reason': 'Incorrect login type'})
    else:
        return jsonify({'status': 'False', 'reason': 'Incorrect info'})

@bp.route('/')
@login_required
def index():
    return render_template('index.html')


@bp.route('/calendar')
@login_required
def calendar():
    return render_template('views/calendar.html')


@bp.route('/news')
@login_required
def news():
    return render_template('views/news.html')


@bp.route('/lectures')
@login_required
def lectures():
    return render_template('views/lectures.html')


@bp.route('/labs')
@login_required
def labs():
    return render_template('views/labs.html')

@bp.route('/labs/tutorial<int:index>')
@login_required
def tut(index):
    try:
        return render_template('views/tutorials/tutorial{}.html'.format(index))
    # no such template
    except TemplateNotFound:
        abort(404)

@bp.route('/assignments')
@login_required
def assignments():
    return render_template('views/assignments.html')


@bp.route('/tests')
@login_required
def tests():
    return render_template('views/tests.html')

@bp.route('/resources')
@login_required
def resources():
    return render_template('views/resources.html')
