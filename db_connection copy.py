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
        con = mysql.connector.connect(user='root', password='Brightpoint@12', host='127.0.0.1', database='invoice_automate')
        cursor = con.cursor()
        return con, cursor
    
    '''
    Creating vendor master tables
    '''
    def vendor_master_create():
        # Create Table
        conn, cursor = Db.config()
        cursor.execute('''create table vendor_master (vendor_code int AUTO_INCREMENT, vendor_name varchar(100), 
        vendor_address varchar(500), vendor_address2 varchar(500), vendor_tax_regd_number varchar(50), vendor_phone_number varchar(40), 
        vendor_email_id varchar(100), vendor_website varchar(100), PRIMARY KEY (vendor_code)) ''')

        cursor.execute('''ALTER TABLE vendor_master AUTO_INCREMENT=6000001''')
        conn.commit()

    '''
    Creating item master table
    '''
    def item_master_create():
        # Create Table
        conn, cursor = Db.config()
        cursor.execute('''create table item_master (product_number int AUTO_INCREMENT, item_number varchar(50), 
        product_name varchar(100), product_description varchar(600), unit varchar(50), currency varchar(5), 
        unit_price varchar(20), tax_type varchar(50), tax_percentage varchar(20), PRIMARY KEY (product_number)) ''')
        
        cursor.execute('''ALTER TABLE item_master AUTO_INCREMENT=1000001''')
        conn.commit()

    '''
    Creating invoice data table
    '''
    def invoice_data_create():
        # Create Table
        conn, cursor = Db.config()
        cursor.execute('''create table invoice_data (s_no int AUTO_INCREMENT, invoice_number varchar(50), 
        invoice_date varchar(20), vendor_code int, product_number int, tax_percentage float, 
        quantity1 varchar(50), price1 varchar(50), amount1 varchar(50), 
        quantity2 varchar(50), price2 varchar(50), amount2 varchar(50), 
        quantity3 varchar(50), price3 varchar(50), amount3 varchar(50), 
        quantity4 varchar(50), price4 varchar(50), amount4 varchar(50), 
        quantity5 varchar(50), price5 varchar(50), amount5 varchar(50), 
        quantity6 varchar(50), price6 varchar(50), amount6 varchar(50), 
        quantity7 varchar(50), price7 varchar(50), amount7 varchar(50), 
        quantity8 varchar(50), price8 varchar(50), amount8 varchar(50), 
        quantity9 varchar(50), price9 varchar(50), amount9 varchar(50), 
        quantity10 varchar(50), price10 varchar(50), amount10 varchar(50), PRIMARY KEY (s_no)) ''')
        conn.commit()

    '''
    Inserting vendor master details to the vendor master table
    '''
    def vendor_master_insert(data_frame):
        conn, cursor = Db.config()
        # Insert DataFrame to Table
        for row in data_frame.itertuples():
            res = cursor.execute('''INSERT INTO vendor_master (vendor_name, vendor_address, vendor_address2,
                         vendor_tax_regd_number, vendor_phone_number, vendor_email_id, vendor_website)
                         VALUES (%s,%s,%s,%s,%s,%s,%s)''',
                         (row.vendor_name,
                         row.vendor_address,
                         row.vendor_address2,
                         row.vendor_tax_regd_number,
                         row.vendor_phone_number,
                         row.vendor_email_id,
                         row.vendor_website)) 
        conn.commit()

    '''
    Inserting item master details to the item master table
    '''
    def item_master_insert(data_frame):
        conn, cursor = Db.config()
        # Insert item_master data to Table
        for row in data_frame.itertuples():
                cursor.execute('''INSERT INTO item_master (item_number, product_name, product_description, unit, 
                       currency, unit_price, tax_type, tax_percentage)
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''',
                       (row.item_number,
                       row.product_name,
                       row.product_description,
                       row.unit, 
                       row.currency,
                       row.unit_price,
                       row.tax_type,
                       row.tax_percentage))    
        conn.commit()

    '''
    Inserting invoice data to the invoice data table
    '''
    def invoice_data_insert(data_frame):
        conn, cursor = Db.config()
        # Insert DataFrame to Table
        for row in data_frame.itertuples():
            res = cursor.execute('''INSERT INTO invoice_data (invoice_number, invoice_date, vendor_code, 
            product_number, tax_percentage, quantity1, price1, amount1, 
        quantity2, price2, amount2, quantity3, price3, amount3, quantity4, price4, amount4, 
        quantity5, price5, amount5, quantity6, price6, amount6, quantity7, price7, amount7, 
        quantity8, price8, amount8, quantity9, price9, amount9, quantity10, price10, amount10)
                         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                         (row.invoice_number, 
                          row.invoice_date, 
                          row.vendor_code, 
                          row.product_number, 
                          row.tax_percentage,
                          row.quantity1, 
                          row.price1,  
                          row.amount1, 
                          row.quantity2, 
                          row.price2, 
                          row.amount2, 
                          row.quantity3, 
                          row.price3, 
                          row.amount3,
                          row.quantity4, 
                          row.price4,  
                          row.amount4, 
                          row.quantity5, 
                          row.price5, 
                          row.amount5, 
                          row.quantity6, 
                          row.price6, 
                          row.amount6,
                          row.quantity7, 
                          row.price7,  
                          row.amount7, 
                          row.quantity8, 
                          row.price8, 
                          row.amount8, 
                          row.quantity9, 
                          row.price9, 
                          row.amount9,
                          row.quantity10, 
                          row.price10, 
                          row.amount10))
                                                  
        conn.commit() 

    '''
    Extracting vendor master details from the vendor master table
    '''
    def vendor_master_data():
        conn, cursor = Db.config()
        query= '''SELECT * FROM vendor_master'''
        cursor.execute(query)
        rs = cursor.fetchall()
        return rs
    
    '''
    Extracting item master details from the item master table
    '''
    def item_master_data():
        conn, cursor = Db.config()
        query= '''SELECT * FROM item_master'''
        cursor.execute(query)
        rs = cursor.fetchall()
        return rs
    
    '''
    Extracting invoice details from the invoice data table
    '''
    def invoice_data():
        conn, cursor = Db.config()
        query= '''SELECT * FROM invoice_data'''
        cursor.execute(query)
        rs = cursor.fetchall()
        return rs
    
# Db.vendor_master_create()
# Db.item_master_create()
# Db.invoice_data_create()

