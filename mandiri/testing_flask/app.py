from flask import Flask, request, jsonify
from models import db, User, Product, Order, OrderItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# create tables
with app.app_context():
    db.create_all()
    
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'name': u.name} for u in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(name=data['name'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created!', 'id': user.id})


@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products])

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = Product(name=data['name'], price=data['price'])
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product added!', 'id': product.id})


@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    user_id = data['user_id']
    items = data['items']  # list of {product_id, quantity}

    order = Order(user_id=user_id)
    db.session.add(order)
    db.session.flush()  # get order.id before commit

    for i in items:
        order_item = OrderItem(order_id=order.id, product_id=i['product_id'], quantity=i['quantity'])
        db.session.add(order_item)

    db.session.commit()
    return jsonify({'message': 'Order created', 'order_id': order.id})


@app.route('/orders/<int:user_id>', methods=['GET'])
def get_user_orders(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    data = []
    for o in orders:
        items = []
        for i in o.order_items:
            items.append({
                'product': i.product.name,
                'quantity': i.quantity,
                'price': i.product.price
            })
        data.append({
            'order_id': o.id,
            'user': o.user.name,
            'items': items
        })
    return jsonify(data)
