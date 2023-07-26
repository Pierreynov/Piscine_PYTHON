def create_recipe(name, persons, ingredients) :
    res = {
        "title" : "",
        "persons" : 0,
        "ingredients" : []
    }
    if len(name) > 150 :
        raise ValueError("Title is too long")
    else : 
        res["title"] = name

    if persons == None or persons >50 or persons == 0 :
        raise ValueError ("Invalid persons number")
    else :
        res["persons"] = persons
    
    if ingredients == [] : 
        raise ValueError("This recipe has no ingredients")
    else :
        res["ingredients"] = ingredients
    
    return res 

def create_recipe_v2 (title, persons, *ingredients, **tags):
    
    if len(title) > 150 :
        raise ValueError("Title is too long")
    if persons == None or persons >50 or persons == 0 :
        raise ValueError ("Invalid persons number")
    if ingredients == () : 
        raise ValueError("This recipe has no ingredients")
    res = {
        "title" :title,
        "persons" : persons,
        "ingredients" : ingredients,
        "tags" : tags
    }
    return res 