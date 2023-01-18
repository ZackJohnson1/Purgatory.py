some_data_collection = ['3', '4', '5','dog', 'cat']
for item in some_data_collection:
    if item.isdigit():
        print(f'{item} is an integer')
    elif item.isalpha():
        print(f'{item} is a string')

#  Iterating over a list of strings and using the isdigit() and isalpha()
# method to determine whether a string is numeric or alphabetical