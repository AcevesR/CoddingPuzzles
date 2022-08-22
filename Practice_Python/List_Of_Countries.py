countries = [("Mexico", "Spanish"),
            ("United States", "English"),
            ("France", "French"),
            ("Spain", "Spanish"),
            ("United Kingdom", "English"),
            ("Canada", "English"),
            ("Brazil", "Portuguese"),
            ("China", "Chinese"),
            ("Japan", "Japanese")]

print(countries)
     
def add_new_country(countries, name, language):
    countries.append((name, language))

add_new_country(countries, "Colombia", "Spanish")

print(countries)

def update_country(countries, index, name, language):
    countries[index] = (name, language)

update_country(countries, 1, "Germany", "German")

print(countries)

def find_countries_by_name(countries, name):
    return [country for country in countries if name in country[0]]

print(find_countries_by_name(countries, "Germany"))    

def get_all_countries(countries):
    return [country[0] for country in countries]

print(get_all_countries(countries))

def get_all_languages(countries):
    return [country[1] for country in countries]

print(get_all_languages(countries))
