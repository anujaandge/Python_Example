words=['cat','dog','infrastructure','window']
for w in words:
    print(w, len(w))

users={"Hans":"active","Anuja":"inactive","Eleonore":'active'}
for user,status in users.copy().items():
    if status=='inactive':
       del users[user]
print(users)

active_users={}
for user,status in users.items():
    if status=='active':
        active_users[user]=status

print(active_users)

