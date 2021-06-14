from flask import Blueprint, render_template, request, redirect, url_for
from .models import Events, Comments 
from .forms import EventsForm, CommentForm
from . import db

bp = Blueprint('events', __name__, url_prefix='/events')

@bp.route('/<id>')
def show(id):
    event = Events.query.filter_by(id=id).first()
    commentForm = CommentForm()
    return render_template('templates/eventDetails.html', event=event, form=commentForm)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    print("Method type: ", request.method)
    events_form = EventsForm()

    if (events_form.validate_on_submit() == True):
        event = Events(name=events_form.name.data,
                        description=events_form.description.data,
                        image=events_form.image.data,
                        date=events_form.date.data,
                        ticketQty=events_form.ticketQTY.data,
                        status=events_form.status.data)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('events.create'))

    return render_template('templates/eventCreation.html', form=events_form)

def get_event():
    b_desc = """ACDC new up and coming show, for sure to 
                pump you up and get that rock and roll flowing 
                through your bones, be there or be square"""
    image_loc = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFyC8pBJI2AAHLpAVih41_yWx2xxLleTtdshAdk1HOZQd9ZM8-Ag'
    event = Events('ACDC', b_desc, image_loc, '$100')
    comment = Comments("User1", "Seen them 3 times already, best band ever",'2021-12-06 4:00:00')
    event.set_comments(comment)

    return event

