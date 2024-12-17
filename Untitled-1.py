"""
print("yousef") #print in python
age = 38
name = "Muhammed Essa"
print (name)
print (age)
# variables can be changed
num = 10 
dgree = 55.2
myname = 'yousef\'s havebook' #to ignore ' if i want to used it 

some_text = """"""trgjgfh
gd;kjh
fghj;f
gfjh"""
sometext='''hgkl
fhghkf;gjh
fghjklfgh
gfj;'''     # to identify the large text 
"""
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
"""
"""
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
"""

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

myname ={"yousef","mosed","fawze"}
print(myname)

myname.add("elshike")
print(myname)

myname.remove("yousef")
print(myname)

