# print("Welcome to Semmy Bank Plc")
# uname = input("Enter your Username ")
# password = input("Enter a password ")

# users = {"username":uname,"pass" : password}
# # print(users)
# print("Log in")
# count = 1
# def menu():
#     print('''
#     1. Check Account Balance
#     2. Transfer    
#     3. Buy Data
#     5. Buy Airtime
#     6. Confirm cheque
#     7. Request for cheque book
#     8. Speak with a customer service representative.
#     ''')
# trials= 2
# while count <=3:
#     login = input("Enter your username ")
#     pass21 = input("enter password ")
#     if login == users["username"] and pass21 == users["pass"]:
#         menu()
#         break

#     else:
#         if trials == 0:
#             print('Your account has been temporarily locked.\nPlease contact our online respresentatives for necessary enquiries.')
#         else:
#             print(f"Invalid Username or Password.\nYou have {trials} tries left.")    
#     count = count + 1
#     trials = trials - 1

# else:
#     print('Your account has been temporarily locked.\nPlease contact our online respresentatives for necessary enquiries.')




# # New User to register here
# reg_details = {}
# # tries = 3
# print('Welcome to Semmy Bank Plc.\nRegister to get started.')
# fname = input('First Name: ')
# sname = input('Surname Name: ')
# # email = input('Email address: ')
# uname = input('Username: ')
# # pnumber = int(input('Phone Number: '))
# pword = input('Password: ')
# # reg_details['fname'] = fname
# # reg_details['sname'] = sname
# # reg_details['email'] = email
# reg_details['uname'] = uname
# # reg_details['pnumber'] = pnumber
# reg_details['pword'] = pword
# print(reg_details)
# print(f'Welcome onboard {fname} {sname}!\nYou can proceed to login')

# # Existing User to login here!
# print('Already have an account? please login here')
# log_details = {}
# # print(f'Enter {reg_details['uname']} and {reg_details['pword']} to login here')
# uname1 = input('Username: ')
# pword1 = input('Password: ')
# log_details['uname1'] = uname1
# log_details['pword1'] = pword1
# account_balance = 1000000
# log_count = 1
# def menu():
#     print('''
#     1. Check Balance
#     2. Deposit
#     3. Withdrawal/Transfer
#     4. Purchase Data
#     5. Confirm cheque
#     6. Speak with a customer service representative.

#     ''')
#     option = input('Select an option: ')
#     if option == '1':
#         print(f' Your account balance is: {account_balance}')
#     elif option == '2':
#         deposit_amount = float(input('Enter Amount to be deposited: '))
#         account_balance += deposit_amount
#         print(f'New account balance is: {account_balance}')
#     elif option == '3':
#         withdraw_amount = float(input('Enter amount to be withdrawn: '))
#         account_balance -= withdraw_amount
#         print(f'New account balance is: {account_balance}')
#     elif option == '4':
#         data_amount = int(input('Enter data amount to be purchased: '))
#         account_balance -= data_amount
#         print(f'Data purchase was successful.\nYour new account balance is: {account_balance}')
#     elif option == '5':
#         print('Enter details of the cheque leaf to be confirmed below:')
#         cheque_details = {}
#         chq_no = int(input('Enter cheque number: '))
#         issue_date = input('Enter date of issuance: ')
#         ben_name = input('Enter Beneficiary Name: ')
#         amt_on_chq = int(input('Enter Amount: '))
#         cheque_details['chq_no'] = chq_no 
#         cheque_details['issue_date'] = issue_date 
#         cheque_details['ben_name'] = ben_name 
#         cheque_details['amt_on_chq'] = amt_on_chq
#         print(cheque_details)
#         print('Cheque Confirmed')
#     elif option == '6':
#         print('Request to speak with customer service representative')
# # trials = 2
# # while log_count <= 3:
#     if uname1 == reg_details['uname'] and pword1 == reg_details['pword']:
#         print(f'Welcome {fname}!')
        
#         menu()
#     break
# else:
#     if trials == 0:
#             print('Your account has been temporarily locked.\nPlease contact our online respresentatives for necessary enquiries.')

#     else:
#             print(f'Invalid Username or Password.\nYou have {trials} tries left.')
    
#     trials = trials - 1
#     log_count = log_count + 1


        # def Login():
        #     reg()
        #     trials= 2
        #     count = 1
        #     while count <=3:
        #         login = input("Enter your username ")
        #         pass21 = input("enter password ")
        #         if login == users["username"] and pass21 == users["pass"]:
        #             menu()
        #             break
        #         else:
        #             if trials == 0:
        #                 print('Your account has been temporarily locked.\nPlease contact our online respresentatives for necessary enquiries.')
        #             else:
        #                 print(f"Invalid Username or Password.\nYou have {trials} tries left.")    
        #         count = count + 1
        #         trials = trials - 1
        # Login()
  
        # else:
        #     print('Unknown Input')
        # def now():
        #     username = input('Enter username: ')
        #     password = input('Enter password: ')

        #     if username == 'admin' and password == 'root':
        #         print('welcome')
        #     else:
        #         print('Enter Again')
        #     # print(users)
        # now()
       
        # def menu():
        #     print('''
        #     1. Check Account Balance
        #     2. Transfer    
        #     3. Buy Data
        #     5. Buy Airtime
        #     6. Confirm cheque
        #     7. Request for cheque book
        #     8. Speak with a customer service representative.
        #     ''')
        # def Login():
        #     reg()
        #     trials= 2
        #     count = 1
        #     while count <=3:
        #         login = input("Enter your username ")
        #         pass21 = input("enter password ")
        #         if login == users["username"] and pass21 == users["pass"]:
        #             menu()
        #             break
        #         else:
        #             if trials == 0:
        #                 print('Your account has been temporarily locked.\nPlease contact our online respresentatives for necessary enquiries.')
        #             else:
        #                 print(f"Invalid Username or Password.\nYou have {trials} tries left.")    
        #         count = count + 1
        #         trials = trials - 1
        # Login()
  

# account_balance = 1000000
class Bank_app:
    def __init__(self): 
        self.d = {}
        def menu():
            account_balance = 1000000
            print('''
            1. Check Balance
            2. Deposit
            3. Withdrawal/Transfer
            4. Purchase Data
            5. Confirm cheque
            6. Speak with a customer service representative.

            ''')
            option = input('Select an option: ')
            if option == '1':
                print(f' Your account balance is: {account_balance}\nWould you like to perform another operation? Y/N')
                self.response = input('Response: ')
                if self.response.upper() == 'Y':
                    menu()
                elif self.response.upper() == 'N':
                    print(f'Would you like to log out? Y/N')
                    self.repsonse = input('Response: ')
                    if self.response.upper() == 'Y':
                        pass
                    elif self.response.upper() == 'N': 
                        menu()
                    else:
                        print('Invalid Input.\nTry again!\nWould you like to log out? Y/N')
                        print(f'Would you like to log out? Y/N')
                        self.repsonse = input('Response: ')

            elif option == '2':
                deposit_amount = float(input('Enter Amount to be deposited: '))
                account_balance += deposit_amount
                print(f'New account balance is: {account_balance}')
                menu()
                
            elif option == '3':
                
                withdraw_amount = float(input('Enter amount to be withdrawn: '))
                account_balance -= withdraw_amount
                print(f'New account balance is: {account_balance}')
                menu()
            elif option == '4':
                data_amount = int(input('Enter data amount to be purchased: '))
                account_balance -= data_amount
                print(f'Data purchase was successful.\nYour new account balance is: {account_balance}')
                menu()
            elif option == '5':
                print('Enter details of the cheque leaf to be confirmed below:')
                cheque_details = {}
                chq_no = int(input('Enter cheque number: '))
                issue_date = input('Enter date of issuance: ')
                ben_name = input('Enter Beneficiary Name: ')
                amt_on_chq = int(input('Enter Amount: '))
                cheque_details['chq_no'] = chq_no 
                cheque_details['issue_date'] = issue_date 
                cheque_details['ben_name'] = ben_name 
                cheque_details['amt_on_chq'] = amt_on_chq
                print(cheque_details)
                print('Cheque Confirmed')
                menu()
            elif option == '6':
                print('Request to speak with customer service representative')
       
        print("Welcome to Semmy Bank Plc")
        chose = input('Enter 1 to Register or 2 to Login: ')
        if chose == '1':
            def reg(self):
                self.first_name = input('Enter first name: ')
                self.last_name = input('Enter last name: ')
                self.username = input("Enter your Username ")
                self.password = input("Enter a password ")
                self.d['first_name'] = self.first_name
                self.d['last_name'] = self.last_name
                self.d['username'] = self.username
                self.d['password'] = self.password

                print(self.d)
                
                # users = {"username":uname,"pass" : password}
                print(f"Welcome on board {self.first_name}!\nProceed to {self.password} reset.")
                self.password = input('Current Password: ')
                self.new_pass = input('New Password: ')
                self.conf_npass = input('Confirm New Password: ')
                self.d['new_pass'] = self.new_pass
                self.d['conf_npass'] = self.conf_npass
                # print(self.d)
                if self.conf_npass == self.new_pass:
                    print(f'Password change successful!\nProceed to menu to perform your banking operations')
                    menu()
                else:
                    print(f'Password disparity. Try again!')
                    self.password = input('Current Password: ')
                    self.new_pass = input('New Password: ')
                    self.conf_npass = input('Confirm New Password: ')
                    if self.conf_npass == self.new_pass:
                        print(f'Password change successful!\nProceed to menu to perform your banking operations')
                        menu()
                    # else:


                    # print(users_me)
            reg(self)
        elif chose == '2':
            def login(self):
                self.username = input("Enter your Username ")
                self.password = input("Enter a password ")
                self.d['username'] = self.username
                self.d['password'] = self.password
               
                print(self.d)
                print(f'Welcomeback {self.username}!\nProceed to perform your banking operations')
            
            login(self)
            menu()
Bank_app()
# detail.reg
# x.registration
# print()

        
    
