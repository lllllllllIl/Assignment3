from flask import Blueprint, render_template
from .models import events


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    Event = events.query.all()

    return render_template('index.html', Event = events)