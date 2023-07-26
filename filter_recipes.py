def filter_recipes(recipes: list[dict], max_persons: int) -> list[str] :
    return [x["title"] for x in recipes if x["persons"]< max_persons ]
