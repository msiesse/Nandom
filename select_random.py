import random
import webbrowser

with open('fdb') as file_database:
    database = file_database.read().splitlines()

n = random.randint(0, len(database))

url = 'https://www.netflix.com/watch/' + database[n]

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

webbrowser.get(chrome_path).open(url)