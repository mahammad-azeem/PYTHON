from pathlib import Path
import re

store_duplicates = dict()

with open("sample.txt", "r") as file:
    for line in file:
        line = re.sub("[^a-zA-Z]+", " ", line)
        #for item in line.split():
        for item in line.split():
            if item != "":
                item = item.lower()
                if item not in store_duplicates:
                    store_duplicates[item] = line.count(item)
                else:
                    store_duplicates[item] = int(store_duplicates[item]) + line.count(item)

#print(f"The word {max(*store_duplicates.values())} is repeated the most {max(*store_duplicates.values())}")
for key, value in store_duplicates.items():
    if value == max(*store_duplicates.values()):
        print(f"The word {key} is repeated the most {value}")

print(store_duplicates)
