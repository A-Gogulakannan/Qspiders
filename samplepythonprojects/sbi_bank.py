import random
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

    def authenticate(self):
        while True:       
            pin_no=int(input("\nENTER THE PIN:"))
            if pin_no==self.__pin:
                print("\n\n-----LOG IN SUCCESSFULL-----\n")
                return True
            else:
                print("\n\n-----AUTHENTICATION FAILED-----\n\n")
                print("OPTIONS: \n1)RETRY\n2)BACK TO PREVIOUS MENU")
                a=int(input("ENTER YOUR CHOICE:"))
                if a==2:
                    return False
                else:
                    continue
 
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
                    amount=int(input("\nPLEASE ENTER THE AMOUNT TO DEPOSIT:"))
                    if amount>0:
                        self.__deposit(amount)
                        print("\n-----DEPOSIT SUCCESSFULL-----\n")
                        self.show_balance()
                        break
                    else:
                        print("\n-----INVALID AMOUNT-----\n")
                        self.show_balance()
                        print("OPTIONS: \n1)RETRY DEPOSIT\n2)BACK TO PREVIOUS MENU")
                        a=int(input("ENTER YOUR CHOICE:"))
                        if a==2:
                            break
                        else:
                            continue
                

    def withdraw_money(self):
                while True:
                    amount=int(input("\nENTER THE AMOUNT TO WITHDRAW:"))
                    if amount<=self.__initial_balance and amount>0:
                        self.__withdraw(amount)
                        print("\n-----WITHDRAW SUCCESSFULL-----\n")
                        self.show_balance()
                        break
                    else:
                        print("\n-----INVALID AMOUNT-----\n")
                        self.show_balance()
                        print("OPTIONS: \n1)RETRY WITHDRAW\n2)BACK TO PREVIOUS MENU")
                        a=int(input("ENTER YOUR CHOICE:"))
                        if a==2:
                            break
                        else:
                            continue

    def show_balance(self):
        print("\n----->ACCOUNT BALANCE   :", self.__initial_balance)

    def show_details(self):
                print("\n----->ACCOUNT HOLDER    :",self.name)
                print("----->BANK NAME         :",self.bankname)
                print("----->BRANCH            :",self.branch)
                print("----->IFSC              :",self.IFSC)
                print("----->ACCOUNT NUMBER    :",self.__account_no)
                print("----->ACCOUNT BALANCE   :",self.__initial_balance)
                print("\n----->ALL TRANSACTIONS<-----\n")
                self.__generate_receipt()

    def lst_transaction(self):
        if self.__last_transaction == "NONE":
            print("\nNO TRANSACTIONS YET\n")
        else:
            print(*self.__last_transaction)

    def all_transactions(self):
        if self.transactions == []:
            print("\nNO TRANSACTIONS YET\n")
        else:
            for i in self.transactions:
                print("----->", *i)


accounts={}
name1="Sample account"
account_number1=random.randint(100000,999999)
pin1=1234
initial_balance2=1000
last_transaction2="NONE"
accounts[account_number1]=bank(name1,account_number1,pin1,initial_balance2,last_transaction2)

while True:

    print("\n-----WELCOME TO OUR SBI BANK------\n")
    print("TO ACCESS OUR SAMPLE ACCOUNT:")
    print("\nACCOUNT NUMBER:",account_number1,"  PIN :",pin1)
    print("\n----->MENU<-----")
    print("\n1)CREATE AN ACCOUNT\n2)LOG IN TO EXISTING ACCOUNT\n3)EXIT\n")

    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("\nENTER YOUR BEAUTIFUL NAME:")
        while True:
            account_number=random.randint(100000,999999)
            if account_number not in accounts:
                print("\nYOUR ACCOUNT NUMBER IS :",account_number)
                break
        while True:
            pinnumber=int(input("\nSET FOUR DIGIT PIN FOR YOUR ACCOUNT : "))
            if len(str(pinnumber))==4:
                break
            else:
                print("\n-----ENTER VALID PIN NUMBER-----")
        initial_balance1=0
        last_transaction1="NONE"
        accounts[account_number]=bank(name,account_number,pinnumber,initial_balance1,last_transaction1)
        print("\nACCOUNT CREATED SUCCESSFULLY")
        print("\nPLEASE SAVE YOUR ACCOUNT NUMBER")

    elif choice==2:
        while True:
            acc_no = int(input("\nENTER ACCOUNT NUMBER: "))
            if acc_no in accounts:
                account = accounts[acc_no]
                if account.authenticate():
                    while True:
                        print("\n1)DEPOSIT\n2)WITHDRAW\n3)SHOW_BALANCE\n4)SHOW_DETAILS\n5)ALL_TRANSACTION\n6)LAST_TRANSACTION\n7)BACK TO PREVIOUS MENU\n")
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
                            account.all_transactions()
                        elif choice==6:
                            account.lst_transaction()
                        elif choice==7:
                            break
                        else:
                            print("\n-----ENTER VALID CHOICE------\n")
                    break
            else:
                print("-----ACCOUNT NUMBER NOT FOUND-----")
                print("OPTIONS: \n1)RETRY\n2)BACK TO PREVIOUS MENU")
                a=int(input("ENTER YOUR CHOICE:"))
                if a==2:
                    break
                else:
                    continue
        
    elif choice==3:
        print("\n------THANKS FOR BANKING WITH US------\n")
        break