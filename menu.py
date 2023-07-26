import datetime as dt

def build_menu(recipes: list[dict], start_date: dt.date) -> list[tuple[dt.date, str]] :
    res = []
    for i in recipes :
        tup = (start_date,i["title"])
        res.append(tup)
        start_date = start_date + dt.timedelta(days= 1)
    return res   

def save_menu(meals: list[tuple[dt.date, str]]) :
    with open("menu.txt", "w") as f :
        for i in meals :
            res = i[0].strftime("%A %d %B %Y")
            f.write(res + ": " + i[1] + "\n")
       