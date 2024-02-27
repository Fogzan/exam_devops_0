from flask import Flask, render_template, request, flash
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from models import Inf, Tickets, create_models

# Создание БД
# create_models(app)

@app.route('/')
def index():
    films = Inf.query.all()
    return render_template('index.html', films = films) 

@app.route('/ticket', methods=['GET', 'POST'])
def ticket():
    ticket = {}
    film = {}
    ticket_id = None
    if request.method == 'POST':
        ticket_id = request.form.get('ticketInput')
        ticket = Tickets.query.get(ticket_id)
        if not ticket:
            flash('Билета с таким id не существует.', 'danger')
            return render_template('tickets.html', ticket = ticket, ticket_id=ticket_id, film = film) 
        else:
            flash('Билет успешно найден.', 'success')
        film = Inf.query.filter(Inf.title == ticket.title).one()
        if not film:
            flash('Ошибка в заполнении БД.', 'danger')
            
    return render_template('tickets.html', ticket = ticket, ticket_id = ticket_id, film = film) 
