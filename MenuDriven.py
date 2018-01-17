import goofycoin as goof
# g=goofy_coin()
# g.makecoin(23)
# g.makecoin(212)
# g.transaction("##GOOFY##","Sunchit",284)
# g.transaction("Sunchit","Sameer",28)
# g.print_goofy_list()
#
# print g.search_goofy_list(123)
# print "HERE"
g=goof.goofy_coin()
print "Hello! Welcome to Goofy Coin"
while(True):
    print "-------MENU-------"
    print "1 : Make a new coin "
    print "2 : Do a transaction "
    print "3 : To see the entire chain "
    print "4 : To quit "
    choice = input("Your Input : ")
    if(choice == 1):
        x=input("Enter Coin Value : ")
        g.makecoin(x)
    elif(choice == 2):
        x=raw_input("Sender : ")
        y=raw_input("Receiver : ")
        z=input("Amount :")
        g.transaction(x,y,z)
    elif(choice==3):
        g.print_goofy_list()
    elif(choice==4):
        break
    else:
        print "Enter Again ! "
