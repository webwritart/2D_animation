from flask import Blueprint, render_template


main = Blueprint('main', __name__, static_folder='static', template_folder='templates')

@main.route('/')
def home():
    col = ['#d9d9d9', 'white']
    bottom_menu = 'y'
    return render_template('animations.html', col=col, bottom_menu=bottom_menu)


@main.route('/character_design')
def character_design():
    col = ['white','#d9d9d9']
    bottom_menu = 'y'
    return render_template('character_design.html', col=col, bottom_menu=bottom_menu)




