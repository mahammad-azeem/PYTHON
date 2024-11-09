sentence = "This is most common interview question"
temp = 0
list = sentence.replace(" ", "")
op = [*list]
print(op)

for i in sentence.lower():
    a = sentence.count(i)
    if a > temp:
        temp = a
        out = i

print(f"{out} is the repeated the most : {temp}")
    