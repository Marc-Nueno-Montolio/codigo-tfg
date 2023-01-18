import os
from . import create_app
from .models import Stock
from flask import Flask, request, jsonify, redirect
from . import db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
@app.errorhandler(404)
def page_not_found(e):
    return "Error 404: The resource requested was not found"

# List all stocks
@app.route("/", methods=["GET"])
@app.route("/stocks/", methods=["GET"])
def list_stocks():
    stocks = Stock.query.all()
    print(stocks)
    res = [] 
    for stock in stocks:
        res.append(stock.to_json())
    return res

# Retrieve stock info by id
@app.route("/stocks/<id>", methods=["GET"])
def get_stock(id):
    stock = Stock.query.filter_by(id=id).first()
    if stock is not None:
        return stock.to_json()
    else:
        return redirect('/404')


# Create new stock
@app.route("/stocks/create", methods=["POST"])
def create_stock():
    body = request.json
    stock = Stock(body['content'], body['position'])
    db.session.add(stock)
    db.session.commit()
    return stock.to_json()

@app.route("/stocks/delete/<id>", methods=["POST"])
def delete_stock(id):
    stock = Stock.query.filter_by(id=int(id)).first()
    db.session.delete(stock)
    db.session.commit()
    return stock.to_json()

# Update stock position
@app.route("/stocks/update_position/<id>", methods=["POST", "GET"])
def update_stock_position(id):
    stock = Stock.query.filter_by(id=int(id)).first()
    body = request.json
    stock.position = body['position']
    db.sesion.add(stock)
    db.session.commit()
    return stock.to_json()