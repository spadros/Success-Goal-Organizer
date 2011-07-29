calendar = open ("test.txt", "r+")

to_do = ["x", "y", "z"]
for todo in to_do:
    print(todo)
cal = calendar.read()
cal = str.splitlines(cal)
calendar.close
print calendar

print cal
