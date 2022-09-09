
# def Menu():
#     print("""
#     1. Data Plans
#     2. XtraValue(Data + Voice)
#     3. Social Bundle 
#     4. Balance Check 
#     """)
    


# ussd = input("Enter a ussd code ")
# if ussd == "*131#":
#     Menu()
#     option = input("Select an option ")
#     if option == 1:
#         print("""
#         1. Daily
#         2. Weekly
#         3. Monthly
#         4. 2-3 Months
#         """)
#     else:
#         Menu()
# else:
#     print("incorrect ussd code")   

def menu():
    print('''
    1. Data Plans
    2. XtraValue(Data + Voice)
    3. Social Bundles
    4. Balance Check
    5. Roaming/Int'l
    6. Borrow Credit/Recharge
    7. Gift Data
    8. Video Pack
    9. Hot Deals
    ''')

def menu1():
     print('''
        Buy Data Plans
        1. Daily
        2. Weekly
        3. Monthly
        4. 2-3 Months
        5. Always on Plans
        6. Broadband Plans
        7. Family Packs
        8. Hot Deals
        9. FREE Youtube
        10.Manage Data
        0. Back
        ''')


ussd = input('Enter code: ')
if ussd == '*131#':
    print('''
    1. Data Plans
    2. XtraValue(Data + Voice)
    3. Social Bundles
    4. Balance Check
    5. Roaming/Int'l
    6. Borrow Credit/Recharge
    7. Gift Data
    8. Video Pack
    9. Hot Deals
    ''')
    option = input('Select an option: ')
    if option == '1':
        print('''
        Buy Data Plans
        1. Daily
        2. Weekly
        3. Monthly
        4. 2-3 Months
        5. Always on Plans
        6. Broadband Plans
        7. Family Packs
        8. Hot Deals
        9. FREE Youtube
        10.Manage Data
        0. Back
        ''')
        option1 = input('Select an option: ')
        if option1 == '1':
            print('''
            1. N50 for 40MB
            2. N100 for 100MB
            3. N100 for 350MB(IG/TIKTOK/YouTube)
            4. N200 for 250MB (2 days)
            5. N300 for 1GB
            6. N500 for 2GB(2 days)
            99.Next
            0. Back           
            ''')
            option2 = input('Select an option: ')
            if option2 == '0':
                menu1()

        elif option1 == '2':
            print('''
            1. N200 for 1GB(IG/TIKTOK/YouTube ONLY)
            2. N300 for N350MB
            3. N500 for 750MB(2-Week plan)
            4. N500 for 750MB+N500 Talktime (Val/14days)
            99.Next
            0. Back
            ''')
            option2 = input('Select an option: ')
            if option2 == '0':
                menu1()
        elif option1 == '3':
            print('''
            1. N1,000 for 1.5GB
            2. N1,200 for 2GB
            3. N1,500 for 3GB
            4. N2,000 for 4.5GB
            5. N2,500 for 6GB
            6. N3,500 for 12GB
            7. N1,000 for 1.5GB+N1,000
            99.Next
            0. Back
            ''')
            option2 = input('Select an option: ')
            if option2 == '0':
                menu1()
        elif option1 == '0':
            menu()
            # print('''
            # 1. Data Plans
            # 2. XtraValue(Data + Voice)
            # 3. Social Bundles
            # 4. Balance Check
            # 5. Roaming/Int'l
            # 6. Borrow Credit/Recharge
            # 7. Gift Data
            # 8. Video Pack
            # 9. Hot Deals
            # ''')
    elif option == '2':
        print('''
        This Plan gives U aitime for Natl & Int'l calls plus data after subscribing to bundle plan.
        1. Xtra Talk
        2. XtraData
        3. Eligible Int'l Destinations
        4. XtraData+
        ''')
    elif option == '3':
        print('''
        1. Whatsapp
        2. Facebook
        3. Instagram
        4. Tiktok
        5. ayoba
        6. All Social Bundles
        7. YouTube, Instagram, and Tiktok
        8. Opera Mini & News
        9. Social Mega bundle
        99. Next
        ''')
    elif option == '4':
        print('''
        Your data balance:
        Monthly: 9.56GB expires 07/09/2022
        Bonus: 3870.37MB expires 07/09/2022 23:59:59
        YouTube Night: 3:56GB expires 28/08/2022
        YouTube
        99. Next
        ''')
else:
    # print('Invalid Code')
    print('''
    Yello! Seems you dialed a wrong code. Please select
    1. Buy Data/Other bundles
    2. Borrow airtime/data
    3. Goodbag Offers
    4. Momo Agents
    5. VAS
    6. Chat Zigi
    ''')
 
