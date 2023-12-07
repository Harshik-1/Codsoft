print("CALCULATOR")
num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
a=num1+num2
b=num1-num2
c=num1*num2
d=num1/num2
print("1=add")
print("2=sub")
print("3=mul")
print("4=div")
choice=int(input("Enter you choice:"))
if choice==1:
  print("add is:",a)
elif choice==2:
  print("sub is:",b)
elif choice==3:
  print("mul is:",c)
elif choice==4:
  if num2 != 0:
    print("div is:", d)
  else:
    print("Division by zero is not allowed.")
else:
   print("invalid choice")