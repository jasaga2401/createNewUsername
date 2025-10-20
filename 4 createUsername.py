# Creating a new username 
def createUsername():
    flag = False
    count = 1
    fname = input('Enter your firstname: ')
    sname = input('Enter your surnamename: ')

    uname = sname + fname[0] + str(count)
    print(uname)

    while (not flag):
        if (exitingUsers(uname)):
            print('The username is unique')
            flag = True
        else:
            count += 1
            uname = sname + fname[0] + str(count)
            print('New username: ', uname)
        
    
def exitingUsers(uname):
    uNameList = ['SimonJ1', 'JohnsonB1', 'BanksR1', 'HollandE1']

    for name in uNameList:
        if (name == uname):
            return False
            break
    return True

createUsername()
