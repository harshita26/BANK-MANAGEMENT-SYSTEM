import os, platform
import mysql.connector

# conn=mysql.connector.connect(host='localhost',username='root',password='')
# mycur=conn.cursor()
# query='CREATE DATABASE bank'
# mycur.execute(query)
conn=mysql.connector.connect(host='localhost',username='root',password='',database='bms')
mycur=conn.cursor()
mycur.execute("CREATE TABLE IF NOT EXISTS bank (user_name VARCHAR(20),user_account VARCHAR(20) NOT NULL PRIMARY KEY,user_money INT(20),account_type VARCHAR(20))")
conn.commit()
mycur.close()
conn.close()

class Account:
    def __init__(self,user_name,user_account,user_money,account_type):
        print('''\n\n********BANK MANAGEMENT SYSTEM********* \n''')
        self.user_name=user_name
        self.user_account=user_account
        self.user_money=user_money
        self.account_type=account_type
 
    def new(self):
        print("\n*************WELCOME TO BANK***********")
        self.user_account=input("ENTER THE ACCOUNT NUMBER: ")
        self.user_name=input("ENTER THE ACCOUNT HOLDER NAME: ")
        self.account_type=input("ENTER THE TYPE OF ACCOUNT [CURRENT(C) / SAVING(S)]: ")
        if self.account_type.lower()=='c' or self.account_type.lower()=='s':
            try:
                self.user_money=int(input("ENTER THE INITIAL AMOUNT (>=500 FOR SAVING AND >=1000 FOR CURRENT: "))
            except:
                print("*********INVALID INPUT**********")
            else:
                conn=mysql.connector.connect(host='localhost',username='root',password='',database='bms')
                mycur=conn.cursor()
                query="INSERT INTO bank (user_name,user_account,user_money,account_type) VALUES (%s,%s,%s,%s)"
                value=(self.user_name,self.user_account,self.user_money,self.account_type)
                mycur.execute(query,value)
                conn.commit()
                mycur.close()
                conn.close()
                print("\n ACCOUNT CREATED")
        else:
            print("ENTER ONLY C OR S") 

    def deposit(self):
        account_no=input("ENTER THE ACCOUNT NUMBER: ")
        query="SELECT * FROM bank where user_account=%s"
        val=(account_no,)
        try:
            conn=mysql.connector.connect(host='localhost',username='root',password='',database='bms')
            mycur=conn.cursor()
            mycur.execute(query,val)
            print(mycur.fetchone())
            if mycur.rowcount>0:
                try:
                    deposit=int(input("ENTER THE AMOUNT TO DEPOSIT: "))
                except:
                    print("*********INVALID INPUT**********")
                else:
                    quer="UPDATE bank SET user_money= user_money+%s where user_account=%s"
                    value=(deposit,account_no)
                    mycur.execute(quer,value)
                    print("MONEY IS DEPOSIT IN YOUR ACCOUNT")
            else:
                print("THIS ACCOUNT IS NOT PRESENT")
        except Exception as er:
            print(er)
        finally:
            conn.commit()
            mycur.close()
            conn.close()            

    def withdraw(self):
        account_no=input("ENTER THE ACCOUNT NUMBER: ")
        query="SELECT * FROM bank where user_account=%s"
        val=(account_no,)
        try:
            conn=mysql.connector.connect(host='localhost',username='root',password='',database='bms')
            mycur=conn.cursor()
            mycur.execute(query,val)
            print(mycur.fetchone())
            if mycur.rowcount>0:
                try:
                    withdraw=int(input("ENTER THE AMOUNT TO WITHDRAW: "))
                except:
                    print("*********INVALID INPUT**********")
                else:
                    quer="UPDATE bank SET user_money= user_money-%s where user_account=%s"
                    value=(withdraw,account_no)
                    mycur.execute(quer,value)
                    print("MONEY IS WITHDRAW IN YOUR ACCOUNT")
            else:
                print("THIS ACCOUNT IS NOT PRESENT")
        except Exception as er:
            print(er)
        finally:
            conn.commit()
            mycur.close()
            conn.close()
             
    def balance(self):
        account_no=input("ENTER THE ACCOUNT NUMBER: ")
        query="SELECT user_money FROM bank where user_account=%s"
        val=(account_no,)
        try:
            conn=mysql.connector.connect(host='localhost',username='root',password='',database='bms')
            mycur=conn.cursor()
            mycur.execute(query,val)
            print(mycur.fetchone())
        except Exception as er:
            print(er)
        finally:
            conn.commit()
            mycur.close()
            conn.close()

    def show(self):
        print("ALL USERS")
        conn=mysql.connector.connect(host='localhost',username='root',password='',database='bms')
        mycur=conn.cursor()
        mycur.execute("SELECT * FROM bank")
        for row in mycur:
            print("ACCOUNT NUMBER: ",row[1])
            print("ACCOUNT HOLDER NAME: ",row[0])
            print("TYPE OF ACCOUNT: ",row[3])
            print("AMOUNT: ",row[2])
        conn.commit()
        mycur.close()
        conn.close()
        
    def remove(self):
        account_no=input("ENTER THE ACCOUNT NUMBER: ")
        query="SELECT * FROM bank where user_account=%s"
        val=(account_no,)
        try:
            conn=mysql.connector.connect(host='localhost',username='root',password='',database='bms')
            mycur=conn.cursor()
            mycur.execute(query,val)
            print(mycur.fetchone())
            if mycur.rowcount>0:
                query="DELETE FROM bank where user_account=%s"
                val=(account_no,)
                conn=mysql.connector.connect(host='localhost',username='root',password='',database='bms')
                mycur=conn.cursor()
                mycur.execute(query,val)
            else:
                print("THIS ACCOUNT IS NOT PRESENT")
        except Exception as er:
            print(er)
        finally:
            print("YOUR ACCOUNT IS DELETED")
            conn.commit()
            mycur.close()
            conn.close()
        
            
    def modify(self):
        account_no=input("ENTER THE ACCOUNT NUMBER: ")
        query="SELECT * FROM bank where user_account=%s"
        val=(account_no,)
        try:
            conn=mysql.connector.connect(host='localhost',username='root',password='',database='bms')
            mycur=conn.cursor()
            mycur.execute(query,val)
            print(mycur.fetchone())
            if mycur.rowcount>0:
                account_name=input("ENTER THE ACCOUNT HOLDER NAME: ")
                account_typ=input("ENTER THE TYPE OF ACCOUNT [CURRENT(C) / SAVING(S)]: ")
                if account_typ.lower()=='c' or account_typ=='s':
                    try:
                        amount=int(input("ENTER THE AMOUNT: "))
                    except:
                        print("*********INVALID INPUT**********")
                    else:
                        quer="UPDATE bank SET user_money=%s,user_name=%s,account_type=%s where user_account=%s"
                        value=(amount,account_name,account_typ,account_no)
                        mycur.execute(quer,value)
                        print("\n ACCOUNT MODIFY")  
                else:
                    print("PLEASE ENTER ONLY C FOR CURRENT AND S FOR SAVING")                  
            else:
                print("THIS ACCOUNT IS NOT PRESENT")
        except Exception as er:
            print(er)
        finally:
            conn.commit()
            mycur.close()
            conn.close()
           
def main():
    account = Account('','',0,'')
    while True:
        print('''\nMAIN MENU
	1. NEW ACCOUNT
	2. DEPOSIT AMOUNT
	3. WITHDRAW AMOUNT
	4. BALANCE ENQUIRY
	5. ALL ACCOUNT HOLDER LIST
	6. CLOSE AN ACCOUNT
	7. MODIFY AN ACCOUNT
	8. EXIT''')
        choice=input("SELECT YOUR OPTION (1-8): ")
        if choice=='1':
            account.new()
        elif choice=='2':
            account.deposit()
        elif choice=='3':
            account.withdraw()
        elif choice=='4':
            account.balance()
        elif choice=='5':
            account.show()
        elif choice=='6':
            account.remove()
        elif choice=='7':
            account.modify()
        elif choice=='8':
            exit('THANK YOU!')
        else:
            print('*********INVALID OPTION**********')
        input('Enter the key to clear the screen: ')
        if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
            print(os.system('cls'))
        else:
            print(os.system('clear'))

main() 