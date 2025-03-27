# Ketika pake open wajib di .close atau pakai With Block
# Memindahkan isi dari users1.txt ke users2.txt (Create First)
with open("users1.txt", "r") as db_users1:
    content_users1 = db_users1.readlines()
with open("users2.txt", "w") as db_users2:
    for user in content_users1:
        db_users2.write(user)