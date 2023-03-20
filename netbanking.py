accounts = []
print("1. Do you have Existing account?")
print("2. Do you want to create an account?")
c = int(input("Please enter your choice in integer"))
while True:
    if c == 1:
        print("Enter your details \n")
        id = int(input("Please Neter Your ID"))
        pa = input("Please Enter Your password")
        # Bank()
        break
    elif c == 2:
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
        # accounts.append(account_creation())
        print("Account Created")
        break
    else:
        print("Invalid : Please Choose correct Option")
