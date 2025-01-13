from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Order, Product, db

order_bp = Blueprint('order', __name__)

@order_bp.route('/', methods=['POST'])
@jwt_required()
def place_order():
    data = request.get_json()
    user_id = get_jwt_identity()
    product = Product.query.get(data['product_id'])

    if not product or product.stock < data['quantity']:
        return jsonify({"message": "Product unavailable"}), 400

    total_price = product.price * data['quantity']
    order = Order(user_id=user_id, product_id=product.id, quantity=data['quantity'], total_price=total_price)

    product.stock -= data['quantity']
    db.session.add(order)
    db.session.commit()

    return jsonify({"message": "Order placed successfully", "total_price": total_price}), 201

