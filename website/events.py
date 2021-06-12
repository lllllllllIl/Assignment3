from flask import Blueprint, render_template, request, redirect, url_for
from .models import events
from .forms import eventsForm, CommentForm
from . import db

bp = Blueprint('events', __name__, url_prefix='/events')

@bp.route('/<id>')
def show(id):
    event = events.query.filter_by(id=id).first()
    commentForm = CommentForm()
    return render_template('templates/eventDetails.html', event=event, form=commentForm)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    print("Method type: ", request.method)
    form = eventsForm()

    if form.validate_on_submit():
        event = events(name=form.name.data,
                        description=form.description.data,
                        image=form.image.data,
                        currency=form.currency.data)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('events.create'))

    return render_template('templates/eventCreation.html', form=form)



