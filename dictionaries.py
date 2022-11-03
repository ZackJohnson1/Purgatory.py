
swiatek = {'Ranking': 1, 'first_name': 'Iga', 'last_name': 'Swiatek', 'Age': 21, 'country': 'Poland'}
jabeur = {'Ranking': 2, 'first_name': 'Ons', 'last_name': 'Jabeur', 'age': 28, 'country': 'Tunisia'}
pegula = {'Ranking': 3, 'first_name': 'Jessica', 'last_name': 'Pegula', 'age': 28, 'country':'United States'}
gauff = {'Ranking': 4, 'first_name': 'Coco', 'last_name': 'Gauff', 'age': 18, 'country': "United States"}
sakkari = {'Ranking': 5, 'first_name': 'Maria', 'last_name': "Sakkari", 'age': 27, 'country': "Greece"}
garcia = {'Ranking': 6, 'first_name': 'Caroline', 'last_name': "Garcia", 'age': 29, 'country': "France"}
sabalenka = {'Ranking': 7, 'first_name': 'Aryna', 'last_name': "Sabalenka", 'age': 24, 'country': "Belarus"}
kasatkina = {'Ranking': 8, 'first_name': 'Daria', 'last_name':'Kasatkina', 'age': 25, 'country': 'Russia'}
kudermetova = {'Ranking': 9, 'first_name': 'Veronika', 'last_name': 'Kudermetova', 'age': 25, 'country': 'Russia'}
halep = {'Ranking': 10, 'first_name': 'Simona', 'last_name': 'Halep', 'age': 31, 'country': 'Romania'}


top_ten = swiatek, jabeur, pegula, gauff, sakkari, garcia, sabalenka, kasatkina, kudermetova, halep
top_10_dict = {**swiatek, **jabeur, **pegula, **gauff, **sakkari, **garcia, **sabalenka, **kasatkina, **kudermetova, **halep}
top_10 = [swiatek, jabeur, pegula, gauff, sakkari, garcia, sabalenka, kasatkina, kudermetova, halep]

#print(sabalenka.get('last_name'))
#print(top_10_dict.get('first_name'))
#print(top_ten)
print(top_10_dict)