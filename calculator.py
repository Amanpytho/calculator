from math import *

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y != 0:
       return x/y
    else:
        print("Invalid Input. Dividor can not be zero.")

def power(x,y):
    return pow(x,y)
def square_root(x):
    return sqrt(x)
def sine(x):
    return sin(radians(x))
def cosine(x):
    return cos(radians(x))

def calculator():

    print("---Scientific calculator---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. power")
    print("6. Square root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Exit")

    while True:
      while True:
       try:
          choice = int(input("\nEnter your choice: "))
          break
       except:
          print("Invalid Input! Please enter a number (1-9)")
          
      if choice in [1,2,3,4,5]:
      
       while True:
         try: 
          x= int(input("Enter first number: "))
          y= int(input("Enter second number: "))
          break
         except:
            print('Please enter a valid input!')
      
      elif choice in [6,7,8]:
  
         while True:
          try:
            x= int(input("Enter the number: "))
            break
          except:
             print("Please eneter a valid input!")
  
      elif choice == 9:
          print("Exiting scientific calculator...")
          return
      else:
        print("Please enter a valid choice!")
          
      
      if choice == 1:
         print(f"{x} + {y} = {add(x,y)}")
      elif choice == 2:
         print(f"{x} - {y} = {sub(x,y)}")
      elif choice == 3:
         print(f"{x} * {y} = {mul(x,y)}")
      elif choice == 4:
         print(f"{x} / {y} = {div(x,y)}")
      elif choice == 5:
         print(f"{x} raise to power {y} is {power(x,y)}")
      elif choice == 6:
         print(f"Square root of {x} is {round(square_root(x),3)}")
      elif choice == 7:
         print(f"sine of angle {x} is {round(sine(x),2)}")
      elif choice == 8:
         print(f"Cosine of {x} is {round(cos(x),2)}")
    
calculator()