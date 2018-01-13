from flask import Blueprint

front = Blueprint('front',__name__)

@front.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html',courses=courses)
