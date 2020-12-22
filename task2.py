import threading
import random
import webbrowser
def wlcm(s):
                s="WELCOME TO TASK MANAGEMENT"
                return(s)
def working(m):
                m=" "
                name=str(input("Enter the name"))
                print("Hi",name)
                n=int(input("enter number of tasks"))
                tasklist=[]
                seq=(1,2,3,4,5)
                for i in range(n):
                                task=str(input("Enter the task"+str(i+1)+" "+name))
                                tasklist.append(task)
                                
                print(tuple(zip(seq,tasklist)))
                choice=[]
                for n in range(len(tasklist)):
                                c=int(input("Enter choice"+str(n+1)))
                                choice.append(c)
                                p=tuple(zip(choice,tasklist))
                               
                for i in range (len(choice)):
                                for j in choice:
                                                
                                                status=0
                                                while status>=0:
                                                                a=int(input("Are u done with "+"task"+str(j)+"?"))
                                                                status+=a
                                                                if status==0:
                                                                                print("Complete it right now")
                                                                
                                                                else:
                                                                                print("Good",name)
                                                                                break
                                break
                
                return(" ")

                
def greet_1(wish):
                wish=str(input("continue or quit"))
                if wish=="continue":
                                a_1=random.randint(1,100)
                                a_2=random.randint(1,100)
                                print(str(a_1)+"+"+str(a_2)+"=")
                                ans=int(input("Enter the captcha"))
                                if ans==a_1+a_2:
                                                print("U can continue")
                                                print(working(0))
                                else:
                                                print("Hall of shame")
                return("")
                                

                
def password(n):
                n=int(input("Enter the numeric password"))
                if n==6262850785:
                                print(greet_1(wish))
                return("")
wish=" "
while wish!="quit":
                print(wlcm(" "))
                print(password(0))
                opt=int(input("do u want to quit"))
                if opt==0:
                                continue
                else: 
                                print("For more such apps go to play store\n https://play.google.com/store/apps/details?id=com.anydo&hl=en_IN")
                                click=str(input("Enter 'open' to open the link and 'e' to exit"))
                                if click=="open":
                                                webbrowser.open("https://play.google.com/store/apps/details?id=com.anydo&hl=en_IN")
                                                break
                                elif click=="e":
                                                print("THANKYOU FOR CHOOSING TASK")
                                                break
                                else:
                                                pass
                                                break

