count = 0
with open('url.json', 'r') as file:
    for line in file:
        count += line.count('_class')
        

print(f"Number of times the string terraform-state present in the file is {count}")