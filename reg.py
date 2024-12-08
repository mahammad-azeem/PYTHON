import re

string = input('Enter the string :')
s = re.sub('[^0-9a-zA-Z]+', '', string)
print(f"post applying regex is : {s}")