from flask import Flask, jsonify, request, make_response
import flask
import decimal
import psycopg2
from app.response_parse import response_parse


app = Flask(__name__)


#Json decimal encoder
class MyJSONEncoder(flask.json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return str(obj)
        return super(MyJSONEncoder, self).default(obj)
app.json_encoder = MyJSONEncoder

@app.route("/customerOrderAnalysis", methods=["GET", "POST"])
def orderSummarize():
    if request.method == "GET":
        return "UP"
    elif request.method == "POST":
        response_list = []
        request_info = request.json
        customerId = request_info["customerId"]

        connection = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' port='5432' password='****'")
        cursor = connection.cursor()

        sql = """select o.order_id ,concat(c.first_name, ' ', c.last_name) as name ,email, phone_number,
        order_item_count, order_price, order_price_tax, order_price_currency, order_city, order_transaction_type 
        from orders o left outer join customer c on o.customer_id=c.customer_id 
        where o.customer_id ={} and 
        coalesce(order_update_date,order_create_date) <= current_date;""".format(customerId)
        cursor.execute(sql)
        sql_result = cursor.fetchall()
        for row in sql_result:
            response_list.append(response_parse(row))
        return make_response(jsonify(response_list))
