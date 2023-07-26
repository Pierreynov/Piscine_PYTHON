dict = {
       1 : "Monday",
       2 : "Tuesday",
       3 : "Wednesday",
       4 : "Thursday",
       5 : "Friday",
       6 : "Saturday",
       7 : "Sunday"
    }
toto = {
        "Monday" : 1,
        "Tuesday" : 2,
        "Wednesday" : 3,
        "Thursday" : 4,
        "Friday" : 5,
        "Saturday" : 6,
        "Sunday" : 7
    }
    
def day_from_number(day_number):
    if day_number in dict.keys() :
        return dict[day_number]
    return None

def day_to_number(day):
    if day in toto.keys() :
        return toto[day]
    return None