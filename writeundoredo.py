data = input('Enter :')
# data    = inp.split("'")[1]
# action  = inp.split("'")[3]
# tmp = ''
# Rtmp = []
# count = 0
# #Input
# #Interpret: 'docx', Action: 'WaWxUUR'
# #Expected Output
# #docxa > docxax > docxa > docx > docxx

# # for seq in action:
# #     if seq == 'W':
# #         op[seq + seq[seq.index(seq)+1]] = data + seq[seq.index(seq)+1]
# #         tmp = data + seq[seq.index(seq)+1]
# #     if seq == 'U':
# #         tmp[::-1] = ""
# #     if seq == 'R':
# #         tmp

# for char in action:
#     if char == 'W':
#         data = data + action[count+1]
#         Rtmp.append(action[count+1])
#     if char == 'U':
#         data = data[:-1]
#     if char == 'R':
#         data = data + Rtmp[-1]
#     else:
#         pass
#     count += 1
#     print(Rtmp)
#     print(f"{char} : : {data}")

# print(f"Expected output : {data}")

# tmp = ''
# count = 0
# store = data.split("'")[1]
# #print(store)

# for char in list(data.split("'")[3]):
#     if char != 'W' or char != 'U' or char != 'R':
#         tmp = tmp + char
#         store = store + char
#     else:
#         pass
#         #print(char)
#     if char == 'U':
#         store = store[:-1]
#     elif char == 'R':
#         tmp = tmp[::-1]
#         store = store + tmp[count]
#         count += 1
#     else:
#         pass
#     print(tmp)
#     print(store)
# #print(store)

# #Interpret: 'docx', Action: 'WaWxUUR'
result = data.split("'")[1]
tmp = ''
count = 1
res = {}

for i in list(data.split("'")[3].replace('W', '')):
    if i == 'U':
        result = result[:-1]
        tmp = tmp + result[-1]
    elif i == 'R':
        #tmp = tmp[::-1]
        result = result + tmp[-count]
        count += 1
        print(tmp)
    else:
        result = result + str(i)
    res[i] = result


print(f"res is {res}")
print(f"result is {result}")

#print(result)