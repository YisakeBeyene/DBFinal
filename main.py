def LoginPage():
    print(""" Welcome to the Trendy Game:
                1)Login
                2)Sign Up
                3)Quit
    """)
    userInput=input("Enter Option")
    if userInput='1':
        Login()
    elif userInput='2':
        NewAccount()
    elif userInput='3':
        closeGame()
    else:
        LoginPage()
def closeGame():
def NewAccount():
    Print("Input your Credentials")
    fname=input('Input your First Name')
    email=input('Input your email')
    passwordCheck=False
    while not passwordCheck:
        password=input('input password')
        password2=input('input your password again')
        if password==password2:
            passwordCheck=True
        else:
            input('passwords were not the same')

def Login():
    username=input("Username:")
    password=input("Password:")
    usernameCheck=True #Check SQL for username and password, return with true or false
    if usernameCheck:
        mainPage()
    else:
        input("Login Failed, Press Enter to Try again")
        Login()

LoginPage()


def mainPage():
    print("To play game press S:")
    print("To see highscore press H:")
    print("TO change personal credentials press C:")
    print("To quit press Q:")
    value = input("Enter your input here:")

    if value == 'S':
        print("The function for questions page")
    elif value == 'H':
        print("The function for highscore page")
    elif value == 'C':
        print("The function for changeing credentials page")
    elif value == 'Q':
        closeGame()
