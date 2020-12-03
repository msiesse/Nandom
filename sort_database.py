with open('film_database') as file_database:
    database = file_database.readlines()

final_db = list(dict.fromkeys(database))

f_fdb = open('fdb', 'w')
for elem in final_db:
    f_fdb.write(elem)