age=int(input("enter the age"))
if age<=12:
    print("child")
elif age<=25:
    print("student")
elif age<=50:
    print("younger")
elif age<=100:
    print("older")
else:
    print("invailed")