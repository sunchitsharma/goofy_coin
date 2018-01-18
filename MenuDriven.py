import goofycoin as goof
import User_Management as um
user_dict={}
print "Hello! Welcome to Goofy Coin !"
pub,pri = um.adduser("##GOOFY##")
user_dict["##GOOFY##"]=[pub,pri]
g=goof.goofy_coin(user_dict["##GOOFY##"][0])
print "##GOOFY## ADDED : Let's Start !"
print "Lets Add Users to the System !"
no_of_users = input("Please tell the No of Users : ")
for i in range(0,no_of_users):
    temp = raw_input("Enter the user name : ")
    pub,pri = um.adduser(temp)
    print "========================================"
    print "PUBLIC KEY : "+str(pub)
    print "PRIVATE KEY : "+str(pri)
    print "========================================"
    user_dict[temp]=[str(pub),str(pri)]

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
        pub_sen =''
        pub_rec=''
        try:
            pub_sen = user_dict[x][0]
            pub_rec = user_dict[y][0]
            print pub_sen

        except:
            print "Invalid users !! Try Again"
        g.transaction(str(pub_sen),str(pub_rec),z)
    elif(choice==3):
        g.print_goofy_list()
    elif(choice==4):
        break
    else:
        print "Enter Again ! "
