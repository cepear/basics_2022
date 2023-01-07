# Functions with return statement

def build_full_name(firstname, lastname):
    """Returns full name."""
    print("starting to build full name")
    full_name = f"{firstname} {lastname}"
    return full_name.title()

#print('Result of the function : ', build_full_name('john', 'doe'))
#person2 = build_full_name(('john', 'doe'))
#print('Person2: ', person2)

#print('-----execise 8.6 ------------------------')
def city_country(city : str, country: str):
    """Returns name of city and country"""
    return  f"{city.title()}  {country.title()}"

print(city_country('paris', 'france'))
print(city_country('london', 'uk'))
print(city_country('new york', 'united states'))

print( '============exercise 8.7 ================')



