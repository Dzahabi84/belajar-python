# Ketika pake open wajib di .close atau pakai With Block
import csv

with open("users.csv", "r") as users:
    users = open("users.csv", "r")
    users_csv = csv.reader(users, delimiter=",")

    for row in users_csv:
        print(f"{row[0]}, yang memiliki username {row[1]} dengan role nya sebagai {row[2]}")