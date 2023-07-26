def sort_recipes(recipes, by) : 
    if by != "persons" and by != "title" : 
        raise ValueError

    newlist = sorted(recipes, key= lambda recipes: recipes[by] )
    return newlist