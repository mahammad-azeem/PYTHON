temp = ""
empty = [item for item in range(1, 3, 1)]
for i in empty:
    temp = str(i) + temp
    result = temp
#result = str(empty)
print(result[::-1])