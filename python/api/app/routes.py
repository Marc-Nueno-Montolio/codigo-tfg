import os
from . import create_app
from .models import Stock
from flask import Flask, request, jsonify
from . import db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')



@app.route("/stocks", methods=["GET"])
def get_stocks():
    stocks = Stock.query.all()
    
    res = [] 
    for stock in stocks:
        res.append(stock.to_json())
    return res


@app.route("/stocks/update_position/<id>", methods=["POST", "GET"])
def update_stock_position(id):
    stock = Stock.query.filter_by(id=int(id)).first()
    body = request.json
    position = body['position']
    stock.position = position
    db.session.commit()
    return str(stock)