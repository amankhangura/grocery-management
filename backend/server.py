from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import products_dao


app = Flask(__name__)


connection = get_sql_connection()


@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/hi')
def hi():
    return "hi,how are you?"


if __name__ == '__main__':
    print("Starting the python flask server for you")
    app.run(port = 5000)