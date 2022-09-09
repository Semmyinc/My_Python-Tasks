# Temperature conversion
# (0°C × 9/5) + 32 = 32°F
# f = (c * 9/5 ) + 32
# c = (f - 32)* (5/9)
# k = c + 273.15



reg_details = {}
log_details = {}
def question():
    print('Would you like to continue? Y/N')
    ans = input('Response: ')
    if ans.upper() == 'Y':
        menu()
    elif ans.upper() == 'N':
        pass
    else:
        count = 1
        while count <= 3:
            menu()
            break
        else:
            count += 1
            print('Invalid Input\nExit Oga!')


def register():
    print('Enter your details to register below')
    fname = input('Firstname: ')
    sname = input('Surname: ')
    uname = input('Username: ')
    pword = input('Password: ')
    reg_details['fname'] = fname
    reg_details['sname'] = sname
    reg_details['uname'] = uname
    reg_details['pword'] = pword
    print(reg_details)
    print(f'Welcome Onboard {fname}\nProceed to change your default password below')

def pass_change():
    pword = input('Password: ')
    old_pass = input('Current Password: ')
    if old_pass == pword:
        new_pass = input('New Password: ')
        confirm_new_pass = input('Confirm New Password: ')
        if new_pass == confirm_new_pass:
            print('Password change successful\nProceed to menu to perform your desired operation')
        else:
            trial = 1
            while trial <= 3:
                old_pass = input('Current Password: ')
                if old_pass == pword:
                    new_pass = input('New Password: ')
                    confirm_new_pass = input('Confirm New Password: ')
                    if new_pass == confirm_new_pass:
                        print('Password change successful\nProceed to menu to perform your desired operation')
                        break
                    else:
                        trial += 1
                        print('Invalid Password')
                        quit

def login():
    print('Enter your details to login below')
    uname = input('Username: ')
    pword = input('Password: ')
    log_details['uname'] = uname
    log_details['pword'] = pword
    print(log_details)
    print(f'Welcome back {uname}\nProceed to menu to perform your desired operation')

def menu():

    # value = float(input('Enter temperature value:'  ))
    print("""
            1. Celcius to Farenheit
            2. Celsius to Kelvin
            3. Farenheit to Celsius
            4. Farenheit to Kelvin
            5. Kelvin to Celsius
            6. Kelvin to Farenheit
        """)
    operation = input('Enter Operation to be performed:')
    if operation == '1':
        celcius = float(input('Temperature in Celcius: '))
        farenheit = ((celcius * 9/5 ) + 32)
        print(f'Temperature in Farenheit is: {farenheit}')
        question()
        menu()
    elif operation == '2':
        celcius = float(input('Tempearture in Celcius: '))
        kelvin = celcius + 273.15
        print(f'Temperature in Kelvin is: {kelvin}')
        question()
        menu()
    elif operation == '3':
        farenheit = float(input('Temperature in Farenheit: '))
        celcius = ((farenheit - 32)* (5/9))
        print(f'Temperature in Celcius is: {celcius}')
        question()
        menu()
    elif operation == '4':
        farenheit = float(input('Temperature in Farenheit: '))
        kelvin = (((farenheit - 32)* (5/9))+273.15)
        print(f'Temperature in Celcius is: {kelvin}')
        question()
        menu()
    elif operation == '5':
        kelvin = float(input('Temperature in Kelvin: '))
        celcius = kelvin - 273.15
        print(f'Temperature in Celcius is: {celcius}')
        question()
        menu()
    elif operation == '6':
        kelvin = float(input('Temperature in Kelvin: '))
        farenheit = (((kelvin - 273.15) * 9/5) + 32)
        print(f'Temperature in Farenheit is: {farenheit}')
        question()
        menu()
    else:
        print('invalid operation')
        question()
        menu()
                  

print('Welcome!\nEnter 1 to Register or 2 to Login')
op = int(input('Response: '))
if op == '1':
    ''
register()
pass_change()
menu()

# elif op == '2':
#     ''
# login()
# menu()
# 
