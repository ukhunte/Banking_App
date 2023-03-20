
# Function to create account
def account_creation(name, mno, email, dob, acc_type):
    obj = Bank(name, mno, email, dob, acc_type)
    pa = input("Please enter a password : ")
    return obj.id, [pa, obj]

# Bank Class


class Bank:
    min_bal = 1000
    bal = 1000
    name = ''
    accno = 0
    transaction_details = {}
    mno = 0
    email = ''
    dob = 0
    acc_type = ''
    creation_date = 0
    card = []
    id = 0

    def __init__(self, name, mno, email, dob, acc_type):
        self.name = name
        self.mno = mno
        self.email = email
        self.dob = dob
        self.acc_type = acc_type
        self.id = int('91'+mno)

    def deposit(self):
        print('Please enter amount you want to deposit ')
        amount = float(input("Amount : "))
        self.bal += amount
        print(f'Amount added | Current Balance = {self.bal}')

    def curr_bal(self):
        print(f'Current Balance = {self.bal}')

    def withdraw(self):
        amt = int(input("Please Enter Amoutn to withdraw "))
        if self.bal - amt < self.min_bal:
            self.bal -= amt
            print(f'Amount Widthdrawn | Current bal = {self.bal}')
        else:
            print("Less than {self.min_bal} | Cannot withdraw")

    def creation_date(self):
        print(f'Account Created on {self.creation_date}')


# Dictionary to keep track of accounts id and objects
accounts = {}

# driver code
print("1. Do you have Existing account?")
print("2. Do you want to create an account?")
c = int(input("Please enter your choice in integer"))
while True:
    if c == 1:  # if account exists
        print("Enter your details \n")
        id = int(input("Please Neter Your ID"))
        pa = input("Please Enter Your password")
        obj = 0
        if id in accounts:
            if pa == accounts[id][0]:
                obj = accounts[id][1]
            else:
                print("Invalid Details | Exiting")
        break
    elif c == 2:  # new account creation
        print("Enter your details \n")
        name = input("Enter your name : ")
        mno = input("Enter your mobile number : ")
        email = input("Enter your email : ")
        dob = input("Enter your DOB in dd/mm/yyyy")
        acc_type = ''
        print("Choose Account type : ")
        print("1. Savings")
        print("2. Salary Account")
        c1 = int(input("Enter Your Choice"))
        while True:
            if c1 == 1:
                acc_type = 'Savings'
                break
            elif c1 == 2:
                acc_type = 'Salary'
                break
            else:
                print("please Enter correct option")
        k, v = account_creation(name, mno, email, dob, acc_type)
        accounts[k] = v
        print("Account Created")
        break
    else:  # invalid option choosen
        print("Invalid : Please Choose correct Option")
    print("Exited Thank you")
