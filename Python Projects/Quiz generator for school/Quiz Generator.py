import math
import random


def elementary_school_quiz(flag, n):
    '''
    (int,int)->None
    preconditon: flag is 0 or 1 , n is 1 or 2
    '''
    # Your code for elementary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    # Preconditions: flag is 0 or 1, n is 1 or 2
    if (flag==0 and n==1):
        
        count=0
        x= random.randint(0,10)
        y=2**x
        print("Question:1")
        z=int(input("2 to what is "+str(y)+" i.e what is the result of log_2 (" + str(y)+")?"))
        if(z==x):
            count=count+1
        return(count)    
    elif (flag==0 and n==2):
        count=0
        x1= random.randint(0,10)
        y1=2**x1
        print("Question:1")
        z1=int(input("2 to what is "+str(y1)+" i.e what is the result of log_2 (" + str(y1)+")?"))
        if(z1==x1):
            count=count+1
        x2= random.randint(0,10)
        y2=2**x2
        print("Question:2")
        z2=int(input("2 to what is "+str(y2)+" i.e what is the result of log_2 (" + str(y2)+")?"))
        if(z1==x1):
            count=count+1
        return(count)    
    elif (flag==1 and n==1):
        count=0
        x= random.randint(0,10)
        y=2**x
        print("Question:1")
        z=int(input("what is the result of 2^"+str(x)))
        if(z==y):
            count=count+1
        return(count)    
    else:
        count=0
        x1= random.randint(0,10)
        y1=2**x1
        print("Question:1")
        z1=int(input("what is the result of 2^"+str(x1)))
        if(z1==y1):
            count=count+1
        x2= random.randint(0,10)
        y2=2**x2
        print("Question:2")
        z2=int(input("what is the result of 2^"+str(x2)))
        if(z2==y2):
            count=count+1
        return(count)    
        
        
        
        
        

        
def high_school_quiz(a,b,c):
    '''
    (int,int ,int)->None 
    '''
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    a=float(a)
    b=float(b)
    c=float(c)
    if (a==0.0):
        print("The quadratic equation is "+ str(b)+".x + "+ str(c)+" = 0")
    else:
        print("The quadratic equation is ", str(a),".x^2 +" ,str(b),".x + ", str(c), " = 0")
        
    
    if(a==0):
        if(b==0):
            if(c==0):
                print("is satisfied for all numbers x")
            else:
                print("is satisfied for no number x")
        else:
            if(c==0):
                print("has the followinf root/solution  0")
            else:
                x=-c/b
                print("has the following root/solution  ", x)
    else:
        des= (b**2)-(4*a*c)
        if(des>0):
            print("has the following roots:")
            print((-b+math.sqrt(des))/(2*a)," and ",(-b-math.sqrt(des))/(2*a))
        elif(des==0):
            print("has only one real root ")
            print(-b/(2*a))
        else:
            print("has the following comlex roots: ")
            print (-b/(2*a), "+ i", math.sqrt(abs(des))/(2*a),  "\n and")
            print (-b/(2*a), "- i", math.sqrt(abs(des))/(2*a) )
             
                





            
       
        



# main

# your code for the welcome tmessage goes here
print("*******************************************")
print("*                                         *")
print("*  __Welcome to my math quiz-generator__  *")
print("*                                         *")
print("*******************************************")
print()
print()

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status=='1':
    # your code goes here
    #pass
    print("\n \n")
    x=len(name)+len( '__ welcome to my quiz-generator for elementary school students.__')
    print("*"*(x+7))
    print("*"+ " "*(x+5) +"*")
    print("*  __"+name+","+" welcome to my quiz-generator for elementary school students.__  *")
    print("*"+ " "*(x+5) +"*")
    print("*"*(x+7))
    print()
    print()
    Flag=int(input(name+" What would you like to practice? Enter \n0 for inverse of exponention \n1 for exponention\n"))
    if (Flag==0 or Flag==1):
        n= int(input("How many questions would you like to do? Enter 0,1, or 2:  "))
        if(n==0):
            print("Zero questions. OK. Good bye")
        elif(n==2 or n==1):
            print(name+", Here is your",n,"questions:")
            x=elementary_school_quiz(Flag, n)
            if(n==1 and x==1):
                print("congratulations",name,"! You'll probably get an A tomorrow")
            if(n==2 and x==2):
                print("congratulations",name,"! You'll probably get an A tomorrow")
            
        else:
            print("Only 0,1, or 2 are valid choices for the number of questions.")    
    else:
        print("Invalid choose. Only 0 or 1 is accepted.")
elif status=='2':

    # your code for welcome message
    x=2+len("*  __quadratic equation, a.x^2 + b.x + c, solver for "+name+"__")
    print("*"*(x))
    print("*"+ " "*(x-2) +"*")
    print("*  __quadratic equation, a.x^2 + b.x + c, solver for "+name+"__")
    print("*"+ " "*(x-2) +"*")
    print("*"*(x))
    print()
    print()
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here
        question = question.lower()
        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
            a=(input("Enter a number for cofficient a: "))
            b=(input("Enter a nubmer for cofficient b: "))
            c=(input("Enter a nubmer for cofficient c: "))
            high_school_quiz(a,b,c)
 
else:
    # your code goes here
    print(name+"you are not a target Audience for this software.")

print("Good bye "+name+"!")
