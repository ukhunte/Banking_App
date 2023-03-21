import datetime
import cx_Oracle
import pandas as pd
import sqlalchemy as sqla
import sys


lib_dir = r"C:\instantclient-basic-windows.x64-21.9.0.0.0dbru\instantclient_21_9"
try:
    cx_Oracle.init_oracle_client(lib_dir=lib_dir)
except Exception as err:
    print("Error connecting: cx_Oracle.init_oracle_client()")
    print(err)
    sys.exit(1)

# Test to see if it will print the version of sqlalchemy
print(sqla.__version__)    # this returns 1.2.15 for me

# Test to see if the cx_Oracle is recognized
print(cx_Oracle.version)   # this returns 8.0.1 for me

# This fails for me at this point but will succeed after the solution described below
cx_Oracle.clientversion()


def account_creation(name, mobile_num, email_id, account_type, password):
    account_id = '91'+mobile_num
    min_bal = 1000
    balance = min_bal
    account_creation_date = datetime.datetime.now().strftime("%d-%m-%Y")
    account_num = mobile_num
    account_id1 = account_id
    con = cx_Oracle.connect(user="U1", password='U1', dsn="localhost/xepdb1")
    cursor = con.cursor()
    query = "insert into account values('{}','{}',{},'{}',{},'{}',{},TO_DATE('{}', 'dd-mm-yyyy'),{},'{}','{}')".format(
        account_id, account_type, min_bal, name, mobile_num, email_id, balance, account_creation_date, account_num, password, account_id1)
    print(query)
    d = cursor.execute(query)
    con.commit()


account_creation('test1', '1234567890', 'qwe@qwew.com', 'savings', '12345')
