from flask import Flask
app = Flask(__name__)
from create_tables import (
    create_collection_table,
    create_sales_table
)

@app.route('/')
@app.route('/index')
def index():
    return 'Hello test!'


@app.route('/create_collection_table')
def collection_table():
    msg = create_collection_table()
    return msg


@app.route('/create_sales_table')
def sales_table():
    msg = create_sales_table()
    return msg