print(":::::::::::::::::: simple single vairbale ::::::::::::::::::")
a = "niranjan"
print(a)

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")



print("____________________________Assigning single value to multiple variables____________________________") 

x=y=z=50    
print(x)    
print(y)    
print(z) 

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("------------------------------- Assigning multiple values to multiple variables -------------------------------")

a,b,c=5,10,15    
print(a)    
print(b)   
print(c)

print(a , b, c, )
print("************************* show sum of total variable *************************")
print(+ a + b + c   ) # show sum of total variable

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print("<<<<<<<<<<<<<<<<<<<<<<<<< VARIABLE AND TYPE OF VARIABLES >>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("------------------------ Type of Variable:-  local and global --------------------------")
print("*********************************** Here we are Defining local variables ***********************************")

# local variables- which is define into function
def add():    
    a = 20  
    b = 30  
    c = a + b  
    print("The sum is:", c)  
  
# Calling a function  
add()  


print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print ("------------------------------------ Here we going to define Global variable ------------------------------------------")

# Defining global variables
print(" ----------------------- Here we using global variables ------------------------- ")
# global variables means the variable which is use for entire code we can use it everywhere in code
d = 101;  
# Global variable in function  
def GLOBALVARIABLE():    
         print(d);  
# modifying a global variable  
x = 'Welcome To global variable'
print(d); 
  
GLOBALVARIABLE(); # call
print(d);  





print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print(">>>>>>>>>>>>>>>>>>>>>>>> To Delete a Vriable <<<<<<<<<<<<<<<<<<<<<<<<")
t = 3
print(t)
print(" ----------------------------Now Variable is Deleted Here ---------------------------- ")
del(t)
print(t)