# username = input('Your username ')
# Email = input('your email ')
# password = input('choose a suitable password ')
# fullname = input('what is your fullname? ')

f = open("staff.txt",'w')
staffDetails = str("1." )+str("Tara, Taradebby@gmail.com, Taradee, Omotara Kuds \n")
f.write(staffDetails)

f = open("staff.txt",'a')
staffDetails2 = str("2. " )+str("korede, korede419@gmail.com, smarter, Korede Ibukunoluwa")
f.write(staffDetails2)
f.close()

f = open("customer.txt", "w")

print("Welcome to the SN Banking App \n ")
Login = input("To LOGIN type-> login" + "\n" +"To CLOSE type-> close \n")
# print("To CLOSE type-> close \n")
action = True

while action:
    if Login == "login":
     username =input("Username: ")
     password =input("Password: ")

     checkIn = input("To CREATE NEW BANK ACCOUNT type-> new" + "\n" + "To CHECK ACCOUNT BALANCE type-> balance \n"+"To LOGOUT type-> logout \n")
     activity = True

    while activity:
        if checkIn == "new":
            account_name = input("Account Name: ")
            account_balance = input("Account Balance: ")
            account_type = input("Account Type: ")
            account_email = input("Account email: ")
            account_number = input("Account Number: ")


            f=open("customer.txt", "a")
            f.write(account_number)
            f.close()

        elif checkIn == "balance":
            account_number = input("What is your Account Number: ")
            f = open("customer.txt", "r")
            print(f.read())

        elif checkIn == "logout":
            print("lets go again")
            breakpoint()




    if Login == "close":
        print("Thank you for using this app.")
        break
