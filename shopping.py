def remember_the_milk(shopping_list):
    if shopping_list == [] : return []

    x = 0
    for shop in shopping_list :
        shop = shop.lower()
        shop = shop.strip()
        if shop == "milk" : x = 1
    
    if x == 0 : shopping_list.append("milk")
    return shopping_list

def clean_list(shopping_list):
    remember_the_milk(shopping_list)
    result = []
    if shopping_list == [] : return []
    for index, shop in enumerate(shopping_list):
        shop = shop.strip()
        shop = shop.lower()
        shop = shop.capitalize()
        x = str(index+1)
        result.append(x + "/ "+shop)
    return result
