num1=int (input("enter the number:"))
num2=int (input("enter the number:"))
choice= int (input("enter the option 1)add\n 2)sub\n 3)multiply\n 4) divide\n"))
if choice ==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
else:
    print("not valid input")
