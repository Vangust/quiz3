import requests
import json
import sqlite3


url = "https://animechan.vercel.app/api/random"


r = requests.get(url)

print('Status Code:', r.status_code)
print(r.headers)
print(r.text)

res = r.json()

f = open('file.json', 'w')
json.dump(res, f, indent=4)
f.close()

a = res['anime']
b = res['character']
c = res['quote']
print('\nanime:', a)
print('character:', b)
print('quote:', c)
print(a)
print(b)
print(c)


conn = sqlite3.connect('data.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS randomquote
(id INTEGER PRIMARY KEY AUTOINCREMENT,
anime VARCHAR(50),
character VARCHAR(50),
quote VARCHAR(1000))
''')
c.execute('INSERT INTO randomquote(anime, character, quote) VALUES (?, ?, ?)', (res['anime'], res['character'], res['quote']))
conn.commit()
conn.close()

# პროგრამის გაშვებისას ის აგენერირებს ერთ-ერთი შემთხვევითი ანიმედან შემთხვევით გამონათქვამს და მონაცემთა ბაზაში
# ჩაწერს ამ ანიმეს სახელს, პერსონაჟის სახელს რომელმაც ეს გამონათქვამი თქვა და ამ გამონათქვამს თვითონ.
