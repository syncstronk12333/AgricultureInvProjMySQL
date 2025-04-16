# IMPORTING MODULES
import pickle

import mysql.connector as sql
from tabulate import tabulate
import csv

# MYSQL CONNECTOR

con = sql.connect(host='localhost', user='root', password='hirtic', database='agri')
if con.is_connected():
    print("\033[1mSuccessfully connected to the Agriculture Inventory System!\033[0m")
    print("")
    cursor = con.cursor()

# MENU

def menu():
    print("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("П                                                                                                                                                                   П")
    print("П                                                                             M E N U                                                                               П")
    print("П                                                                                                                                                                   П")
    print("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    print(" ")
    print("1. User login ")
    print("2. Reset Password")
    print("3. Quit")
    print("")
    while True:
        choice = str(input("Enter your choice \033[1m[NUMBERS ONLY]\033[0m: "))
        if choice == '1':
            exisuser()
            break

        elif choice == '2':
            resetpw()
            break

        elif choice == '3':
            thankyou()
            break

        else:
            print("")
            print("Invalid Input! ")
            print("")
            continue

# LOGIN

def exisuser():
    print(""
          "╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("П                                                                                                                                                                   П")
    print("П                                                                     \033[1m L O G I N  P O R T A L \033[0m                                                                      П")
    print("П                                                                                                                                                                   П")
    print("╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    print("")
    exisname = str(input("\033[1mEnter your username: \033[0m"))
    if exisname == 'Hirtic':
        with open("password.dat", "rb") as f:
            pw_read = pickle.load(f)
        pw = input("Enter your password \033[1m[CASE SENSITIVE]: \033[0m")
        if pw_read == pw:
            print("")
            print("")
            dbmanagenew()

        else:
            print("")
            print("Incorrect Password!")
            print("")
            pw_choice = str(input("\033[1m1) Try again \n2) Reset password \n3) Quit \n \nAnswer: \033[0m"))
            if pw_choice in ['1', 'try again', 'Try again', '1)']:
                exisuser()

            elif pw_choice in ['2', 'reset password', 'Reset password', '2)']:
                resetpw()

            else:
                print("Invalid Input!")
                print("")
                print("Redirecting.....")
                print("")
                exisuser()
    else:
        print("\033[1mInvalid Input!\033[0m")
        print("")
        wrng_name = str(input("Type 1 to retry or 2 to quit: "))
        if wrng_name == '1':
            print("")
            exisuser()

        elif wrng_name == '2':
            print("")
            print("Quitting....")
            thankyou()

        else:
            print("Invalid input!")
            menu()

# RESET PASSWORD

def resetpw():
    print("")
    while True:
        secque = str(input("\033[1mSECURITY QUESTION:\033[0m \nWhat is your favourite animal? "))
        if secque in ['Tiger', 'tiger']:
            print("")
            print("Access granted! ")
            print("")
            while True:
                new_pw = str(input("Enter your new password: "))
                neww_pw = str(input("Confirm your new password: "))
                if new_pw == neww_pw:
                    with open("password.dat", "wb") as f:
                        pickle.dump(new_pw, f)
                    print("")
                    print("Password changed successfully! ")
                    exisuser()
                    break

                else:
                    print("Passwords don't match...")
                    print("Redirecting......")
                    print("")
                    continue

        elif secque not in ['Tiger', 'tiger']:
            print("")
            print("Invalid input!")
            print("")
            wrng_name2 = str(input("Type 1 to retry or 2 to go to menu or 3 to quit: "))
            if wrng_name2 == '1':
                print("")
                resetpw()
                break

            elif wrng_name2 == '2':
                print("Redirecting....")
                menu()
                break

            elif wrng_name2 == '3':
                print("")
                print("Quiting....")
                thankyou()
                break

            else:
                print("Invalid input!")
                continue

# DATABASE MANAGEMENT

def dbmanagenew():
    print("╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("П                                                                                                                                                                    П")
    print("П                                                               A G R I C U L T U R E  I N V E N T O R Y                                                             П                ")
    print("П                                                                                                                                                                    П")
    print("П                                                                              S Y S T E M                                                                           П              ")
    print("П                                                                                                                                                                    П")
    print("╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    print("")
    print("1. Database Management")
    print("2. User options")
    print("3. View Table")
    print("4. Quit")
    print("")
    while True:
        db_choice = str(input("Enter your choice \033[1m[NUMBERS ONLY]\033[0m: "))
        if db_choice == '1':
            print("")
            print("Redirecting.....")
            print("")
            dbmg()
            break

        elif db_choice == '2':
            print("")
            print("Redirecting.....")
            print("")
            menu()
            break

        elif db_choice == '3':
            print("")
            print("Redirecting.....")
            print("")
            table_profit0 = "SELECT * FROM stock"
            cursor.execute(table_profit0)
            result = cursor.fetchall()
            h = ['Name', 'Stock', 'Profit', 'Loss']
            print(tabulate(result, headers=h, tablefmt='psql'))
            print("")
            ftc()
            break

        elif db_choice == '4':
            print("")
            print("Quiting.....")
            thankyou()
            break

        else:
            print("")
            print("Invalid Input!")
            print("Redirecting....")
            print("")
            continue

# THANK YOU

def thankyou():
    print("")
    print("╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("П                                                                                                                                                                    П")
    print("П                                                                        T H A N K  Y O U !                                                                          П         ")
    print("П                                                                                                                                                                    П")
    print("╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    print("System shut down! ")

# CROP DATA MANAGEMENT

def ins_del():
    print("╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("П                                                                                                                                                                    П")
    print("П                                                               C R O P  D A T A  M A N A G E M E N T                                                                П         ")
    print("П                                                                                                                                                                    П")
    print("╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    print("")
    print("1. Add Crops")
    print("2. Update Crop details")
    print("3. Delete crop details")
    print("4. View crops by range")
    print("5. View table")
    print("6. Go back")
    print("7. Quit")
    print("")

    def ins_del_opt1():
        print("Enter the following details:")
        print("")
        while True:
            insdel_name = input("Enter crop name: ")
            cursor.execute("SELECT Name from stock where Name='{}'".format(insdel_name))
            result = cursor.fetchall()
            if len(result) != 0:
                print("")
                print("Crop Exists Already!")
                print("")
                continue

            else:
                insdel_stock = input("Enter stock: ")
                insdel_profit = input("Enter the profit [PRESS ENTER IF LOSS]: ")
                insdel_loss = input("Enter the loss [PRESS ENTER IF PROFIT]: ")
                cursor.execute("INSERT INTO stock(Name, Stock, Profit, Loss) values('{}','{}','{}','{}')".format(insdel_name, insdel_stock, insdel_profit, insdel_loss))
                con.commit()

            if len(insdel_loss) == 0:
                cursor.execute("UPDATE stock set Loss='-' where Name='{}'".format(insdel_name))
                con.commit()

            print("")
            print("Added successfully!")
            ftc2()

    def ins_del_opt2():
        print("")
        update_name = input("Enter the name of the crop to updated: ")
        cursor.execute("select Name from stock where Name='{}'".format(update_name))
        view_result = cursor.fetchall()
        if len(view_result) == 0:
            print("")
            print("Crop does not exist!")
            print("Redirecting.....")
            print("")
            ins_del_opt2()

        else:
            print("")
            print("1. Name")
            print("2. Stock")
            print("3. Profit")
            print("4. Loss")
            update_opt = str(input("Enter the number of the column to be updated: "))
            if update_opt == '1':
                print("")
                name_updated = input("Enter the updated name: ")
                cursor.execute("update stock set Name='{}' where Name='{}'".format(name_updated, update_name))
                con.commit()
                print("")
                print("Successfully updated!")
                ftc2()

            elif update_opt == '2':
                print("")
                stock_updated = input("Enter the updated stock: ")
                cursor.execute("update stock set Stock='{}' where Stock='{}'".format(stock_updated, update_name))
                con.commit()
                print("")
                print("Successfully updated!")
                ftc2()

            elif update_opt == '3':
                print("")
                profit_updated = input("Enter the updated profit in AED: ")
                cursor.execute("update stock set Profit='{}' where Profit='{}'".format(profit_updated, update_name))
                con.commit()
                print("")
                print("Successfully updated!")
                ftc2()

            elif update_opt == '4':
                print("")
                loss_updated = input("Enter the updated loss in AED: ")
                cursor.execute("update stock set Loss='{}' where Loss='{}'".format(loss_updated, update_name))
                print("")
                print("Successfully updated!")
                ftc2()

            else:
                print("")
                print("Invalid Input!")
                ins_del_opt2()

    def ins_del_opt3():
        print("")
        while True:
            delete_name = input("Enter the name of the crop to be deleted: ")
            cursor.execute("select * from stock where Name='{}'".format(delete_name))
            view_result1 = cursor.fetchall()
            if len(view_result1) == 0:
                print("")
                print("Crop does not exist.")
                print("Redirecting.....")
                print("")
                continue

            else:
                cursor.execute("delete from stock where Name='{}'".format(delete_name))
                con.commit()
                print("")
                print("Successfully deleted!")
                ftc2()
                break

    def ins_del_opt4():
        print("")
        print("1. Stock")
        print("2. Profit")
        print("3. Loss")
        print("4. Go back")
        print("")
        while True:
            filter_name = str(input("Enter your choice \033[1m[NUMBERS ONLY]\033[0m: "))
            if filter_name == '1':
                print("")
                print("Enter the range: ")
                while True:
                    filter_stock1 = input("Lower range [INTEGERS ONLY]: ")
                    if str.isdigit(filter_stock1):
                        filter_stock2 = input("Higher range [INTEGERS ONLY]: ")
                        filter2 = str.isdigit(filter_stock2)
                        if str.isdigit(filter_stock2):
                            cursor.execute("SELECT * FROM stock WHERE Stock BETWEEN('{}') and ('{}')".format(filter_stock1, filter_stock2))
                            filter_result = cursor.fetchall()
                            h1 = ['Name', 'Stock', 'Profit', 'Loss']
                            print("")
                            print(tabulate(filter_result, headers = h1, tablefmt = 'psql'))
                            ftc2()
                            break

                        else:
                            print("")
                            print("Invalid Input!")
                            continue

                    else:
                        print("")
                        print("Invalid Input!")
                        ins_del_opt4()
                        break

            elif filter_name == '2':
                print("")
                print("Enter the range:")
                while True:
                    filter_profit1 = input("Lower range [NUMBERS ONLY]: ")
                    if str.isdigit(filter_profit1):
                        filter_profit2 = input("Higher range [NUMBERS ONLY]: ")
                        if str.isdigit(filter_profit2):
                            cursor.execute("SELECT * FROM stock WHERE Profit BETWEEN('{}') and ('{}')".format(filter_profit1, filter_profit2))
                            filter_result1 = cursor.fetchall()
                            h2 = ['Name', 'Stock', 'Profit', 'Loss']
                            print("")
                            print(tabulate(filter_result1, headers = h2, tablefmt = 'psql'))
                            ftc2()
                        else:
                            print("")
                            print("Invalid Input!")
                            continue
                    else:
                        print("")
                        print("Invalid Input!")
                        continue

            elif filter_name == '3':
                print("")
                print("Enter range:")
                while True:
                    filter_loss1 = input("Lower range [INTEGERS ONLY]: ")
                    if str.isdigit(filter_loss1):
                        filter_loss2 = input("Higher range [INTEGERS ONLY]: ")
                        filterrr2 = str.isdigit(filter_loss2)
                        if str.isdigit(filter_loss2):
                            cursor.execute("SELECT * FROM stock WHERE Loss BETWEEN('{}') and ('{}')".format(filter_loss1, filter_loss2))
                            filter_result1 = cursor.fetchall()
                            h3 = ['Name', 'Stock', 'Profit', 'Loss']
                            print("")
                            print(tabulate(filter_result1, headers=h3, tablefmt='psql'))
                            ftc2()

                        else:
                            print("")
                            print("Invalid Input!")
                            continue

                    else:
                        print("")
                        print("Invalid Input!")
                        continue

            elif filter_name == '4':
                print("Redirecting.....")
                print("")
                ins_del()
                break

            else:
                print("")
                print("Invalid Input!")
                continue

    while True:
        insdel_opt = str(input("Enter your desired option [NUMBERS ONLY]: "))
        if insdel_opt == '1':
            ins_del_opt1()
            break

        elif insdel_opt == '2':
            ins_del_opt2()
            break

        elif insdel_opt == '3':
            ins_del_opt3()
            break

        elif insdel_opt == '4':
            ins_del_opt4()
            break

        elif insdel_opt == '5':
            print("")
            table_profit = "SELECT * FROM stock"
            cursor.execute(table_profit)
            result = cursor.fetchall()
            h = ['Name', 'Stock', 'Profit', 'Loss']
            print(tabulate(result, headers = h, tablefmt = 'psql'))
            print("")
            ftc2()
            break

        elif insdel_opt == '6':
            print("")
            print("Redirecting.......")
            print("")
            dbmg()
            break

        elif insdel_opt == '7':
            print("")
            print("Quitting.......")
            print("")
            thankyou()
            break

        else:
            print("")
            print("Invalid Input!")
            continue

# TOOLS MANAGEMENT

def toolmanagement():
    print("")
    print("╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("П                                                                                                                                                                    П")
    print("П                                                                  T O O L S  M A N A G E M E N T                                                                    П")
    print("П                                                                                                                                                                    П")
    print("╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    print("")
    print("1. List of tools")
    print("2. Add tools")
    print("3. Delete tools")
    print("4. Go back")
    print("5. Quit")
    print("")
    while True:
        opt = input("Enter your choice \033[1m[NUMBERS ONLY]\033[0m: ")
        if opt == '1':
            data = []
            f = open('toolsss.csv', 'r', newline='')
            csvreader = csv.reader(f)
            for i in csvreader:
                data.append(i)
            print(tabulate(data, tablefmt='grid'))
            ftc3()

        elif opt == '2':
            n = int(input("How many tools would you like to add [NUMBERS ONLY]? "))
            f = open("toolsss.csv", "a", newline="")
            h = ['name', 'stock', 'quality']
            wok = csv.writer(f)
            for i in range(n):
                print("Add tool", (i+1))
                name = input("Enter the name: ")
                stock = int(input("Enter the quantity: "))
                quality = input("Enter the condition [EXCELLENT/USABLE/BROKEN]: ")
                store = [name,stock,quality]
                wok.writerow(store)
            f.close()
            ftc3()

        elif opt == '3':
            f = open('toolsss.csv','r')
            csvRead = csv.reader(f)
            l = []
            delTool = input("Enter the name of the tool to be deleted: ")
            found = 0
            for row in csvRead:
                if row[0] != str(delTool):
                    l.append(row)

                else:
                    found = 1

            f.close()
            if found == 0:
                print("")
                print("Tool not found!")
                toolmanagement()

            else:
                f = open('toolsss.csv','w+',newline='')
                csvWrite = csv.writer(f)
                csvWrite.writerows(l)
                f.close()
                print("")
                print("Successfully Deleted!")
                print("")
                print("Redirecting......")
                toolmanagement()

        elif opt == '4':
            print("")
            print("Redirecting.....")
            print("")
            dbmg()

        elif opt == '5':
            print("")
            print("Quitting.......")
            print("")
            thankyou()
            break

        else:
            print("")
            print("Invalid Input!")
            print("")
            continue

# INVENTORY OPTIONS

def dbmg():
    print("")
    print("╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("П                                                                                                                                                                    П")
    print("П                                                                I N V E N T O R Y  O P T I O N S                                                                    П         ")
    print("П                                                                                                                                                                    П")
    print("╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    print("")
    print("1. Stock of seeds")
    print("2. List of crops")
    print("3. Profits/Loss")
    print("4. Profitable Crops")
    print("5. Crop data management")
    print("6. Tools management")
    print("7. Go back")
    print("8. Quit")
    print("")
    while True:
        dbmg_choice = str(input("Enter your choice \033[1m[NUMBERS ONLY]\033[0m: "))
        if dbmg_choice == '1':
            print("")
            while True:
                seed = input("Enter the name of the seed: ")
                cursor.execute("SELECT Stock from stock where Name='{}'".format(seed))
                seedcheck = cursor.fetchall()
                if len(seedcheck) == 0:
                    print("")
                    print("Seed not found.")
                    print("Redirecting....")
                    print("")
                    continue

                else:
                    print("")
                    h6 = ['Available Stock']
                    print(tabulate(seedcheck, headers = h6, tablefmt='psql'))
                    print("")
                    ftc()
                    break

        elif dbmg_choice == '2':
            print("")
            name_result = "Select Name from stock"
            cursor.execute(name_result)
            name_crop = cursor.fetchall()
            h5 = ['Name', 'Stock', 'Profit', 'Loss']
            print(tabulate(name_crop, headers = h5, tablefmt = 'psql'))
            print("")
            ftc()
            break

        elif dbmg_choice == '3':
            input_profit()
            break

        elif dbmg_choice == '4':
            print("")
            profit_pandas_table = "SELECT * from stock where Profit>=2000"
            cursor.execute(profit_pandas_table)
            resultt = cursor.fetchall()
            h4 = ['Name', 'Stock', 'Profit', 'Loss']
            print("Crops that are profitable (profit >= 2000) are :")
            print(tabulate(resultt, headers = h4, tablefmt = 'psql'))
            print("")
            ftc()
            break

        elif dbmg_choice == '5':
            print("")
            print("Redirecting......")
            print("")
            ins_del()
            break

        elif dbmg_choice == '6':
            print("")
            print("Redirecting....")
            print("")
            toolmanagement()
            break

        elif dbmg_choice == '7':
            print("")
            print("Redirecting......")
            print("")
            dbmanagenew()

        elif dbmg_choice == '8':
            thankyou()
            break

        else:
            print("")
            print('Invalid Input!')
            print("")
            continue


def input_profit():
    profit_input = str(input("Enter 1 for Profit and 2 for Loss: "))
    if profit_input == '1':
        print("")
        profit_name = input("Enter the name of the seed to view the profit: ")
        cursor.execute("SELECT Profit from stock where Name='{}'".format(profit_name))
        profitcheck = cursor.fetchall()
        if len(profitcheck) == 0:
            print("")
            print("Seed not found!")
            input_profit()

        else:
            print("")
            print("The Profit from", profit_name, "is:", profitcheck, "AED.")
            print("")
            ftc()

    elif profit_input == '2':
        print("")
        loss_name = input("Enter the name of the seed to view the loss: ")
        cursor.execute("SELECT Loss from stock where Name='{}'".format(loss_name))
        losscheck = cursor.fetchall()
        if len(losscheck) == 0:
            print("")
            print("Seed not found!")

        else:
            print("")
            print("The Loss incurred from", loss_name, "is:", losscheck, "AED.")
            print("")
            ftc()

    else:
        print("")
        print("Invalid Input!")
        input_profit()

# CSV CREATION

def createCSV():
    f = open("toolsss.csv", "a",newline='')
    infile = csv.writer(f)
    h = ['name','stock','quality']
    infile.writerow(h)
    f.close()

# GO BACK FUNCTIONS

def ftc():
    while True:
        ftc_input = str(input("Press 1 to go back to inventory options or 2 to quit \033[1m[NUMBERS ONLY]\033[0m: "))
        if ftc_input == '1':
            print("")
            print("Redirecting.....")
            dbmg()
            break

        elif ftc_input == '2':
            print("Redirecting.....")
            print("")
            thankyou()
            break

        else:
            print("Invalid Input!")
            continue

def ftc2():
    print("")
    ftc2_input = str(input("Press 1 to go back to crop database management or 2 to quit \033[1m[NUMBERS ONLY]: "))
    if ftc2_input == '1':
        ins_del()
        print("")

    elif ftc2_input == '2':
        thankyou()

    else:
        print("Invalid Input!")
        ftc2()

def ftc3():
    print("")
    ftc2_input = str(input("Press 1 to go back to tools management or 2 to quit \033[1m[NUMBERS ONLY]: "))
    if ftc2_input == '1':
        toolmanagement()
        print("")

    elif ftc2_input == '2':
        thankyou()

    else:
        print("Invalid Input!")
        ftc3()

menu()
