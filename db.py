import pandas as pd
import sqlalchemy as sqla
import sys
import cx_Oracle

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


con = cx_Oracle.connect(user="U1", password='U1', dsn="localhost/xepdb1")
cursor = con.cursor()
queries = ['''CREATE TABLE account(
    account_id NUMBER(12) NOT NULL,
    account_type VARCHAR2(10),
    min_bal NUMBER(4),
    name VARCHAR2(50),
    mobile_num NUMBER(10),
    email_id VARCHAR2(30),
    balance NUMBER(15),
    account_creation_date DATE,
    account_num NUMBER(10),
    password VARCHAR2(10),
    account_id1 NUMBER NOT NULL
)''',
           '''ALTER TABLE account ADD CONSTRAINT account_pk PRIMARY KEY(account_id)''',
           '''
    CREATE TABLE bank(
    account_id NUMBER(12) NOT NULL,
    bank_addr VARCHAR2(30),
    bank_name VARCHAR2(15),
    account_id1 NUMBER NOT NULL
)''',
           '''ALTER TABLE bank ADD CONSTRAINT bank_pk PRIMARY KEY(account_id)''',
           '''
    CREATE TABLE card(
    account_id NUMBER(12) NOT NULL,
    card_no NUMBER(12),
    exp_date DATE,
    name_on_card VARCHAR2(20),
    cvv NUMBER(3),
    card_type VARCHAR2(8),
    account_account_id NUMBER(12) NOT NULL
)''',
           '''ALTER TABLE card ADD CONSTRAINT card_pk PRIMARY KEY(account_id)''',
           '''
    CREATE TABLE loan(
    account_id NUMBER(12) NOT NULL,
    loan_amount NUMBER(10),
    interest NUMBER(10),
    issue_date DATE,
    account_account_id NUMBER(12) NOT NULL
)''',
           '''ALTER TABLE loan ADD CONSTRAINT loan_pk PRIMARY KEY(account_id)''',
           '''
    CREATE TABLE transaction_details(
    account_id NUMBER(10) NOT NULL,
    amount NUMBER(15),
    transaction_type VARCHAR2(10),
    account_account_id NUMBER(12) NOT NULL
)''',
           '''ALTER TABLE transaction_details ADD CONSTRAINT transaction_details_pk PRIMARY KEY(account_id)
    ADD CONSTRAINT card_account_fk FOREIGN KEY(account_account_id)
    REFERENCES account(account_id)''',
           '''
    ALTER TABLE loan
    ADD CONSTRAINT loan_account_fk FOREIGN KEY(account_account_id)
    REFERENCES account(account_id)''',
           '''
    ALTER TABLE transaction_details
    ADD CONSTRAINT transaction_details_account_fk FOREIGN KEY(account_account_id)
    REFERENCES account(account_id)'''
           ]
print(len(queries))

for i in queries:
    print(i)
    d = cursor.execute(i)
    con.commit()
    print('Done')
