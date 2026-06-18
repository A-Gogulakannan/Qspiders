class bank:
    bankname='SBI'
    branch='VADA'
    IFSC='SBIN000123'
    def __init__(self,name,account_no,pin,initial_balance,last_transaction):
        self.name=name
        self.__account_no=account_no
        self.__pin=pin
        self.__initial_balance=initial_balance
        self.__last_transaction=last_transaction
        self.transactions=[]
    def __authenticate(self):         
            account_number=int(input("\nENTER THE ACCOUNT NUMBER:"))
            pin_no=int(input("\nENTER THE PIN:"))
            if account_number==self.__account_no and pin_no==self.__pin:
                return True
            else:
                print("\n\n-----AUTHENTICATION FAILED-----\n\n")
                return False
    
    def __generate_receipt(self):
        if self.transactions!=[]:
            for i in (self.transactions):
                print("----->", *i)
        else:
            print("\n-----NO TRANSACTIONS DONE-----\n")

    def __deposit(self,amount):
        self.__initial_balance+=amount
        self.transactions.append(["DEPOSITED $",amount])
        self.__last_transaction=("----->DEPOSITED AMOUNT $",amount)

    def __withdraw(self,amount):
        self.__initial_balance-=amount
        self.transactions.append(["WITHDRAWN $",amount])
        self.__last_transaction=("----->WITHDRAWN AMOUNT $",amount)

    def deposit_money(self):
        while True:
            if self.__authenticate()==True:
                while True:
                    amount=int(input("\nPLEASE ENTER THE AMOUNT TO DEPOSIT:"))
                    if amount>=0:
                        self.__deposit(amount)
                        print("\n-----DEPOSIT SUCCESSFULL-----\n")
                        break
                    else:
                        print("\n-----INVALID AMOUNT-----\n")
                break
            else:
                print("\n-----ENTER DETAILS AGAIN-----\n")
                

    def withdraw_money(self):
        while True:
            if self.__authenticate()==True:
                while True:
                    amount=int(input("\nENTER THE AMOUNT TO WITHDRAW:"))
                    if amount<=self.__initial_balance and amount>=0:
                        self.__withdraw(amount)
                        print("\n-----WITHDRAW SUCCESSFULL-----\n")
                        break
                    else:
                        print("\n-----INVALID AMOUNT-----\n")
                        break
                break
            else:
                print("ENTER DETAILS AGAIN")

    def show_balance(self):
        while True:
            if self.__authenticate()==True:
                print("\n----->ACCOUNT BALANCE   :", self.__initial_balance)
                break
            else:
                print("\n-----ENTER DETAILS AGAIN-----\n")

    def show_details(self):
        while True:
            if self.__authenticate()==True:
                print("\n----->ACCOUNT HOLDER    :",self.name)
                print("----->BANK NAME         :",self.bankname)
                print("----->BRANCH            :",self.branch)
                print("----->IFSC              :",self.IFSC)
                print("----->ACCOUNT NUMBER    :",self.__account_no)
                print("----->ACCOUNT BALANCE   :",self.__initial_balance)
                print("\n----->ALL TRANSACTIONS<-----\n")
                self.__generate_receipt()
                break
            else:
                print("\n-----ENTER DETAILS AGAIN-----\n")

    def lst_transaction(self):
        while True:
            if self.__authenticate()==True:
                print(*self.__last_transaction)
                print()
                break
            else:
                print("\n-----ENTER DETAILS AGAIN-----\n")

account=bank("Gogul",123456,1234,0,'None')

while True:
    print("\n-----WELCOME TO OUR SBI BANK------\n")
    print("1)DEPOSIT\n2)WITHDRAW\n3)SHOW_BALANCE\n4)SHOW_DETAILS\n5)LAST_TRANSACTION\n6)EXIT\n")
    choice=int(input("Enter your choice:"))
    if choice==1:
        account.deposit_money()
    elif choice==2:
        account.withdraw_money()
    elif choice==3:
        account.show_balance()
    elif choice==4:
        account.show_details()
    elif choice==5:
        account.lst_transaction()
    elif choice==6:
        print("\n------THANKS FOR BANKING WITH US------\n")
        break
    else:
        print("\n-----ENTER VALID CHOICE------\n")
