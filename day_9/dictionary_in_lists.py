travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# add_new_country() => allow add new country (dictionary) to the travel_log.
def add_new_country(country_name, visited, cities_name):
    travel_log.append({
        "country": country_name,
        "visits": visited,
        "cities": cities_name,
    }) 


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)