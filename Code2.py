#7 Задача
#from random import *
#A<B
#A=randint(10,100)
#B=randint(100,1000)
#K=int(input("K: "))
#for i in range(A,B+1):
#    if i%K==0: print(i)

#for x in range(10): #0-9...
#    print("Hello world!")
#for x in range(1,11): #1-10...
#    print("Hello world!")
#for x in range(start,stop,step): #0...N-1
#    print("Hello world!")

#1 Задача
#p=0
#for i in range(15): #0,1,2,3...
    #A=0
    #while type(A)!=float:
        #try:
            #A=float(input(f"Sisesta {i+1} arv -> "))
        #except ValueError:
            #print("Oi")

    #if A==round(A): #Округление
       #p+=1
        #print(str(A)+" on täisarv") #Выводит, что число целое
    #else:
        #print(str(A)+" ei ole täisarv") #Выводит, что число не целое
#print(str(p)+" Täisarvud") #Выводит сколько целых чисел получилось

#4 Задача
#for i in range(10,21):
#    print(i**2)


#6 Задача
#from random import *
#p=0
#n=0
#N=randint(1,10)
#for i in range(N):
#    Arv=int(input("Sisesta arv"))
#    if Arv>0:
#        p+=1
#    elif Arv<0:
#        n+=1
#print("Neg: "+ str(n))
#print("Pos: "+ str(p))
#print("Nullid: "+ str(N-n-p))

#2 Задача
#A=input("Sisesta arv - ")
#while int(A)<=1:
#        try:
#            A=int(input(f"Sisesta {i+1} arv -> "))
#        except:
#            TypeError
#Summa=0
#for i in range(1,int(A)+1):
#    Summa+=i
#print("Summa võrdlub ",Summa)



#3 Задача
#k=1
#for i in range(8):
#    arv=float(input("Arv: "))
#    if arv>0:
#        k*=arv
#print(k)

#9 Задача
#p=1.03
#S=int(input("Sisesta summa: "))
#N=int(input("Mittu aastat: "))
#for aasta in range(1,N+1):
#    S*=p
#    print(aasta, "aasta pärast tulemus on",round(S,2))

#13 Задача
#K=0
#Summa=0
#for i in range(100,1001):
#    if i % 7==0:
#        print(i) #Вывели на экран
#        K+=1 #Korrus
#        Summa+=i #Summa, mis jagatakse 7
#print("Summa: ", Summa,"Kogus: ", K)

#15 Задача
#for rjady in range(10):
#    for stroka in range(10):
#        print(stroka, end=" ")
#    print()

#16 Задача
#for rjady in range(1,10):
#    for stroka in range(1,10):
#       if rjady==stroka:
#           print(stroka,end=" ")
#       else:
#           print("0",end=" ")
#    print()

#29 Задача
#for rjady in range(1,10):
#    for stroka in range(1,10):
#       if rjady==stroka:
#           print("x",end=" ")
#       elif stroka==1:
#           print("x",end=" ")
#       else:
#           print("0",end=" ")
#    print()

#Задача с While
#loom=input("Купи слона! ")
#while loom.title()!="Слон": #upper(), lower()
#    loom=input("Все говорят " +loom+"! А ты купи!!!")
#print("Молодец!!!")


#28 Задача
from random import *
A=randint(1,10)
B=int(input("Введи загаданное число: "))
if A==B:
    print("Молодец, ты угадал!")
else:
    print("К сожалению, ты не угадал.")
