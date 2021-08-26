import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
import cloudinary
import cloudinary.uploader
# location = "C:\\Users\\jchno\\PycharmProjects\\final-project\\my_db.db"


app = Flask(__name__)
CORS(app)


# creating a register table using my database
def register_tb():

    with sqlite3.connect('my_db.db') as connect:

        connect.execute('CREATE TABLE IF NOT EXISTS users (userid INTEGER PRIMARY KEY AUTOINCREMENT,'
                        'name TEXT NOT NULL,'
                        'username TEXT NOT NULL,'
                        'password TEXT NOT NULL, '
                        'email TEXT NOT NULL)')
        print("Users table was created successfully")


register_tb()


# creating products using my database
def product_tb():

    with sqlite3.connect('my_db.db') as connect:

        connect.execute('CREATE TABLE IF NOT EXISTS items(product_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                        'product_num TEXT NOT NULL,' 
                        'product_cat TEXT NOT NULL,'
                        'product_name TEXT NOT NULL,'
                        'product_desc TEXT NOT NULL, '
                        'product_price TEXT NOT NULL, '
                        'product_image TEXT NOT NULL)')
        print("Products table was created successfully")


product_tb()


def sale_tb():

    with sqlite3.connect('my_db.db') as connect:

        connect.execute('CREATE TABLE IF NOT EXISTS sale(sale_pro_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                        'sale_pro_num TEXT NOT NULL,'
                        'sale_pro_cat TEXT NOT NULL,'
                        'sale_pro_name TEXT NOT NULL,'
                        'sale_pro_desc TEXT NOT NULL, '
                        'sale_pro_price TEXT NOT NULL, '
                        "was_price TEXT NOT NULL,"
                        'sale_pro_image TEXT NOT NULL)')
        print("For Sale Products table was created successfully")


sale_tb()


def trend_tb():
    with sqlite3.connect('my_db.db') as connect:

        connect.execute('CREATE TABLE IF NOT EXISTS trend(trend_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                        'trend_num TEXT NOT NULL,'
                        'trend_cat TEXT NOT NULL,'
                        'trend_name TEXT NOT NULL,'
                        'trend_desc TEXT NOT NULL, '
                        'trend_price TEXT NOT NULL, '
                        'trend_image TEXT NOT NULL)')
        print("Trending Products table was created successfully")


trend_tb()


# Returns the data in a dict
def dict_factory(cursor, row):
    d = {}
    for i, x in enumerate(cursor.description):
        d[x[0]] = row[i]
    return d


# this code allows you to view the products
@app.route('/view-product/', methods=['GET'])
def view_product():
    products = []
    try:

        with sqlite3.connect('my_db.db') as connect:
            connect.row_factory = dict_factory
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM items")
            products = cursor.fetchall()

    except Exception as e:
        connect.rollback()
        print("There was an error fetching results from the database: " + str(e))

    finally:
        return jsonify(products)


# this code allows you to view the products that are on sale
@app.route('/view-sale/', methods=['GET'])
def view_sale_product():
    products = []
    try:

        with sqlite3.connect('my_db.db') as connect:
            connect.row_factory = dict_factory
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM sale")
            products = cursor.fetchall()

    except Exception as e:
        connect.rollback()
        print("There was an error fetching results from the database: " + str(e))

    finally:
        connect.close()
        return jsonify(products)


# this code allows you to view the number 1 product that is trending
@app.route('/view-trend/', methods=['GET'])
def view_trends():
    trend = []
    try:

        with sqlite3.connect('my_db.db') as connect:
            connect.row_factory = dict_factory
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM trend where trend_id= 1")
            trend = cursor.fetchall()

    except Exception as e:
        connect.rollback()
        print("There was an error fetching results from the database: " + str(e))

    finally:
        connect.close()
        return jsonify(trend)


# this code allows you to see the 2nd trending shoe in the trending section
@app.route('/view-trends/', methods=['GET'])
def view_trend():
    trend = []
    try:

        with sqlite3.connect('my_db.db') as connect:
            connect.row_factory = dict_factory
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM trend where trend_id = 3")
            trend = cursor.fetchall()

    except Exception as e:
        connect.rollback()
        print("There was an error fetching results from the database: " + str(e))

    finally:
        connect.close()
        return jsonify(trend)


# this code allows you to see the 3rd trending shoe in the trending section
@app.route('/view-trends3/', methods=['GET'])
def view_trend3():
    trend = []
    try:

        with sqlite3.connect('my_db.db') as connect:
            connect.row_factory = dict_factory
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM trend where trend_id = 5")
            trend = cursor.fetchall()

    except Exception as e:
        connect.rollback()
        print("There was an error fetching results from the database: " + str(e))

    finally:
        connect.close()
        return jsonify(trend)


# this code allows you to see the 4th trending shoe in the trending section
@app.route('/view-trends4/', methods=['GET'])
def view_trend4():
    trend = []
    try:

        with sqlite3.connect('my_db.db') as connect:
            connect.row_factory = dict_factory
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM trend where trend_id = 6")
            trend = cursor.fetchall()

    except Exception as e:
        connect.rollback()
        print("There was an error fetching results from the database: " + str(e))

    finally:
        connect.close()
        return jsonify(trend)


# this code allows you to see the all trending shoes in the trending section
@app.route('/view-trending/', methods=['GET'])
def view_trending():
    trend = []
    try:

        with sqlite3.connect('my_db.db') as connect:
            connect.row_factory = dict_factory
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM trend")
            trend = cursor.fetchall()

    except Exception as e:
        connect.rollback()
        print("There was an error fetching results from the database: " + str(e))

    finally:
        connect.close()
        return jsonify(trend)

# admin controls to create/add a product
@app.route('/add-product/', methods=["POST"])
# @jwt_required()
def add_product():
    response = {}

    if request.method == "POST":
        pro_num = request.json['product_num']
        pro_cat = request.json['product_cat']
        pro_nm = request.json['product_name']
        pro_desc = request.json['product_desc']
        pro_price = request.json['product_price']
        pro_img = request.json['product_image']

        cloudinary.config(
            cloud_name="final-project1",
            api_key="733853268843835",
            api_secret="iD-Rwj51sziP0V8ux1JCCFc7U24"
        )
        upload_result = None
        app.logger.info('%s file_to_upload', pro_img)
        if pro_img:
            upload_result = cloudinary.uploader.upload(pro_img)  # Upload results
            app.logger.info(upload_result)

        with sqlite3.connect('my_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO items("
                           "product_num,"
                           "product_cat,"
                           "product_name,"
                           "product_desc,"
                           "product_price,"
                           "product_image) VALUES(?, ?, ?, ?, ?, ?)",
                           (pro_num, pro_cat, pro_nm, pro_desc, pro_price, upload_result['url']))
            conn.commit()
            response['hurray!'] = "product successfully created"

        return response


# admin controls to create/add a product
@app.route('/add-sale/', methods=["POST"])
# @jwt_required()
def sale_product():
    response = {}
    # try:

    if request.method == "POST":
        sale_num = request.json['sale_pro_num']
        sale_cat = request.json['sale_pro_cat']
        sale_nm = request.json['sale_pro_name']
        sale_desc = request.json['sale_pro_desc']
        sale_price = request.json['sale_pro_price']
        sale_was = request.json['was_price']
        sale_img = request.json['sale_pro_image']

        cloudinary.config(
            cloud_name="final-project1",
            api_key="733853268843835",
            api_secret="iD-Rwj51sziP0V8ux1JCCFc7U24"
        )
        upload_result = None
        app.logger.info('%s file_to_upload', sale_img)
        if sale_img:
            upload_result = cloudinary.uploader.upload(sale_img)  # Upload results
            app.logger.info(upload_result)

        with sqlite3.connect('my_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO sale("
                           "sale_pro_num,"
                           "sale_pro_cat,"
                           "sale_pro_name,"
                           "sale_pro_desc,"
                           "sale_pro_price,"
                           "was_price,"
                           "sale_pro_image) VALUES(?, ?, ?, ?, ?, ?, ?)",
                           (sale_num, sale_cat, sale_nm, sale_desc, sale_price, sale_was, upload_result['url']))
            conn.commit()
            response['hurray!'] = "product on sale was successfully created"

        return response

    # except Exception as e:
    #     conn.rollback()
    #     response["msg"] = "Error occurred when adding a product in the database: " + str(e)

    # finally:
    #     conn.close()
    #     return jsonify(response)


# admin controls to add to trending products
@app.route('/add-trend/', methods=["POST"])
# @jwt_required()
def trend_add():
    res = {}

    if request.method == "POST":
        tr_num = request.json['trend_num']
        tr_cat = request.json['trend_cat']
        tr_nm = request.json['trend_name']
        tr_desc = request.json['trend_desc']
        tr_price = request.json['trend_price']
        tr_img = request.json['trend_image']

        cloudinary.config(
            cloud_name="final-project1",
            api_key="733853268843835",
            api_secret="iD-Rwj51sziP0V8ux1JCCFc7U24"
        )
        upload_result = None
        app.logger.info('%s file_to_upload', tr_img)
        if tr_img:
            upload_result = cloudinary.uploader.upload(tr_img)  # Upload results
            app.logger.info(upload_result)

        with sqlite3.connect('my_db.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO trend("
                           "trend_num,"
                           "trend_cat,"
                           "trend_name,"
                           "trend_desc,"
                           "trend_price,"
                           "trend_image) VALUES(?, ?, ?, ?, ?, ?)",
                           (tr_num, tr_cat, tr_nm, tr_desc, tr_price, upload_result['url']))
            conn.commit()
            res['hurray!'] = "trending product successfully created"

        return res


# this code allows admins to delete products using its id
@app.route('/delete-product/<int:product_id>/')
# @jwt_required()
def delete_product(product_id):
    response = {}

    try:

        with sqlite3.connect('my_db.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM items WHERE product_id=" + str(product_id))
            con.commit()
            response["msg"] = "A record was deleted successfully from the database."

    except Exception as e:
        con.rollback()
        response["msg"] = "Error occurred when deleting a product in the database: " + str(e)

    finally:
        con.close()
        return jsonify(response)


# this code allows admins to delete products on sale using its id
@app.route('/delete-onsale/<int:sale_pro_id>/')
# @jwt_required()
def delete_sale(sale_pro_id):
    response = {}

    try:

        with sqlite3.connect('my_db.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM sale WHERE sale_pro_id=" + str(sale_pro_id))
            con.commit()
            response["msg"] = "A record was deleted successfully from the database."

    except Exception as e:
        con.rollback()
        response["msg"] = "Error occurred when deleting a product in the database: " + str(e)

    finally:
        con.close()
        return jsonify(response)


# this code allows admins to delete products in the trending section
@app.route('/delete-trend/<int:trend_id>')
# jwt required()
def delete_trend(trend_id):
    response = {}

    try:

        with sqlite3.connect('my_db.db') as con:
            cur = con.cursor()
            cur.execute("DELETE FROM trend WHERE trend_id=" + str(trend_id))
            con.commit()
            response["msg"] = "A record was deleted successfully from the database."

    except Exception as e:
        con.rollback()
        response["msg"] = "Error occurred when deleting a product in the database: " + str(e)

    finally:
        con.close()
        return jsonify(response)


# this code allows admins to edit elements in the product
@app.route('/update/<int:product_id>', methods=["PUT"])
# @jwt_required()
def updating_products(product_id):
    response = {}
    try:

        if request.method == "PUT":

            with sqlite3.connect('my_db.db') as conn:
                print(request.json)
                incoming_data = dict(request.json)
                put_data = {}

               # editing name of the product
                if incoming_data.get("product_name") is not None:
                    put_data["product_name"] = incoming_data.get("product_name")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE items SET product_name =? WHERE product_id=?",
                                       (put_data["product_name"], product_id))
                        conn.commit()
                        response['message'] = "Update was successfully updated"
                # editing the price of the product
                if incoming_data.get("product_price") is not None:
                    put_data["product_price"] = incoming_data.get("product_price")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE items SET product_price =? WHERE product_id=?",
                                       (put_data["product_price"], product_id))
                        conn.commit()
                        response['message'] = "Update was successfully"

                # editing the products category
                if incoming_data.get("product_cat") is not None:
                    put_data["product_cat"] = incoming_data.get("product_cat")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE items SET product_cat =? WHERE product_id=?",
                                       (put_data["product_cat"], product_id))
                        conn.commit()
                        response['message'] = "Update was successfully"

                # editing the description of the product
                if incoming_data.get("product_desc") is not None:
                    put_data["product_desc"] = incoming_data.get("product_desc")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE items SET product_desc =? WHERE product_id=?",
                                       (put_data["product_desc"], product_id))
                        conn.commit()
                        response['message'] = "Update was successfully"

                # editing the product number
                if incoming_data.get("product_num") is not None:
                    put_data["product_num"] = incoming_data.get("product_num")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE items SET product_num =? WHERE product_id=?",
                                       (put_data["product_num"], product_id))
                        conn.commit()
                        response['message'] = "Update was successfully"

                # editing the products image
                if incoming_data.get("product_image") is not None:
                    put_data["product_image"] = incoming_data.get("product_image")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE items SET product_image =? WHERE product_id=?",
                                        (put_data["product_image"], product_id))
                        conn.commit()
                        response['message'] = "picture was updated successfully"

    except Exception as e:
        conn.rollback()
        response["msg"] = "Error occurred when updating a product in the database: " + str(e)

    finally:
        conn.close()
        return jsonify(response)


# this code allows admins to edit elements in the products that are on sale
@app.route('/update-sale/<int:sale_pro_id>', methods=["PUT"])
# @jwt_required()
def updating_sales(sale_pro_id):
    response = {}
    try:

        if request.method == "PUT":

            with sqlite3.connect('my_db.db') as conn:
                print(request.json)
                incoming_data = dict(request.json)
                put_data = {}

                # editing name of the product
                if incoming_data.get("sale_pro_name") is not None:
                    put_data["sale_pro_name"] = incoming_data.get("sale_pro_name")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE sale SET sale_pro_name =? WHERE sale_pro_id=?",
                                       (put_data["sale_pro_name"], sale_pro_id))
                        conn.commit()
                        response['message'] = "Update was successfully updated"

                # editing the price of the product
                if incoming_data.get("sale_pro_price") is not None:
                    put_data["sale_pro_price"] = incoming_data.get("sale_pro_price")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE sale SET sale_pro_price =? WHERE sale_pro_id=?",
                                       (put_data["sale_pro_price"], sale_pro_id))
                        conn.commit()
                        response['message'] = "Update was successfully"

                # editing the products category
                if incoming_data.get("sale_pro_cat") is not None:
                    put_data["sale_pro_cat"] = incoming_data.get("sale_pro_cat")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE sale SET sale_pro_cat =? WHERE sale_pro_id=?",
                                       (put_data["sale_pro_cat"], sale_pro_id))
                        conn.commit()
                        response['message'] = "Update was successfully"

                # editing the description of the product
                if incoming_data.get("sale_pro_desc") is not None:
                    put_data["sale_pro_desc"] = incoming_data.get("sale_pro_desc")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE sale SET sale_pro_desc =? WHERE sale_pro_id=?",
                                       (put_data["sale_pro_desc"], sale_pro_id))
                        conn.commit()
                        response['message'] = "Update was successfully"

                # editing the product number
                if incoming_data.get("sale_pro_num") is not None:
                    put_data["sale_pro_num"] = incoming_data.get("sale_pro_num")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE sale SET sale_pro_num =? WHERE sale_pro_id=?",
                                       (put_data["sale_pro_num"], sale_pro_id))
                        conn.commit()
                        response['message'] = "Update was successfully"

                # editing the products image
                if incoming_data.get("sale_pro_image") is not None:
                    put_data["sale_pro_image"] = incoming_data.get("sale_pro_image")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE sale SET sale_pro_image =? WHERE sale_pro_id=?",
                                       (put_data["sale_pro_image"], sale_pro_id))
                        conn.commit()
                        response['message'] = "picture was updated successfully"

                # editing the price of the products before sale
                if incoming_data.get("was_price") is not None:
                    put_data["was_price"] = incoming_data.get("was_price")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE sale SET was_price =? WHERE sale_pro_id=?",
                                       (put_data["was_price"], sale_pro_id))
                        conn.commit()
                        response['message'] = "Update was successfully"

    except Exception as e:
        conn.rollback()
        response["msg"] = "Error occurred when updating a product in the database: " + str(e)

    finally:
        conn.close()
        return jsonify(response)


# this code allows admins to edit elements in the products that are on sale
@app.route('/update-trend/<int:trend_id>', methods=["PUT"])
# @jwt_required()
def update_trend(trend_id):
    response = {}
    try:

        if request.method == "PUT":

            with sqlite3.connect('my_db.db') as conn:
                print(request.json)
                incoming_data = dict(request.json)
                put_data = {}

                # editing name of the product
                if incoming_data.get("trend_name") is not None:
                    put_data["trend_name"] = incoming_data.get("trend_name")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE trend SET trend_name =? WHERE trend_id=?",
                                       (put_data["trend_name"], trend_id))
                        conn.commit()
                        response['message'] = "Update was successful"

                # editing the price of the product
                if incoming_data.get("trend_price") is not None:
                    put_data["trend_price"] = incoming_data.get("trend_price")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE trend SET trend_price =? WHERE trend_id=?",
                                       (put_data["trend_price"], trend_id))
                        conn.commit()
                        response['message'] = "Update was successful"

                # editing the products category
                if incoming_data.get("trend_cat") is not None:
                    put_data["trend_cat"] = incoming_data.get("trend_cat")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE trend SET trend_cat =? WHERE trend_id=?",
                                       (put_data["trend_cat"], trend_id))
                        conn.commit()
                        response['message'] = "Update was successful"

                # editing the description of the product
                if incoming_data.get("trend_desc") is not None:
                    put_data["trend_desc"] = incoming_data.get("trend_desc")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE trend SET trend_desc =? WHERE trend_id=?",
                                       (put_data["trend_desc"], trend_id))
                        conn.commit()
                        response['message'] = "Update was successful"

                # editing the product number
                if incoming_data.get("trend_num") is not None:
                    put_data["trend_num"] = incoming_data.get("trend_num")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE trend SET trend_num =? WHERE trend_id=?",
                                       (put_data["trend_num"], trend_id))
                        conn.commit()
                        response['message'] = "Update was successfully"

                # editing the products image
                if incoming_data.get("trend_image") is not None:
                    put_data["trend_image"] = incoming_data.get("trend_image")

                    with sqlite3.connect('my_db.db') as connection:
                        cursor = connection.cursor()
                        cursor.execute("UPDATE trend SET trend_image =? WHERE trend_id=?",
                                       (put_data["trend_image"], trend_id))
                        conn.commit()
                        response['message'] = "picture was updated successfully"

    except Exception as e:
        conn.rollback()
        response["msg"] = "Error occurred when updating a product in the database: " + str(e)

    finally:
        conn.close()
        return jsonify(response)


if __name__ == "__main__":
    app.debug = True
    app.run(port=5001)

