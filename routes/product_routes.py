from flask import Blueprint, request, jsonify
from models import Product, db

product_bp = Blueprint('product', __name__)

@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = [{"id": p.id, "name": p.name, "price": p.price, "stock": p.stock} for p in products]
    return jsonify(result)

@product_bp.route('/', methods=['POST'])
def add_product():
    data = request.get_json()
    product = Product(name=data['name'], price=data['price'], stock=data['stock'])
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"}), 201

@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    data = request.get_json()
    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)
    db.session.commit()
    return jsonify({"message": "Product updated successfully"}), 200

@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}), 200

