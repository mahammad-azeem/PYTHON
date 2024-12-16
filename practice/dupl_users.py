from pathlib import Path

dup_user = {}

with open("passwd", "r") as file:
    for i in file:
        if i.split(':')[0] in dup_user:
            print(f"duplicate user {i.split(':')[0]} has uid {i.split(':')[2]}")
        else:
            dup_user[i.split(':')[0]] = i.split(':')[2]

print(f"dup_user contents is >>> {dup_user}")