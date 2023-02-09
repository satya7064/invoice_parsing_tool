import mysql.connector
import pandas as pd
import pyodbc
from cryptography.fernet import Fernet


key = Fernet.generate_key()
fernet = Fernet(key)

'''
Creating tables in the database
'''

class Db:

    '''
    Connecting to the database
    '''
    def config():
        con = mysql.connector.connect(user='root', password='Brightpoint@12', host='127.0.0.1', database='invoice_parsing')
        cursor = con.cursor()
        return con, cursor
    
    '''
    Creating seller tables
    '''
    def seller_table_create():
        # Create Table
        conn, cursor = Db.config()
        cursor.execute('''create table seller_table (seller_name varchar(100), seller_address varchar(500), 
        seller_phone_num varchar(50), seller_mailid varchar(100)) ''')

        # cursor.execute('''ALTER TABLE vendor_master AUTO_INCREMENT=6000001''')
        conn.commit()

    '''
    Creating customer tables
    '''
    def customer_table_create():
        # Create Table
        conn, cursor = Db.config()
        cursor.execute('''create table customer_table (customer_name varchar(200), customer_address varchar(500), 
        customer_phone_num varchar(50), customer_mailid varchar(100), customer_tax_id_num varchar(100)) ''')
        
        # cursor.execute('''ALTER TABLE item_master AUTO_INCREMENT=1000001''')
        conn.commit()

    '''
    Creating product tables
    '''
    def product_table_create():
        # Create Table
        conn, cursor = Db.config()
        cursor.execute('''create table product_table (invoice_number varchar(100), invoice_date varchar(30), tax_percentage varchar(50), 
        product_description1 varchar(1000), quantity1 varchar(100), net_price1 varchar(50), amount1 varchar(100), 
        product_description2 varchar(1000), quantity2 varchar(100), net_price2 varchar(50), amount2 varchar(100), 
        product_description3 varchar(1000), quantity3 varchar(100), net_price3 varchar(50), amount3 varchar(100), 
        product_description4 varchar(1000), quantity4 varchar(100), net_price4 varchar(50), amount4 varchar(100), 
        product_description5 varchar(1000), quantity5 varchar(100), net_price5 varchar(50), amount5 varchar(100), 
        product_description6 varchar(1000), quantity6 varchar(100), net_price6 varchar(50), amount6 varchar(100), 
        product_description7 varchar(1000), quantity7 varchar(100), net_price7 varchar(50), amount7 varchar(100), 
        product_description8 varchar(1000), quantity8 varchar(100), net_price8 varchar(50), amount8 varchar(100), 
        product_description9 varchar(1000), quantity9 varchar(100), net_price9 varchar(50), amount9 varchar(100), 
        product_description10 varchar(1000), quantity10 varchar(100), net_price10 varchar(50), amount10 varchar(100), 
        gross_total varchar(50)) ''')
        conn.commit()

    '''
    Inserting seller details to the seller table
    '''
    def seller_table_insert(data_frame):
        conn, cursor = Db.config()
        # Insert DataFrame to Table
        for row in data_frame.itertuples():
            res = cursor.execute('''INSERT INTO seller_table (seller_name, seller_address, seller_phone_num, 
            seller_mailid)
                         VALUES (%s,%s,%s,%s)''',
                         (row.seller_name, 
                         row.seller_address, 
                         row.seller_phone_num, 
                         row.seller_mailid)) 
        conn.commit()

    '''
    Inserting customer details to the customer table
    '''
    def customer_table_insert(data_frame):
        conn, cursor = Db.config()
        # Insert item_master data to Table
        for row in data_frame.itertuples():
                cursor.execute('''INSERT INTO customer_table (customer_name, customer_address, customer_phone_num, 
                customer_mailid, customer_tax_id_num)
                       VALUES (%s,%s,%s,%s,%s)''',
                       (row.customer_name, 
                       row.customer_address, 
                       row.customer_phone_num, 
                       row.customer_mailid, 
                       row.customer_tax_id_num))    
        conn.commit()

    '''
    Inserting product details to the product table
    '''
    def product_table_insert(data_frame):
        conn, cursor = Db.config()
        # Insert DataFrame to Table
        for row in data_frame.itertuples():
            res = cursor.execute('''INSERT INTO product_table (invoice_number, invoice_date, tax_percentage, 
            product_description1, quantity1, net_price1, amount1, 
            product_description2, quantity2, net_price2, amount2, 
            product_description3, quantity3, net_price3, amount3, 
            product_description4, quantity4, net_price4, amount4, 
            product_description5, quantity5, net_price5, amount5,
            product_description6, quantity6, net_price6, amount6, 
            product_description7, quantity7, net_price7, amount7, 
            product_description8, quantity8, net_price8, amount8, 
            product_description9, quantity9, net_price9, amount9, 
            product_description10, quantity10, net_price10, amount10, gross_total)
                         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                         %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                         (row.invoice_number, 
                         row.invoice_date, 
                         row.tax_percentage,  
                         row.product_description1, 
                         row.quantity1, 
                         row.net_price1, 
                         row.amount1, 
                         row.product_description2, 
                         row.quantity2, 
                         row.net_price2, 
                         row.amount2, 
                         row.product_description3, 
                         row.quantity3, 
                         row.net_price3, 
                         row.amount3, 
                         row.product_description4, 
                         row.quantity4, 
                         row.net_price4, 
                         row.amount4, 
                         row.product_description5, 
                         row.quantity5, 
                         row.net_price5, 
                         row.amount5, 
                         row.product_description6, 
                         row.quantity6, 
                         row.net_price6, 
                         row.amount6, 
                         row.product_description7, 
                         row.quantity7, 
                         row.net_price7, 
                         row.amount7, 
                         row.product_description8, 
                         row.quantity8, 
                         row.net_price8, 
                         row.amount8, 
                         row.product_description9, 
                         row.quantity9, 
                         row.net_price9, 
                         row.amount9, 
                         row.product_description10, 
                         row.quantity10, 
                         row.net_price10, 
                         row.amount10, 
                         row.gross_total))
                                                  
        conn.commit() 

    '''
    Extracting seller details from the seller table
    '''
    def seller_table_data():
        conn, cursor = Db.config()
        query= '''SELECT * FROM seller_table'''
        cursor.execute(query)
        rs = cursor.fetchall()
        return rs
    
    '''
    Extracting customer details from the customer table
    '''
    def customer_table_data():
        conn, cursor = Db.config()
        query= '''SELECT * FROM customer_table'''
        cursor.execute(query)
        rs = cursor.fetchall()
        return rs
    
    '''
    Extracting product details from the product table
    '''
    def product_table_data():
        conn, cursor = Db.config()
        query= '''SELECT * FROM product_table'''
        cursor.execute(query)
        rs = cursor.fetchall()
        return rs
    
# Db.seller_table_create()
# Db.customer_table_create()
# Db.product_table_create()

