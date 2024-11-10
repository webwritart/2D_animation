from flask import Blueprint, render_template, request

about = Blueprint('about', __name__, static_folder='static', template_folder='templates')


@about.route('/about', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        subject = request.form.get('subject')
        email = request.form.get('mail')

    return render_template('about.html')
