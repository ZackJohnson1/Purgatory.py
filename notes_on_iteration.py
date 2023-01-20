li = ["one"]
try:
    print(li[2])
except IndexError:
    print("List is too short")