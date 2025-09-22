#Products backend
import sys
print(sys.path)
import pymysql

from sql_connection import get_sql_connection



# def connect():
#     cnx = pymysql.connect(user='root', password='Rabaab@0505',
#                               host='127.0.0.1',
#                               database='gs')
#     print("connected")
#     return cnx

# def close(cnx):
#     cnx.close()
#     print("closed")


def get_all_products(connection):
    cursor = connection.cursor()
    # In this query we have joined the products and uom tables and retrieved the product_id, name, uom_id, price_per_unit and uom_name
    query = ("select products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)

    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            "product_id": product_id,
            "name": name,
            "uom_id": uom_id,
            "price_per_unit": price_per_unit,
            "uom_name": uom_name
            
        })
    #cursor.close()
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("insert into products(name, uom_id, price_per_unit) values (%s, %s, %s)")
    cursor.execute(query, (product['name'], product['uom_id'], product['price_per_unit'])) 
    connection.commit()
    return cursor.lastrowid


def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid

# ---------main function----------
if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))
   # print(insert_new_product(connection, {"name": "Dantmanjan", "uom_id": 1, "price_per_unit": 10}))
   # print(get_all_products(connection))
    #print(delete_product(connection, 12))
   
    
    







# def get_all_products(cnx):
#     cursor = cnx.cursor()
#     cursor.execute("SELECT * FROM gs.products")
#     rows = cursor.fetchall()
#     cursor.close()
#     return rows

# def main():
#     cnx = connect()
#     rows = get_all_products(cnx)
#     for row in rows:
#         print(row)
#     close(cnx)
#     my_test_function()

# if __name__ == '__main__':
#     main()
