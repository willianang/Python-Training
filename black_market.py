def arms(passkey,money=500):
    print("Hello World")
    name = input("Enter your name: ")
    print("Welocome %s to this program!"% name)
    password = input("Enter the password to acess the program:")
    if password == str(passkey):
        print("Access Granted!")
    else: 
        print("Access Denied!")
    print("Alright %s, let's proceed."%name)
    gun=["1.pistol","2.rifle","3.sniper","4.rocket",]
    print("Here are avaliable guns:")
    for x in gun:
        print(x)
    purchase = int(input("Select the gun you want to purchase:"))
    if purchase == 1 and money >= 100:
        print("You have purchase a pistol for $100!")
        money -= 100
    elif purchase == 2 and money >= 300:
        print("You have purchase a rifle for $300!")
        money -= 300
    elif purchase == 3 and money >= 500:
        print("You have purchase a sniper for $500")
        money -= 500
    elif purchase == 4 and money >= 1000:
        print("You have purchase a rocket for $1000")
        money -= 1000
    else:
        print("Insufficient fund or invalid option!")
    print("You have $%d remaining."%money)
    return money



i = True
while i:
    print("Plese select your service:")
    service = input("1.Arms shop\n2.Exit\n")
    if service == "1":
      arms("@Leo301929#",500)
    elif service == "2":
      print("Thank you for visiting us!")
      i=False
    else:
      print("Invalid option")
      continue
    exit_choice = input("Do you want to exit? (yes/no):")
    if exit_choice.lower() == "yes":
       i= False
    else:
       i =True
       continue




