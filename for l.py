passw = input("Enter the first number:")
for i in range(10):
    if( passw =="ra"):
        print("correct")
        return
    elif (i <= 4 and passw !="ra"):
        print("try again")
        passw = input("Enter the first number:")
    else:
        print("wrong pass")
