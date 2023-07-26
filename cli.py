import datetime_utils
import menu
import filter_recipes
import sort_list
import recipes
import read_recipes
import datetime as dt

import argparse
def build2_menu(recipes: list[str], start_date: dt.date) -> list[tuple[dt.date, str]] :
    res = []
    for i in recipes :
        tup = (start_date,i)
        res.append(tup)
        start_date = start_date + dt.timedelta(days= 1)
    return res   

parser = argparse.ArgumentParser()

parser.add_argument('-s', '--start', required= True)          
parser.add_argument('-p', '--max-persons', default = 4) 
args = parser.parse_args()
args.max_persons = (int(args.max_persons))
print(args.start, args.max_persons)

x = read_recipes.get_recipes('recipes_data.json')
y = sort_list.sort_recipes(x, 'title')
filter = filter_recipes.filter_recipes(y, args.max_persons)
args.start = dt.datetime.strptime(args.start,  "%d/%m/%Y")
m = build2_menu(filter, args.start)
menu.save_menu(m)    