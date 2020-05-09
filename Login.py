#checks a username and password
def checkLogin():

    name = input("Name: ")
    password = input("Password: ")

    #Open login file and check details match
    with open("Login_data.txt", 'r') as file:
        for row in file:
            details = row.split(",")
            user = details[0]
            pw = details[1].replace("\n", "")

            #Return True if name and password is found in file
            if user == name and password == pw:
                return True, name

    #If it can't find the details in the file, return false
    return False, name