#import re
sentence = "This is a common interview question"
count = dict()
#sentence = re.sub(" ", '', sentence)
#print(sentence)
for i in sentence:
    if i != " ":
        count[sentence.count(i)] = i

# if count[max(*count.keys())] == ' ':
#     count[max(*count.keys())] = 0
# else:
#     print(f"{count[max(*count.keys())]}")

#print(f"count dict is : {count}")
print(f"{count[max(*count.keys())]}")