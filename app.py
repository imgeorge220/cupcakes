"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request, render_template, redirect
from models import db, connect_db, Cupcake
from forms import CupcakesForm


app = Flask(__name__)
app.config['SECRET_KEY'] = "DHFGUSRGHUISHGUISHG"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)
db.create_all()

@app.route('/')
def root():
    return redirect('/cupcakes')


@app.route('/cupcakes')
def cupcakes():
    form = CupcakesForm()
    return render_template('cupcakes.html', form=form)


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

@app.errorhandler(404)
def page_not_found(e):
    # custom page for 404 error

    return render_template('404.html'), 404

@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():
    """Adds a new cupcake"""

    data = request.json
    data["image"] = data["image"] or None
    new_cupcake = Cupcake(**data)

    db.session.add(new_cupcake)
    db.session.commit()

    response = {'cupcake': new_cupcake.serialize()}

    return (jsonify(response), 201)


@app.route('/api/cupcakes/<cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    """Updates a cupcake"""

    data = request.json

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data['flavor']
    cupcake.size = data['size']
    cupcake.rating = data['rating']
    cupcake.image = data['image']

    db.session.commit()

    response = {'cupcake': cupcake.serialize()}

    return (jsonify(response), 200)


@app.route('/api/cupcakes/<cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """Updates a cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    response = {'message': 'Deleted'}

    return (jsonify(response), 200)