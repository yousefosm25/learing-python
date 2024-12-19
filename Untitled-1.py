
print("yousef") #print in python
age = 38
name = "Muhammed Essa"
print (name)
print (age)
# variables can be changed
num = 10 
dgree = 55.2
myname = 'yousef\'s havebook' #to ignore ' if i want to used it 

some_text = """trgjgfh
gd;kjh
fghj;f
gfjh"""
sometext='''hgkl
fhghkf;gjh
fghjklfgh
gfj;'''     # to identify the large text 

print(f"{name} {age}") #how to print two different variables with different format 

salary = 3000
employeeinfo = "yousef mosed {} dollar "
print(employeeinfo.format(salary)) # to put a variables in the text 

led_off = False
lde_on = True
num1 = 10
num2 = 20
if led_off:
    print("LED is off")
    
if num1>num2:
     print("num1 is greater than num2")
     
        
if num1 == num2:
     print("num1 is equal to num2")
else:
    print("num1 is not equal to num2")
    
if num1 < num2:
    print("num1 is less than num2")
elif num1 > num2:
    print("num1 is greater than num2")
else:
    print("num1 is not less than num2")
    
print("Hello World")

names = ["yousef","mosed","fawze","yousef"]    #list
print(names)
print (len(names))     #how many items in the list
ages =[1,2,3,4,5,6,7]
check1=[True,False,True,False,False,False]
dataset = ["yousef","mosed",1,True]
print(names[0])   # to print the first item
names.insert(0,"esraa") # to insert the items 
names.insert(1,"mo")
print(names) 
del(names[5])# to delete items
print(name)


#tuple unchangable order
mypermissionlevel = ("admin","teacher","student")    #tuple
print(mypermissionlevel)
print(len(mypermissionlevel))

mykey = ("1",)
print(mykey)

ages =(1,2,3,4,5,6,7)
check1=(True,False,True,False,False,False)

dataset = ("yousef","mosed",1,True)
print(dataset[0])

#to change items in tuple

mylist = list(mypermissionlevel) # to change tuple to list
mylist[2] = 3 
mytuple = tuple(mylist) # to change list to tuple
print(mytuple)


#Sets uncachable and unordered unindex 
'''
myname ={"yousef","mosed","fawze"}
print(myname)

myname.add("elshike")
print(myname)

myname.remove("yousef")
print(myname)
'''
# dictionary ordered changeable not repeat

mydoc={"name": "yousef"
       ,"last_name":"elshike" 
       ,"age":19
       ,"years":[1,2,3,4,5,6]}
print(mydoc),
print(mydoc["name"])
print(len(mydoc))
mydoc["department"]="development"
print(mydoc)
mydoc.update({"name":"mosed"})
print(mydoc)
mydoc.pop("age")
print(mydoc)

# for loop
print(names)
for a in names:
    print(a)
for a in name:
    print(a)

for a in range(7):
    print(a)
for a in range(1,20):
    print(a)
for a in range(1,20,4):
    print(a)

#function 

def my_name():
    print("yousef")

def my_name(lname):
    print("yousef " + lname)
    
my_name("yousef")


def my_name(lname,fname):
    print(f"{fname} {lname}")
    
my_name("ali","ahmed")

# *args
def my_name(*lname):
    print("Name is : " + lname[0])

my_name("ahmed" , " Mahmed")

def my_name(lname,sname,fname):
    print(f"{fname} {sname} {lname}")
  

#my_name(fname=input("first name: "),sname=input("secand name: "),lname=input("last name: "))

#**kwargs
def my_name(**names):
    print(f"{names["fname"]}{names["lname"]}")
my_name(fname ="ahmed",lname = "marime")

def my_name(lname =" elshike"):
    print(f"yousef{lname}")
    
my_name("mosed")

def addNumbers(y):
    return 2*y

print(addNumbers(2))

def changetoupcase(myname):
    return myname.upper() 
print(changetoupcase("yousef"))

#mytext = input('enter first name: ')
#rint(f"hello {mytext.upper()}") 

#mytext =input('enter number: ')
#print(type(mytext))
#print(f"square of {mytext} is {int(mytext)**2}")

#calss object

class Person:
    name= "yousef"
    
myname=Person()

myname.name

print(myname.name)


class Person1:
   def __init__(self,name,age,salary):
       self.name = name
       self.age  = age
       self.salary = salary
    
yousef=Person1("yousef",30,2500)
mosed=Person1("mosed",50,3000)
esraa=Person1("esraa",30,2000)
print(f"{yousef.name} {yousef.age} {yousef.salary}")
print(f"{mosed.name} {mosed.age} {mosed.salary}")
print(f"{esraa.name} {esraa.age} {esraa.salary}")    


class Person2:
    def __init__(self,name,age,salary):
       self.name = name
       self.age  = age
       self.salary = salary
    def __str__(self):
        return f"Name: {self.name} Age: {self.age} Salary: {self.salary}"
    def in_salary(self):
        z =self.salary +1000
        print (z)
        
yousef = Person2("yousf",40,20500)
print(yousef)
yousef.in_salary()