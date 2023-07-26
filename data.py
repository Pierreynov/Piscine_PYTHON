import pandas as pd 

data = {
    'apples': [3, 2, 0, 1], 
    'oranges': [0, 3, 7, 2]
}

df = pd.read_csv("Automobile_data.csv")
print(df)

import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
df2 = pd.read_sql_query("SELECT * FROM movie", con)
print(df2)

dfi = df.info()
print(df.shape)
# Afficher les colonnes

print(df.columns)

# Changer le nom des colonnes

print ("---REPLACE---")
df.rename(columns={
    'index' : 'toto',
    'length' : 'tata'
}, inplace = True)

print(df.columns)

#comprehension list 

a = [1, 2, 3]

b = [item ** 2 for item in a if item %2 ==0]
print(b)

d = {item : item ** 2 for item in a}
print(d)

# Checker si des valeurs sont nulles 
df.isnull()

#Supprimer les lignes de valeurs nulles 
df.dropna()

companies = df["company"]
print(companies)

print(df.describe)

#Afficher el nombre de fois qu'un valeur apparaît dans la data 
df.value_counts()
# cur.execute("CREATE TABLE movie(title, year, score)")

# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975,8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)


