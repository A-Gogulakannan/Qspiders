class bank:
    bankname='SBI'
    branch='VADA'
    IFSC='SBIN000123'
    def __init__(self,name,age,dob,acc_no,pin,initial_balance,mobile_no,address):
        self.name=name
        self.age=age
        self.dob=dob
        self.__acc_no=acc_no
        self.__pin=pin
        self.__initial_balance=initial_balance
        self.mobile_no=mobile_no
        self.address=address

    def show_customer_details(self):
        account_no=int(input("Enter account_no:"))
        pin_no=int(input("Enter pin:"))
        if account_no == self.__acc_no and pin_no==self.__pin:
            print("Bank name:",self.bankname)
            print("Branch:",self.branch)
            print("Account holder name:",self.name)
            print("age:",self.age)
            print("date of birth:",self.dob)
            print("Mobile number:",self.mobile_no)
            print("Address:",self.address)
            print("Account_number:",self.__acc_no)
            print("Balance:",self.__initial_balance)
        else:
            print("Authentication Failed")


    def __deposit(self,amount):
        self.__initial_balance+=amount
    def deposit_money(self):
        account_no=int(input("Enter account_no:"))
        pin_no=int(input("Enter pin:"))
        if account_no == self.__acc_no and pin_no==self.__pin:
            amount=int(input("Enter amount to deposit:"))
            if amount>=0:
                self.__deposit(amount)
                print("Deposited the money successfully")
            else:
                print("invalid amount")
        else:
            print("Authentication failed")

    def __withdraw(self,amount):
        self.__initial_balance-=amount
    def withdraw_money(self):
        account_no=int(input("Enter account_no:"))
        pin_no=int(input("Enter pin:"))
        if account_no == self.__acc_no and pin_no==self.__pin:
            amount=int(input("Enter amount to deposit:"))
            if amount<=self.__initial_balance and amount>=0:
                self.__withdraw(amount)
                print("Withdrawed the money successfully")
            else:
                print("invalid amount")
        else:
            print("Authentication failed")

    def show_balance(self):
        print("Account holder name:",self.name)
        print("Account number:",self.__acc_no)
        print("Account balance:",self.__initial_balance)

account=None
while True:
    print(" WELCOME TO OUR BANK ")
    print("1)Create account 2)Account details 3)Deposit money 4)Withdraw money 5)Bank balance 6)Exit")
    choice=int(input("Enter the option number:"))
    if choice==1:
        name=input("Enter name:")
        age=int(input("Enter age:"))
        dob=input("Date of birth:")
        accountnumber=int(input("Account_number:"))
        pin=int(input("Set pin:"))
        mobilenumber=int(input("Enter mobile number:"))
        address=input("Enter address:")
        balance=0
        account=bank(name,age,dob,accountnumber,pin,balance,mobilenumber,address)

    elif choice in [2,3,4,5,6]:
        if account is None:
            print("Please create an account")
            continue
        if choice ==2:
            account.show_customer_details()
        elif choice==3:
            account.deposit_money()
        elif choice==4:
            account.withdraw_money()
        elif choice==5:
            account.show_balance()
        elif choice==6:
            break 
    else:
        print("Invalid option")
