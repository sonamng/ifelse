
year=int(input("enter the year"))
if year%100==0:
    if year%400==0:
        print("leep year")
    else:
        print("not leep year")
else:
    print("not leep year")