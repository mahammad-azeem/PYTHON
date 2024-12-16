s = input('Enter a string :')
k = int(input('Enter number of equal parts of substring :'))

n = len(s) // k
store_string = []
tmp = 0
str = ''
for i in range(n):
    if i == 0:
        store_string.append(s[tmp:n])
        tmp += n
    else:
        store_string.append(s[tmp:tmp+n])
        tmp += n

print(f"sliced string is { store_string }")
#output = [ output.app for i in store_string for j in i if i.count(j) == 1 ]
output = []
for i in store_string:
    for j in i:
        if j not in str:
            str += j
    output.append(str)
    str = ''

print(f"output is  { output }")