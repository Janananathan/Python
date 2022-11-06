import calculation as cal

x=int(input("enter x="))
print(x)
y=int(input("enter y="))
print(y)
choice=int(input("Select\n1 for add\n2 for substract\n3 for multiply\n4 for division\nChoice : "))
print(choice)
if(choice ==1):
    ad=cal.addition(x,y)
    print("addition =",ad)
elif choice==2:
    ad=cal.sybstract(x,y)
    print("substraction =",ad)
elif choice==3:
    ad=cal.multiplication(x,y)
    print("mulriplication =",ad)
elif choice==4:
    ad=cal.division(x,y)
    print("division =",ad)
else:
    print("wrong choice, existing")