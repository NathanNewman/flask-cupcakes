"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from form import CupcakeForm
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','postgresql:///cupcakes')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'Secret!')

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/', methods=["GET", "POST"])
def homepage():
    form = CupcakeForm()
    if form.validate_on_submit():
        cupcake = Cupcake()
        cupcake.submit_cupcake(form)
        return redirect('/')
    else:
        return render_template('/index.html', form=form)

@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    cupcake = Cupcake.query.get(id)
    form = CupcakeForm(obj=cupcake)
    if form.validate_on_submit():
        cupcake = Cupcake()
        cupcake.edit_cupcake(id, form)
        return redirect(f"/edit/{id}")
    else:
        return render_template("/edit.html", form=form, cupcake=cupcake)

# ------------------------------ API Routes --------------------------------------------------------
@app.route('/api/cupcakes')
def list_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    new_cupcake = Cupcake(
        flavor=request.json['flavor'],
        size=request.json['size'],
        rating=request.json['rating'],
        image=request.json['image']
    )
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='deleted')
