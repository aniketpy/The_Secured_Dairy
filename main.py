import time
from goto import with_goto
from temp import *

def open_dairy(dairy):
    f=open(f"{dairy}.txt","a+")
    ch=0
    while(ch!=3):
        ch=int(input("\nWelcome to your dairy:\n\t1.Read \n\t2.Write \n\t3.Exit\n\t\t"))
        if ch==1:
            f.seek(0)
            a=f.readlines()
            for i in a:
                i=decrypt(i)
                print(i)

        elif ch==2:
            app=str(input("Enter your text: \n"))
            app=encrypt(app)
            # print("\n\n",app)
            f.write(f" \n{app}")

        elif ch==3:exit
    f.close()

def login_check():
    u=str(input("\n\nEnter username: "))
    p=str(input("Enter password: "))
    u=encrypt(u)
    p=encrypt(p)
    l=open("Login.txt", "r")
    a=l.readlines()
    for i in a:
        i=i.split("\n")[0]
        i=i.split(",")
        if u==i[0] and p==i[1]:return u,11 #login
        elif u==i[0] and p!=i[1]:return u,10  #wrong pass
    else: 
        return  u,0
    l.close()

@with_goto
def add_user():
    label .begin
    u=str(input("\nEnter username: "))
    p=str(input("Enter password: "))
    u=encrypt(u)
    p=encrypt(p)
    flag=0
    l1=open("Login.txt", "a+")
    l1.seek(0)
    a=l1.readlines()
    for i in a:
        i=i.split("\n")[0]
        i=i.split(",")
        if u!=i[0]:
            if flag==0:
                l1.write(f"\n{u},{p}")
            flag+=1
        else:
            print("\tUsername is already taken.")
            goto .begin
    l1.close()   
    print("\tUser Added Sucessfully")

@with_goto
def start():
    print("\n\n\t\t🔥🔥🔥Welcome to The Secured Dairy🔥🔥🔥\n\n")
    time.sleep(2)
    label .begin
    u,check=login_check()
    if check==10:
        print("\tYour entered password is wrong")
        c=int(input("\nPress 0 to retry OR 1 to exit: "))
        if c==0:
            goto .begin
        elif c==1:exit
        else: print("Enter correct option")
    
    elif check==0:
        print("\tNo user Found")
        c=int(input("Press 0 to retry OR 1 To add user OR 2 To exit: "))
        if c==0:
            # check=login_check()
            goto .begin
        elif c==1:
            add_user()
            goto .begin
        elif c==2:exit    

    elif check==11:
        print("\n\tLogin Sucessfully")
        open_dairy(u)








if __name__ == "__main__":
    start()