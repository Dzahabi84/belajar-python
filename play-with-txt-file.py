"Memindahkan isi dari users1.txt ke users2.txt (Create First)"
db_users1 = open("users1.txt", "r")
db_users2 = open("users2.txt", "w")
content_users1 = db_users1.readlines()
for user in content_users1:
    db_users2.write(user)