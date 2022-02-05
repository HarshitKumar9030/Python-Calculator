
calc =  '''
      _____                            _____                                    _________     ________      ______
     /           / \      |           /        |      |   |             /\          |        |        |    |      |   PYTHON
    /           /   \     |          /         |      |   |            /  \         |        |        |    |      | 
    |          /_____\    |          |         |      |   |           /____\        |        |        |    |______| 
    \         /       \   |          \         |      |   |          /      \       |        |        |    |       \\
     \_____  /         \  |_______    \_____   |______|   |______   /        \      |        |________|    |        \    BY LEON  
        '''#Defining calc (If we want to use multi line strings , we use " '''Triple single quotes''' ") 

welcome = "Welcome to Calculator | Python | Press enter to start \n" #Defining welcome
print(calc) #Printing the credits and logo
print(input(welcome))#Printing the welcome
print(" Enter 1 for addition \n Enter 2 for subtraction \n Enter 3 for multiplication \n Enter 4 for division \n Enter 5 Decimal related stuff!\n")#Printing the choices
input("If you want to do decimal related things you have to select the 5 option : PRESS ENTER \n")#Just a note
choice = input("What you want to do : ")#Telling the user to Enter his/her choices
intigerizedchoice = int(choice) #Created a variable for making the choice variable an integer 
if intigerizedchoice > 5:
    print("Error\nYou must choose between 1 and 5," )
    print("Please restart the program now")
    exit()#In this if a user enter a value more than 5 in his choice he will get error and the program will stop

if intigerizedchoice == 1:
 enternum = "Enter your first number : "
 enternum = input(enternum)
 enternum = int(enternum)

 enternum2 = "Enter your second number : "
 enternum2 = input(enternum2)
 enternum2 = int(enternum2)
 sol = (enternum + enternum2)
 print("Here is your answer : ",sol)

if intigerizedchoice == 2:
 enternum = "Enter your first number : "
 enternum = input(enternum)
 enternum = int(enternum)

 enternum2 = "Enter your second number : "
 enternum2 = input(enternum2)
 enternum2 = int(enternum2)
 sol = (enternum - enternum2)
 print("Here is your answer : ",sol)

if intigerizedchoice == 3:
 enternum = "Enter your first number : "
 enternum = input(enternum)
 enternum = int(enternum)

 enternum2 = "Enter your second number : "
 enternum2 = input(enternum2)
 enternum2 = int(enternum2)
 sol = (enternum * enternum2)
 print("Here is your answer : ",sol)

if intigerizedchoice == 4:
 enternum = "Enter your first number : "
 enternum = input(enternum)
 enternum = int(enternum)

 enternum2 = "Enter your second number : "
 enternum2 = input(enternum2)
 enternum2 = int(enternum2)
 sol = (enternum / enternum2)
 remainder = (enternum % enternum2)
 q = "Quotient is : "
 r = " and Remainder is : "
 print("Here is your answer : ",q,sol,r,remainder)

if intigerizedchoice == 5:
    input("Welcome to, Decimal Calculator | Python | PRESS ENTER")
    print(" Enter 1 for addition \n Enter 2 for subtraction \n Enter 3 for multiplication \n Enter 4 for division\n")
    print(" This is only for decimal values")
    floatchoice = input("Enter your choice : ")
    intigerizedfloatchoice = int(floatchoice)
    if (intigerizedfloatchoice > 4):
        print(" Error\n You must enter your choice between 1 and 4")
        print(" Please restart the program now.")
        exit()


    if intigerizedfloatchoice == 1:
     enterfloatnum = "Enter your first number : "
     input(enterfloatnum)
     enterfloatnum2 = input('Enter your second number : ')
     enterfloatnum2 = float(enterfloatnum2)
     sol = (enterfloatnum + enterfloatnum2)
     print("Here is your answer",sol)

    if intigerizedfloatchoice == 2:
     enterfloatnum = "Enter your first number : "
     input(enterfloatnum)
     enterfloatnum2 = input('Enter your second number : ')
     enterfloatnum2 = float(enterfloatnum2)
     sol = (enterfloatnum - enterfloatnum2)
     print("Here is your answer",sol)

    if intigerizedfloatchoice == 3:
     enterfloatnum = "Enter your first number : "
     input(enterfloatnum)
     enterfloatnum2 = input('Enter your second number : ')
     enterfloatnum2 = float(enterfloatnum2)
     sol = (enterfloatnum * enterfloatnum2)
     print("Here is your answer",sol)

    if intigerizedfloatchoice == 4:
     enterfloatnum = "Enter your first number : "
     enterfloatnum = input(enterfloatnum)
     enterfloatnum = float(enterfloatnum)

    enterfloatnum2 = "Enter your second number : "
    enterfloatnum2 = input(enterfloatnum2)
    enterfloatnum2 = float(enterfloatnum2)
    sol = (enterfloatnum / enterfloatnum2)
    remainder = (enterfloatnum % enterfloatnum2)
    q = "Quotient is : "
    r = " and Remainder is : "
    print("Here is your answer : ",q,sol,r,remainder)
   
