"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SECRET_KEY'] = "DHFGUSRGHUISHGUISHG"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)
db.create_all()

@app.route('/api/cupcakes')
def get_cupcakes():
    """Returns all cupcakes"""

    cupcakes = Cupcake.query.all()
    serialized_cupcakes = [cupcake.serialize() for cupcake in cupcakes]

    response = {'cupcakes': serialized_cupcakes}

    return (jsonify(response), 200)


@app.route('/api/cupcakes/<cupcake_id>')
def get_cupcake(cupcake_id):
    """Returns a cupcake with the provided id"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized_cupcake = cupcake.serialize()
    response = {'cupcake': serialized_cupcake}

    return (jsonify(response), 200)


@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():
    """Adds a new cupcake"""

    data = request.json

    new_cupcake = Cupcake(flavor=data['flavor'], size=data['size'],
                          rating=data['rating'], image=data['image'])

    db.session.add(new_cupcake)
    db.session.commit()

    response = {'cupcake': new_cupcake.serialize()}

    return (jsonify(response), 201)
