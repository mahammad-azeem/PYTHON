age = input("Age : ")
try:
    if age >= 5:
        print("Ok")
except ValueError as error:
    print(error)
else:
    print("Try block executed fully")
finally:
    print("End of the execution")