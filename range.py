temp = ""
result = 0
output = 0
for number in range(1, 23, 1):
        temp = str(number)
        result = temp.count('2')
        output += result
        print("*" * output)
print(f"Number of 2s in the given range is: {output}")

# temp = 2
# result = 1
# output = op + result = 0 + 1 = 1

# temp = 12
# result = 1
# output = 1 + 1 = 2